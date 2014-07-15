# coding: utf-8
from fabric.api import *

def build():
    """
    build docker containers
    """
    with lcd('base'):
        local('pwd')
        local('docker build -t base/java7 .')

    with lcd('jenkins'):
        local('pwd')
        local('docker build -t base/jenkins .')

def start_jenkins():
    pass
