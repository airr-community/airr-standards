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
        self.rep_good = os.path.join(data_path, 'good_repertoire.airr.yaml')
        self.rep_bad = os.path.join(data_path, 'bad_repertoire.airr.yaml')

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

    # @unittest.skip('-> repertoire_template(): skipped\n')
    def test_repertoire_template(self):
        try:
            rep = airr.repertoire_template()
            result = airr.schema.RepertoireSchema.validate_object(rep)
            self.assertTrue(result, 'repertoire_template(): repertoire template failed validation')
        except:
            self.assertTrue(False, 'repertoire_template(): repertoire template failed validation')

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

    # @unittest.skip('-> load_repertoire(): skipped\n')
    def test_load_repertoire(self):
        # Good data
        try:
            data = airr.load_repertoire(self.rep_good, validate=True)
        except:
            self.assertTrue(False, 'load_repertoire(): good data failed')

        # Bad data
        try:
            data = airr.load_repertoire(self.rep_good, validate=True)
            self.assertFalse(True, 'load_repertoire(): bad data failed')
        except:
            pass

if __name__ == '__main__':
    unittest.main()
