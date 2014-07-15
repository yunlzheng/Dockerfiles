# coding: utf-8
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
    with lcd(name):
        local('pwd')
        local('docker build -t cloud/' + name + ' .')
