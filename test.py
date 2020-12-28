import subprocess

class Neo4jUploader(object):

        def commandRunner(self, db_name, project_name, container_name, node_file, edge_file):
            node_file_path = os.path.join(project_name, node_file)
            edge_file_path = os.path.join(project_name, edge_file)
            adminImportResponse = subprocess.run(['docker', 'exec', '-it', container_name, './bin/neo4j-admin', 'import', \
                '--database', db_name, \
                '--nodes', node_file_path, \
                '--relationships', edge_file_path ], \
                capture_output=True, \
                text=True, encoding="utf-8_sig" \
                )
            if adminImportResponse.returncode != 0:
                # エラーメッセージ表示
                return adminImportResponse.stdout
            else:
                return True

# adminImportResponse = subprocess.run(['docker', 'exec', '-it', 'newneo4j_neo4j_1', './bin/neo4j-admin',\
#     'import','--database', 'pro', '--nodes', \
#     'import/nodes.csv', '--relationships', 'import/relationsN.csv'],\
#     capture_output=True, \
#     text=True, encoding="utf-8_sig" \
#     )