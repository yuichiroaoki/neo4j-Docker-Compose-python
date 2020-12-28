import subprocess

p2 = subprocess.run(['docker', 'exec', '-it', 'newneo4j_neo4j_1', './bin/neo4j-admin',\
    'import','--database', 'pro', '--nodes', \
    'import/nodes.csv', '--relationships', 'import/relationsN.csv'],\
    capture_output=True, \
    text=True, encoding="utf-8_sig" \
    )
if p2.returncode != 0:
    # エラーメッセージ表示
    print(p2.stdout)
else:
    print('success')