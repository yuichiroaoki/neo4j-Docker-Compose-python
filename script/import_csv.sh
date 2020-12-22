#!/bin/bash
set -eu

# CSVインポート
echo "importing csv started."
/var/lib/neo4j/bin/neo4j-admin import \
  --database start \
  --nodes import/nodes.csv \
  --relationships import/relations.csv 
echo "importing csv finished."

