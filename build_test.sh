#!/bin/bash

export PATH=\
/opt/buildout.python/bin:\
$PATH:

if [[ "$1" = "plone-4.0" ]]
then
    python_version=2.6
    config=alltests-plone40.cfg
fi

if [[ "$1" = "plone-4.1" ]]
then
    python_version=2.6
    config=alltests-plone41.cfg
fi

if [[ "$1" = "plone-4.2" ]]
then
    python_version=2.6
    config=alltests-plone42.cfg
fi

if [[ "$1" = "plone-4.3" ]]
then
    python_version=2.7
    config=alltests-plone43.cfg
fi

virtualenv-$python_version .
bin/python bootstrap.py -c $config
bin/buildout -c $config
bin/alltests-jenkins --xml
