import subprocess

# p1 = subprocess.run(['ls', '-la', 'the'], 
#     capture_output=True, text=True, check=True)

p2 = subprocess.run(['docker-compose', 'up', '-d'],
    capture_output=True, text=True, check=True)

# shows 0 if there no error
# print(p1.returncode)

# print(p1.stdout)

if p2.returncode != 0:
    print(p1.stderr)
else:
    print('success')