import subprocess, os, errno
from pathlib import Path

class Neo4jUploader(object):

        def commandRunner(self, db_name, container_name, node_file, edge_file):
            node_file_path = "import/" + node_file
            edge_file_path = "import/" + edge_file
            adminImportResponse = subprocess.run(['docker', 'exec', '-it', container_name, '/var/lib/neo4j/bin/neo4j-admin', 'import', \
                '--database', db_name, \
                '--nodes', node_file_path, \
                '--relationships', edge_file_path ],
                capture_output=True, text=True, encoding="utf-8_sig" 
            )
            if adminImportResponse.returncode != 0:
                self.after_import_fail(db_name)
                # エラーメッセージ表示
                return adminImportResponse.stdout
            else:
                self.after_import_success(db_name)

        def after_import_success(self, db_name):
            self.dockerComposeDown()
            set_env = {**os.environ, 'DB_name': db_name}
            command = subprocess.run(['docker-compose', 'up'], env=set_env)
            if command.returncode != 0:
                return command.stdout

        def dockerComposeDown(self):
            command = subprocess.run(['docker-compose', 'down'],
                capture_output=True, text=True, encoding="utf-8_sig")
            if command.returncode != 0:
                return command.stdout

        def after_import_fail(self, db_name):
            path_to_databases = Path('data/databases/' + db_name)
            path_to_transactions = Path('data/transactions/' + db_name)

            if not path_to_databases.exists():
                raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path_to_databases)
            if not path_to_transactions.exists():
                raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path_to_transactions)

            delete_database = subprocess.run(['rm', '-rf', path_to_databases], 
                capture_output=True, text=True, encoding="utf-8_sig")
            delete_transaction = subprocess.run(['rm', '-rf', path_to_transactions], 
                capture_output=True, text=True, encoding="utf-8_sig")
            
            if delete_database.returncode != 0:
                return delete_database.stderr
            if delete_transaction.returncode != 0:
                return delete_transaction.stderr

exampleCmd = Neo4jUploader()
result = exampleCmd.commandRunner("testone", "newneo4j_neo4j_1", "nodes.csv", "relations.csv")
# result = exampleCmd.after_import_success("testdata")
# result = exampleCmd.after_import_fail("newdata")
if result:
    print(result)
else:
    print('success')
# adminImportResponse = subprocess.run(['docker', 'exec', '-it', 'newneo4j_neo4j_1', '/var/lib/neo4j/bin/neo4j-admin',\
#     'import','--database', 'pro', '--nodes', \
#     'import/nodes.csv', '--relationships', 'import/relationsN.csv'],\
#     capture_output=True, \
#     text=True, encoding="utf-8_sig" \
#     )