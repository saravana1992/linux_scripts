import subprocess

output = subprocess.call(["ls","-l ","/tmp/"])

print(output)
