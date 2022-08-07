"""
Unit tests for interface
"""
# System imports
import os
import time
import unittest
import jsondiff
import sys

# Load imports
import airr
from airr.schema import ValidationError

# Paths
test_path = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.join(test_path, 'data')


class TestInferface(unittest.TestCase):
    def setUp(self):
        print('-------> %s()' % self.id())

        # Test data
        self.data_good = os.path.join(data_path, 'good_rearrangement.tsv')
        self.data_bad = os.path.join(data_path, 'bad_rearrangement.tsv')
        self.rep_good = os.path.join(data_path, 'good_repertoire.yaml')
        self.rep_bad = os.path.join(data_path, 'bad_repertoire.yaml')
        self.germline_good = os.path.join(data_path, 'good_germline_set.json')
        self.germline_bad = os.path.join(data_path, 'bad_germline_set.json')
        self.genotype_good = os.path.join(data_path, 'good_genotype_set.json')
        self.genotype_bad = os.path.join(data_path, 'bad_genotype_set.json')

        # Output data
        self.output_rep_good = os.path.join(data_path, 'output_rep_data.json')
        self.output_good = os.path.join(data_path, 'output_data.json')

        # Expected output
        self.shape_good = (9, 44)
        self.shape_bad = (9, 44)

        # Start timer
        self.start = time.time()

    def tearDown(self):
        t = time.time() - self.start
        print('<- %.3f %s()' % (t, self.id()))

    # @unittest.skip('-> load(): skipped\n')
    def test_load_rearrangement(self):
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
    def test_validate_rearrangement(self):
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
        except Exception as inst:
            print(type(inst))
            raise inst

    # @unittest.skip('-> load_airr_data(): skipped\n')
    def test_read_airr(self):
        # Good data
        try:
            data = airr.read_airr(self.rep_good, validate=True, debug=True)
        except:
            self.assertTrue(False, 'load_airr_data(): good data failed')

        # Bad data
        try:
            data = airr.read_airr(self.rep_bad, validate=True, debug=True)
            self.assertFalse(True, 'load_airr_data(): bad data failed')
        except ValidationError:
            pass
        except Exception as inst:
            print(type(inst))
            raise inst

    # @unittest.skip('-> validate_airr_data(): skipped\n')
    def test_validate_airr(self):
        # Good data
        try:
            result = airr.validate_airr(self.rep_good, debug=True)
            self.assertTrue(result, 'validate_airr_data(): good data failed')
        except:
            self.assertTrue(False, 'validate_airr_data(): good data failed')

        # Bad data
        try:
            result = airr.validate_airr(self.rep_bad, debug=True)
            self.assertFalse(result, 'validate_airr_data(): bad data failed')
        except ValidationError:
            pass
        except Exception as inst:
            print(type(inst))
            raise inst

    # @unittest.skip('-> load_repertoire(): skipped\n')
    def test_read_repertoire(self):
        # Good data
        try:
            data = airr.load_repertoire(self.rep_good, validate=True, debug=True)
        except:
            self.assertTrue(False, 'load_repertoire(): good data failed')

        # Bad data
        try:
            data = airr.load_repertoire(self.rep_bad, validate=True, debug=True)
            self.assertFalse(True, 'load_repertoire(): bad data failed')
        except ValidationError:
            pass
        except Exception as inst:
            print(type(inst))
            raise inst

    # @unittest.skip('-> write_repertoire(): skipped\n')
    def test_write_repertoire(self):
        # Good data
        try:
            data = airr.load_repertoire(self.rep_good, validate=True, debug=True)
            result = airr.write_repertoire(self.output_rep_good, data['Repertoire'], debug=True)

            # verify we can read it
            obj = airr.load_repertoire(self.output_rep_good, validate=True, debug=True)

            # is the data identical?
            if jsondiff.diff(obj['Repertoire'], data['Repertoire']) != {}:
                print('Output data does not match', file=sys.stderr)
                print(jsondiff.diff(obj, data), file=sys.stderr)
                self.assertTrue(False, 'write_repertoire(): Output data does not match')
        except:
            self.assertTrue(False, 'write_repertoire(): good data failed')

    # @unittest.skip('-> load_germline(): skipped\n')
    def test_read_germline(self):
        # Good data
        try:
            result = airr.read_airr(self.germline_good, validate=True, debug=True)
        except ValidationError:
            self.assertTrue(False, 'load_germline(): good data failed')

        # Bad data
        try:
            result = airr.read_airr(self.germline_bad, validate=True, debug=True)
            self.assertFalse(True, 'load_germline(): bad data succeeded')
        except ValidationError:
            pass

    # @unittest.skip('-> validate_germline(): skipped\n')
    def test_validate_germline(self):
        # Good data
        try:
            result = airr.validate_airr(self.germline_good, debug=True)
            self.assertTrue(result, 'validate_germline(): good data failed')
        except ValidationError:
            self.assertTrue(False, 'validate_germline(): good data failed')

        # Bad data
        try:
            result = airr.validate_airr(self.germline_bad, debug=True)
            self.assertFalse(result, 'validate_germline(): bad data succeeded')
        except ValidationError:
            pass

    # @unittest.skip('-> load_genotype(): skipped\n')
    def test_read_genotype(self):
        # Good data
        try:
            result = airr.read_airr(self.genotype_good, validate=True, debug=True)
        except ValidationError:
            self.assertTrue(False, 'load_genotype(): good data failed')

        # Bad data
        try:
            result = airr.read_airr(self.genotype_bad, validate=True, debug=True)
            self.assertFalse(True, 'load_genotype(): bad data succeeded')
        except ValidationError:
            pass

    # @unittest.skip('-> validate_genotype(): skipped\n')
    def test_validate_genotype(self):
        # Good data
        try:
            result = airr.validate_airr(self.genotype_good, debug=True)
            self.assertTrue(result, 'validate_genotype(): good data failed')
        except ValidationError:
            self.assertTrue(False, 'validate_genotype(): good data failed')

        # Bad data
        try:
            result = airr.validate_airr(self.genotype_bad, debug=True)
            self.assertFalse(result, 'validate_genotype(): bad data succeeded')
        except ValidationError:
            pass

    # @unittest.skip('-> load_genotype(): skipped\n')
    def test_write_airr(self):
        # Good data
        try:
            repertoire_data = airr.read_airr(self.rep_good, validate=True, debug=True)
            germline_data = airr.read_airr(self.germline_good, validate=True, debug=True)
            genotype_data = airr.read_airr(self.genotype_good, validate=True, debug=True)

            # combine together and write
            obj = {}
            obj['Repertoire'] = repertoire_data['Repertoire']
            obj['GermlineSet'] = germline_data['GermlineSet']
            obj['GenotypeSet'] = genotype_data['GenotypeSet']
            airr.write_airr(self.output_good, obj, debug=True)

            # verify we can read it
            data = airr.read_airr(self.output_good, validate=True, debug=True)

            # is the data identical?
            del data['Info']
            if jsondiff.diff(obj, data) != {}:
                print('Output data does not match', file=sys.stderr)
                print(jsondiff.diff(obj, data), file=sys.stderr)
                self.assertTrue(False, 'write_airr_data(): Output data does not match')

        except Exception as inst:
            self.assertTrue(False, 'write_airr_data(): good data failed')
            print(type(inst))
            raise inst


if __name__ == '__main__':
    unittest.main()
