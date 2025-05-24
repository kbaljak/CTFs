import subprocess

FLAG = 'KibSec{fake_flag_for_testing}'

def call_fortune():
    result = subprocess.run(['fortune'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def get_fortune(cookie):
    if b"user=admin" in cookie.split(b";"):
        return {"fortune": FLAG}
    else:
        return {"fortune": call_fortune()}
