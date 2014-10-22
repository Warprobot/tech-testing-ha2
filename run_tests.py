#!/usr/bin/env python2

import unittest

import sys
from tests import test


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(test.Test),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())