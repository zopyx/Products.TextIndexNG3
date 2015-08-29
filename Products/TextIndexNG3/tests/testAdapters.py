# -*- coding: iso-8859-15 -*-

###########################################################################
# TextIndexNG V 3
# The next generation TextIndex for Zope
#
# This software is governed by a license. See
# LICENSE.txt for the terms of this license.
###########################################################################

"""
adapter unit tests

$Id: testAdapters.py 2311 2011-04-20 10:01:11Z yvoschu $
"""

import unittest
import pkg_resources
import os
import sys
import txngtest
from Testing import ZopeTestCase

ZopeTestCase.installProduct('ZCatalog', 1)
ZopeTestCase.installProduct('TextIndexNG3', 1)

from zopyx.txng3.core import tests

try:
    pkg_resources.get_distribution('plone.indexer')
except pkg_resources.DistributionNotFound:
    _PLONE_INDEXER_INSTALLED = False
else:
    _PLONE_INDEXER_INSTALLED = True

_DATA_DIR = os.path.join(os.path.dirname(tests.__file__), 'data')


class PloneIndexerAdapterTests(unittest.TestCase):

    layer = txngtest.TextIndexNG3ZCMLLayer

    def testCorrectAdapter(self):
        from zope.component import provideAdapter

        from Products.CMFCore.PortalContent import PortalContent
        from plone.indexer.interfaces import IIndexer as PIIIndexer
        from plone.indexer.wrapper import IndexableObjectWrapper \
            as PIIndexableObjectWrapper

        from zopyx.txng3.core.interfaces import IIndexableContent

        d = PortalContent()
        piwrapper = PIIndexableObjectWrapper(d, None)
        txngwrapper = IIndexableContent(piwrapper)
        def SearchableText():
            return ""
        provideAdapter(lambda a,b:SearchableText, (None, None), \
            PIIIndexer, name='SearchableText')
        # This can throw an exception if the adapter is not prepared for
        # the "transparent" Plone Indexer wrapper
        txngwrapper.indexableContent('SearchableText')


def test_suite():
    s = unittest.TestSuite()
    if _PLONE_INDEXER_INSTALLED:
        s.addTest(unittest.makeSuite(PloneIndexerAdapterTests))
    else:
        print 'Products.TextIndexNG3: Skipped Plone Indexer adapter tests.'
    return s

def main():
    unittest.TextTestRunner().run(test_suite())

def debug():
    test_suite().debug()

def pdebug():
    import pdb
    pdb.run('debug()')

if __name__=='__main__':
    if len(sys.argv) > 1:
        globals()[sys.argv[1]]()
    else:
        main()
