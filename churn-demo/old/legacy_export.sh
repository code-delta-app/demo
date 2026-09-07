#!/usr/bin/env bash
# Legacy CSV export — removed in the new version.
set -e
out="${1:-ledger.csv}"
printf "kind,amount\n" > "$out"
grep -h "^entry" ledger.log | cut -d" " -f2,3 | tr " " "," >> "$out"
echo "wrote $out"
