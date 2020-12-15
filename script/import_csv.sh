#!/bin/bash
set -eu

# CSVインポート
echo "importing csv started."
/var/lib/neo4j/bin/neo4j-admin import \
  --database smalldata.db \ 
  --nodes import/nodes.csv \
  --relationships import/relations.csv 
  --id-type=INTEGER   > import.out
echo "importing csv finished."

