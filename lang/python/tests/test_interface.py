"""
Unit tests for interface
"""
# System imports
import os
import time
import unittest

# Load imports
import airr

# Paths
test_path = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.join(test_path, 'data')


class TestInferface(unittest.TestCase):
    def setUp(self):
        print('-------> %s()' % self.id())

        # Test data
        self.data_good = os.path.join(data_path, 'good_data.tsv')
        self.data_bad = os.path.join(data_path, 'bad_data.tsv')

        # Expected output
        self.shape_good = (9, 44)
        self.shape_bad = (9, 44)

        # Start timer
        self.start = time.time()

    def tearDown(self):
        t = time.time() - self.start
        print('<- %.3f %s()' % (t, self.id()))

    # @unittest.skip('-> load(): skipped\n')
    def test_load(self):
        # Good data
        result = airr.load_rearrangement(self.data_good)
        self.assertTupleEqual(result.shape, self.shape_good, 'load(): good data failed')

        # Bad data
        result = airr.load_rearrangement(self.data_bad)
        self.assertTupleEqual(result.shape, self.shape_bad, 'load(): bad data failed')

    # @unittest.skip('-> validate(): skipped\n')
    def test_validate(self):
        # Good data
        try:
            result = airr.validate_rearrangement(self.data_good)
            self.assertTrue(result, 'validate(): good data failed')
        except:
            self.assertTrue(False, 'validate(): good data failed')

        # Bad data
        try:

            result = airr.validate_rearrangement(self.data_bad)
            self.assertFalse(result, 'validate(): bad data failed')
        except:
            pass


if __name__ == '__main__':
    unittest.main()
