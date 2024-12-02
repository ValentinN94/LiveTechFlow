import subprocess
import shlex

def init_git_repo_for_user(username:str):

    subprocess.call(shlex.split(f'/home/livetechromania/LiveTechFlow/git_init.sh {username}'))