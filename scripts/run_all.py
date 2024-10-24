import subprocess

# Run download.py
subprocess.run(["python", "download.py"])

#Print contents
subprocess.run(['ls', '-R'])

# Run extract.py
subprocess.run(["python", "extract.py"])

# # Run parse.py
subprocess.run(["python", "parse.py"])
