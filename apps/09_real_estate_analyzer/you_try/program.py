import os
import csv

def main():
	print_header()
	filename = get_data_file()
	data = load_file(filename)
	query_data(data)



def print_header():
	print('---------------------')
	print('REAL ESTATE APP')
	print('---------------------')
	print()


def get_data_file():
	base_folder = os.path.dirname(__file__)
	return os.path.join('.', 'data', 'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
    # with open(filename, 'r') as fin:
        reader = csv.DictReader(fin)
		for row in reader:
			print(type(row), row)
			print('Bed count: {}'.format(row['beds']))


def query_data(data):
	pass

if __name__ == '__main__':
	main()