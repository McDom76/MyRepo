import json
import subprocess

outxbytes = subprocess.check_output("curl https://api.github.com/users/McDom76", shell=True)

outcmd = str(outxbytes)
text = ["login: hennd"]
list_output = outcmd.split(",\\n")
pos_login = outcmd.find("login")

print("Now cmdout:")
print(pos_login)
print("\n ----------------")