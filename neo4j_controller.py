import subprocess, os, errno
from pathlib import Path
from neo4j import GraphDatabase, basic_auth

class Neo4jController(object):

    def __init__(self, url, user, password):
        self.driver = GraphDatabase.driver(url, auth=(user, password))
    
    def close(self):
        self.driver.close()

    def admin_import(self, db_name, container_name, node_file, edge_file):
        node_file_path = "import/" + node_file
        edge_file_path = "import/" + edge_file
        adminImportResponse = subprocess.run(['docker', 'exec', '-it', container_name, '/var/lib/neo4j/bin/neo4j-admin', 'import', \
            '--database', db_name, \
            '--nodes', node_file_path, \
            '--relationships', edge_file_path ],
            capture_output=True, text=True, encoding="utf-8_sig" 
        )
        if adminImportResponse.returncode != 0:
            print(adminImportResponse.stdout)
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

    def dockerComposeRestart(self, service_name):
        command = subprocess.run(['docker-compose', 'restart',  service_name],
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
        
    def run_command(self, db_name):
        with self.driver.session() as session:
            result = session.write_transaction(
                self.change_database, db_name
            )
            for record in result:
                print(record)
            self.close()


    @staticmethod
    def change_database(tx, db_name):
        query = (
            "USE $db_name "
            "MATCH p=()-->() RETURN p "
        )
        result = tx.run(query, db_name=db_name)

        try:
            return [record for record in result]
        except Exception as e:
            raise e

scheme = "bolt"
host_name = "localhost"
port = 7687
url = f"{scheme}://{host_name}:{port}"
user = "neo4j"
password = "password"
exampleCmd = Neo4jController(url, user, password)
result = exampleCmd.run_command("testone")