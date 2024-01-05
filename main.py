import subprocess

# Run command
command = subprocess.run(['uhubctl', '-l', '1-1', '-p', '2', '-a', 'toggle'], capture_output=True, text=True)

# Print output
print("Output:", command.stdout)
print("Return Code:", command.returncode)