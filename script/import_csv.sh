#!/bin/bash
set -eu

# CSVインポート
echo "importing csv started."
/var/lib/neo4j/bin/neo4j-admin import \
  --database testdata \
  --nodes import/nodes.csv \
  --relationships import/relations.csv 
  --id-type INTEGER
echo "importing csv finished."

