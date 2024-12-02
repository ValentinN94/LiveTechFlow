import subprocess
import shlex

def init_git_repo_for_user(username:str):
    subprocess.call(shlex.split(f'sudo /home/livetechromania/LiveTechFlow/git_operations.py {username}'))