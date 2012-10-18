# Installation lib for fabric

__author__ = 'Colin Su <littleq0903@gmail.com'

from fabric.api import *
from fabric.operations import *
from fabric.utils import *
from fabric.contrib.files import *
from fabric.colors import green, yellow, red


def install_python():
    """
    Install python-dev headers
    """
    print yellow("Installing python...")
    sudo("apt-get install -y python-dev")


def install_django_nonrel():
    """
    Installs django-nonrel
    """
    print yellow("Installing django-nonrel...")

    with prefix('cd %(src_path)s' % env):
        run('hg clone https://bitbucket.org/wkornewald/django-nonrel' % env)
    with prefix('source %(env_path)s/bin/activate' % env):
        run('python %(src_path)s/django-nonrel/setup.py --quiet install' % env)

def install_mongodb():
    """
    Install MongoDB
    """
    print yellow("Installing MongoDB...")
    sudo("apt-get install -y mongodb")

def install_mercurial():
    """
    Install Mercurial (HG)
    """
    print yellow("Installing Mercurial...")
    sudo("apt-get install -y mercurial")

def install_virtualenv():
    """
    Install Virtual Environment Tool for Python
    """
    print yellow("Installing Python Virtual Environment...")
    sudo("apt-get install -y python-virtualenv")

def install_pil_requirements():
    """
    Install Python Image Library requirements:
        * python-imaging
        * libjpeg-dev
    """
    print yellow("Installing PIL requirements...")
    sudo("apt-get install -y python-imaging")
    sudo("apt-get install -y libjpeg-dev")

def install_lxml_requirements():
    """
    Install the requirements for lxml module:
        * libxml2-dev
        * libxslt1-dev
    """
    print yellow("Installing lxml requirements...")
    sudo("apt-get install -y libxml2-dev libxslt1-dev")

"""
Apache modules
"""
def install_apache_modules(module_names = ["libapache2-mod-wsgi"]):
    """
    Install Apache modules:
        * libapache2-mod-wsgi
    """
    print yellow("Installing Apache Modules:")

    for module_name in module_names:
        print yellow("Installing %s..." % module_name)
        sudo("apt-get install -y %s" % module_name)

