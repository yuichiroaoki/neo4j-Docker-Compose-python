import subprocess

p1 = subprocess.run(['ls', '-la', 'the'], 
    capture_output=True, text=True, check=True)

# shows 0 if there no error
print(p1.returncode)

print(p1.stdout)