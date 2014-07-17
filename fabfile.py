# coding: utf-8
import os
from fabric.api import *


def build():
    """
    build docker containers
    """
    with lcd('base'):
        local('pwd')
        local('docker build -t cloud/base .')


def build_one(name='base'):
    """
    build image by name
    """
    with settings(warn_only=True):
        with lcd(name):
            local('pwd')
            local('docker build -t cloud/' + name + ' .')

def build_all():
    """
    build all images define by Dockerfile
    """
    build_one('base')
    execute_dirs = ['base', '.git', '.gitignore', 'bin', 'fabfile.py', 'fabfile.pyc', 'LICENSE', 'README.md', 'setup.sh']
    dirs = os.listdir('.')
    dirs = filter(lambda v: v not in execute_dirs, dirs)
    for subdir in dirs:
        build_one(subdir)
