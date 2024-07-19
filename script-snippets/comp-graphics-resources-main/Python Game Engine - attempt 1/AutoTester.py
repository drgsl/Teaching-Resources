import subprocess

command = "python -m Tests.SceneTests"

# Run the command as a subprocess and capture the output and errors
completed_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = completed_process.communicate()

# Print the captured output and errors
print("Standard Output:")
print(stdout.decode("utf-8"))
print("Standard Error:")
print(stderr.decode("utf-8"))

# Check the return code to handle errors if needed
if completed_process.returncode != 0:
    print("An error occurred.")
