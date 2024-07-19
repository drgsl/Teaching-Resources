import os

import subprocess

command = "python -m PyUnity/GUI"

# Run the command as a subprocess and capture the output and errors
completed_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = completed_process.communicate()

print(stdout)
print(stderr)










