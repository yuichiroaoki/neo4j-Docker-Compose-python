#!/bin/bash
set -eu

# データを全削除
# echo "delete database started."
# rm -rf /var/lib/neo4j/data/databases
# rm -rf /var/lib/neo4j/data/transactions
# echo "delete database finished."

# CSVインポート
echo "importing csv started."
/var/lib/neo4j/bin/neo4j-admin import \
  --database smalldata \ 
  --nodes import/nodes.csv \
  --relationships import/relations.csv 
  --id-type=INTEGER   > import.out
echo "importing csv finished."

