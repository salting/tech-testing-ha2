#!/usr/bin/env python2

import sys
import unittest


from tests.target_tests import TargetTests

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(TargetTests),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())