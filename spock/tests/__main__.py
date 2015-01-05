""" spock.tests.__main__
"""
import unittest2 as unittest
from spock.tests.test_basic import *
from spock.tests.test_temporal import *

if __name__=='__main__':
    unittest.main()
    from IPython import Shell; Shell.IPShellEmbed(argv=['-noconfirm_exit'])()
