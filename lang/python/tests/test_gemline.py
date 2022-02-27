import airr

try:
    data = airr.load_germline_set('data/bad_germline_set.json')
    airr.validate_germline_set(data)
except airr.ValidationError:
    print('The format of the germline set is invalid')

try:
    data = airr.load_genotype_set('data/bad_genotype_set.json')
    airr.validate_genotype_set(data)
except airr.ValidationError:
    print('The format of the genotype set is invalid')


