import subprocess

def check_output(command, text):
    try:
        output = subprocess.check_output(command, shell=True).decode()
        if text in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False


command = "add‑repo"
text = "action"
result = check_output(command, text)
print(result)