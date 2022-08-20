from fabric.api import *
from fabric.api import local

env.hosts = ['gisconsulting4.com']
env.password = '<fulani>'
venv = 'source /venv/bin/activate'
env.user = 'fulani'

# env.hosts = ['localhost']
# env.user = 'root'
# env.password = '<remote-server-password>'
# env.full_name_user = '<your-name>'
# env.user_group = 'deployers'
# env.user_name = 'deployer'
# ssh key path
# env.ssh_keys_dir = os.path.join(abs_dir_path, 'ssh-keys')




def test():
 print("Hello world!")




