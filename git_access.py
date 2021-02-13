import json
import subprocess

output = subprocess.check_output("curl https://api.github.com/users/McDom76", shell=True)




print("Now cmdout:")
print(output)
print("\n ----------------")
