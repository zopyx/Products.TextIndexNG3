#!/bin/bash

export PATH=\
/opt/buildout.python/bin:\
$PATH:

if [[ "$1" = "plone-4.3" ]]
then
    python_version=2.7
    config=alltests-plone43.cfg
fi

if [[ "$1" = "plone-5.0" ]]
then
    python_version=2.7
    config=alltests-plone50.cfg
fi

if [[ "$1" = "plone-5.1" ]]
then
    python_version=2.7
    config=alltests-plone51.cfg
fi

python --version
pip install -U setuptools==36.6.0
pip install zc.buildout==2.9.5
pip install six=1.10.0
buildout bootstrap
buildout -c $config
bin/test
