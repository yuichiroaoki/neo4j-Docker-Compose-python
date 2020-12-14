from neo4j import GraphDatabase, Driver
from neobolt.exceptions import ServiceUnavailable
import subprocess
import time
import traceback

class Neo4jServer:
    def __enter__(self):
        """
        dockerコンテナを起動する
        """
        subprocess.run(['docker-compose', 'up'],
        capture_output=True, text=True, check=True)
        while self.__neo4j_available() is False:
            time.sleep(10)
            
        # if start_neo4j.returncode != 0:
        #     print(start_neo4j.stderr)
        return self

    def __exit__(self, exc_type, exc_value, tb):
        """
        dockerコンテナを停止する
        """
        if tb is not None:
            print(''.join(traceback.format_tb(tb)))
        subprocess.run(['docker-compose', 'stop'])

    def __neo4j_available(self) -> bool:
        """
        Neo4jが利用可能かどうかをチェックする
        """
        try:
            GraphDatabase.driver('bolt://localhost:7687', auth=('neo4j', 'password'), encrypted=False)
        except:
            print('neo4j is not available yet.')
            return False
        print('neo4j is already available.')
        return True

with Neo4jServer():
    driver: Driver = GraphDatabase.driver('bolt://localhost:7687', auth=('neo4j', 'password'), encrypted=False)
    with driver.session() as session:
        print(f"node_count: {session.run('MATCH (n:Node) RETURN count(n) as cnt').single()['cnt']}")
        print(f"relationship_count: {session.run('MATCH ()-[l:LINKED]->() RETURN count(l) as cnt').single()['cnt']}")