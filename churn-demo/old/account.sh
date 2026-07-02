#!/bin/sh
balance=0
history=""

deposit() {
  balance=$((balance + $1))
  history="$history deposit"
}

withdraw() {
  balance=$((balance - $1))
  history="$history withdraw"
}

apply_fee() {
  balance=$((balance - $1))
  history="$history fee"
}

get_balance() {
  echo "$balance"
}

is_overdrawn() {
  [ "$balance" -lt 0 ]
}

print_statement() {
  for e in $history; do
    echo "$e"
  done
}
