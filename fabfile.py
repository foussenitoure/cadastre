#!/usr/bin/python
# -*- coding: utf-8 -*-

from virtualenv.activation import bash
#!/usr/bash
# -*- coding: utf-8 -*-
# os.environ["PYTHONIOENCODING"] = "utf-8"

from fabric.api import *
import time
from cryptography.hazmat.backends import default_backend

from fabric.api import local

# env.hosts = ['root@gisconsulting4.com']
import pyblog


env.hosts = ['www.gisconsulting4.com']
# env.hosts = ['root@165.232.131.54']
env.password = 'fulani'
env.user = 'fulani'
venv = 'source /home/fulani/giscon/cadastre/venv/bin/activate'

# GIT_REPO = "https://github.com/foussenitoure/cadastre.git:gisconsulting"

repo='https://github.com/foussenitoure/cadastre.git:gisconsulting'
# repo='https://github.com/foussenitoure/cadastre:gisconsulting.git'
# repo='git@github.com:cadastre/gisconsulting.git'
timestamp="release_%s" % int(time.time() * 1000)
# https://github.com/foussenitoure/cadastre
# env.hosts = ['localhost']
# env.user = 'root'
# env.password = '<remote-server-password>'
# env.full_name_user = '<your-name>'
# env.user_group = 'deployers'
# env.user_name = 'deployer'
# ssh key path
# env.ssh_keys_dir = os.path.join(abs_dir_path, 'ssh-keys')



def _install_doc():
    sudo("%s && pip install -r requirements.txt" % venv)


def _get_code():
    cd("%s git fetch origin gisconsulting")


def _makemigrations():

    sudo("%s && python manage.py makemigrations" % venv)

def _migrate():
    sudo("%s && python manage.py migrate" % venv)

def _reload():
    cd("touch rebuild")
    sudo('service nginx reload')

@task(alias="d")
def basic_deploy():
     with cd('/home/fulani/giscon/cadastre'):
        _install_doc()
        _get_code()
        _reload()

@task(alias="dwn")
def deploy():
     with cd('/home/fulani/giscon/cadastre'):
        _install_doc()
        _get_code()
        _makemigrations()
        _migrate()
        _reload()



