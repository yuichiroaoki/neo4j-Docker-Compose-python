#!/bin/bash
set -eu

# CSVインポート
echo "importing csv started."
/var/lib/neo4j/bin/neo4j-admin import \
  --database dectwenty8 \
  --nodes import/nodes.csv \
  --relationships import/relationsN.csv 
echo "importing csv finished."

