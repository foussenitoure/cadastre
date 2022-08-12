#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
# from multiprocessing import Connection

from fabric.api import *
# $ export PYTHONIOENCODING=utf8
from fabric.api import *

# server = Connection(host="root@147.182.235.200:22", connect_kwargs={"password": "Allahkbarou1@Portail"})
# server = Connection(host="root@147.182.235.200:22", connect_kwargs={"password": "Allahkbarou1@Portail"})
# server = Connection(host="ombportail.net:22", connect_kwargs={"password": "fulani"})
# server = Connection(host="root@server.com:22", connect_kwargs={"password": "mypassword"})
env.hosts = ['root@147.182.235.200']
venv = 'source /opt/geoportail/cadastre/venv/bin/activate'

def _install_doc():
    sudo("%s && pip install -r requirements_cada.txt" % venv)

def _migrate():
    sudo("%s && python manage.py migrate" % venv)

def _get_code():
    sudo("%s git pull origin main_cadastre")
def _reload():
    sudo("touch rebuild")

@task(alias="d")
def basic_deploy():
     with cd('/opt/geoportail/cadastre'):
        _install_doc()
        _get_code()
        _reload()

@task(alias="dwn")
def deploy():
     with cd('/opt/geoportail/cadastre'):
        _install_doc()
        _migrate()
        _get_code()
        _reload()