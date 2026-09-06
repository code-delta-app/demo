#!/usr/bin/env bash
# Ledger — a tiny bash account ledger

declare -A summary
declare -a entries
name="${1:-main}"
previous_name=""
balance=0
limit=0
interest_paid=0
transfers=0
pending_holds=0
cleared_items=0
flagged_items=0
disputed_items=0

average_of() {
    local sum=$1
    local n=$2
    if [ "$n" -eq 0 ]; then
        echo 0
        return
    fi
    echo $((sum / n))
}

post() {
    local status=$1
    local amount=$2
    entries+=("$name:$status:$amount")
    balance=$((balance + amount))
    log "posted"
}

credit() {
    post posted "$1"
    cleared_items=$((cleared_items + 1))
}

debit() {
    post posted "-$1"
    cleared_items=$((cleared_items + 1))
}

hold() {
    post pending "$1"
    pending_holds=$((pending_holds + 1))
}

dispute() {
    post disputed "$1"
    disputed_items=$((disputed_items + 1))
    flagged_items=$((flagged_items + 1))
}

transfer() {
    local target_file=$1
    local amount=$2
    debit "$amount"
    echo "posted:$amount" >> "$target_file"
    transfers=$((transfers + 1))
}

apply_interest() {
    local rate_pct=$1
    local interest=$((balance * rate_pct / 100))
    post posted "$interest"
    interest_paid=$((interest_paid + interest))
}

flag_large() {
    local threshold=$1
    local n=0
    for e in "${entries[@]}"; do
        local amount=${e#*:}
        if [ "${amount#-}" -gt "$threshold" ]; then
            n=$((n + 1))
        fi
    done
    flagged_items=$((flagged_items + n))
    echo "$n"
}

largest_entry() {
    local best=0
    for e in "${entries[@]}"; do
        local amount=${e#*:}
        if [ "${amount#-}" -gt "${best#-}" ]; then
            best=$amount
        fi
    done
    echo "$best"
}

statement_line() {
    local e=${entries[$1]}
    echo "${e%%:*}:${e#*:}"
}

rename_ledger() {
    previous_name=$name
    name=$1
    log "renamed"
}

net_flow() {
    echo $(( $(sum_signed 1) - $(sum_signed -1) ))
}

reset_ledger() {
    entries=()
    summary=()
    balance=0
    log "reset"
}

sum_signed() {
    local sign=$1
    local sum=0
    for e in "${entries[@]}"; do
        local amount=${e#*:}
        if [ "$sign" -gt 0 ] && [ "$amount" -ge 0 ]; then
            sum=$((sum + amount))
        elif [ "$sign" -lt 0 ] && [ "$amount" -lt 0 ]; then
            sum=$((sum - amount))
        fi
    done
    echo "$sum"
}

count_status() {
    local wanted=$1
    local n=0
    for e in "${entries[@]}"; do
        if [ "${e%%:*}" = "$wanted" ]; then
            n=$((n + 1))
        fi
    done
    echo "$n"
}

set_limit() {
    limit=$1
    log "limit changed"
}

over_limit() {
    [ "$balance" -lt "$((-limit))" ]
}

entry_count() {
    echo "${#entries[@]}"
}

summary_value() {
    echo "${summary[$1]:-0}"
}

reconcile() {
    local opening=$balance
    local credits=$(sum_signed 1)
    local debits=$(sum_signed -1)
    local closing=$((opening + credits - debits))
    local drift=$((closing - balance))
    local posted_n=$(count_status posted)
    local pending_n=$(count_status pending)
    local disputed_n=$(count_status disputed)
    local total=$((posted_n + pending_n + disputed_n))
    local average=$(average_of $((credits + debits)) "$total")
    summary[opening]=$opening
    summary[credits]=$credits
    summary[debits]=$debits
    summary[closing]=$closing
    summary[drift]=$drift
    summary[posted]=$posted_n
    summary[pending]=$pending_n
    summary[disputed]=$disputed_n
    summary[average]=$average
    balance=$((closing + interest_paid))
}

log() {
    :
}
