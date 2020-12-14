#!/bin/bash
set -euC

# CSVファイルがなければ何もしない
if [[ "$(ls -1 /import | wc -l)" == "0" ]]; then
    echo "import csv skipped."
    return
fi

# データを全削除
echo "delete database started."
rm -rf /var/lib/neo4j/data/databases
rm -rf /var/lib/neo4j/data/transactions
echo "delete database finished."

# CSVインポート
echo "importing csv started."
/var/lib/neo4j/bin/neo4j-admin import \
  --id-type=INTEGER \
  --nodes="/var/lib/neo4j/import/nodes.csv" \
  --relationships="/var/lib/neo4j/import/relations.csv"
echo "importing csv finished."