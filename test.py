import subprocess

p2 = subprocess.run(['docker-compose', 'up', '-d'],
    capture_output=True, text=True, check=True)

if p2.returncode != 0:
    print(p1.stderr)
else:
    print('success')