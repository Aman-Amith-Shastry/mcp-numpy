import subprocess
import json
import time

proc = subprocess.Popen(
    ["python", "main.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1
)

startup_message = proc.stdout.readline()
print("Startup:", startup_message)

# Wait a bit for server to initialize
time.sleep(0.5)

# If it crashed, report why
if proc.poll() is not None:
    print("Server crashed with return code", proc.returncode)
    print("Stderr:\n", proc.stderr.read())
    exit()

# Build request
request = {
    "jsonrpc": "2.0",
    "id": 1,
    "tool": "create_matrix",
    "input": {
        "shape": [2, 2],
        "values": [1, 2, 3, 4],
        "name": "m1"
    }
}

try:
    proc.stdin.write(json.dumps(request) + "\n")
    proc.stdin.flush()
except Exception as e:
    print("Error writing to stdin:", e)
    print("Stderr:", proc.stderr.read())
    exit()

# Read and print response
response = proc.stdout.readline()

print("Response:", response)