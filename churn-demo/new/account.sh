#!/bin/sh
balance=0
min_balance=0
history=""

deposit() {
  balance=$((balance + $1))
  history="$history DEPOSIT"
}

withdraw() {
  balance=$((balance - $1))
  history="$history WITHDRAW"
}

apply_fee() {
  balance=$((balance - $1))
  history="$history FEE"
}

get_balance() {
  echo "$balance"
}

is_overdrawn() {
  [ "$balance" -lt "$min_balance" ]
}

apply_interest() {
  balance=$((balance + balance * $1 / 100))
  history="$history INTEREST"
}
