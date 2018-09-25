"""
Unit tests for interface
"""
# System imports
import os
import time
import unittest

# Load imports
from airr.io import *

# Paths
test_path = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.join(test_path, 'data')


class TestRearrangementReader(unittest.TestCase):
    def setUp(self):
        print('-------> %s()' % self.id())

        # Test data
        self.data_good = os.path.join(data_path, 'good_data.tsv')
        self.data_bad = os.path.join(data_path, 'bad_data.tsv')

        # Start timer
        self.start = time.time()

    def tearDown(self):
        t = time.time() - self.start
        print('<- %.3f %s()' % (t, self.id()))

    # @unittest.skip('-> validate(): skipped\n')
    def test_validate(self):
        # Good data
        try:
            with open(self.data_good, 'r') as handle:
                reader = RearrangementReader(handle, validate=True)
                for r in reader:
                    pass
        except:
            self.assertTrue(False, 'validate(): good data failed')

        # Bad data
        try:
            with open(self.data_bad, 'r') as handle:
                reader = RearrangementReader(handle, validate=True)
                for r in reader:
                    pass
            self.assertFalse(True, 'validate(): bad data failed')
        except:
            pass

if __name__ == '__main__':
    unittest.main()
