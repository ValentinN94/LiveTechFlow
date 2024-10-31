import subprocess
import shlex

def init_git_repo_for_user(username:str):
    subprocess.call(shlex.split(f'/root/new.sh {username}'))

init_git_repo_for_user('okok')