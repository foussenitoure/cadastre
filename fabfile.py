from fabric.api import *
from fabric.api import local

env.hosts = ['localhost']
env.user = 'root'
env.password = '<remote-server-password>'
env.full_name_user = '<your-name>'
env.user_group = 'deployers'
env.user_name = 'deployer'
# ssh key path
# env.ssh_keys_dir = os.path.join(abs_dir_path, 'ssh-keys')

venv = 'source /venv/bin/activate'

def test():
 print("Hello world!")



# def say_hi():
#     local("echo hi!")