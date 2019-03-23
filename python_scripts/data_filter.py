import sys
import csv
dper_file = "./../relation_mapping/dbpediaCanonicalPerson.csv"
dloc_file = "./../relation_mapping/dbpediaCanonicalLocation.csv"
dorg_file = "./../relation_mapping/dbpediaCanonicalOrganization.csv"
wper_file = "./../relation_mapping/wikidataCanonicalPerson.csv"
wloc_file = "./../relation_mapping/wikidataCanonicalLocation.csv"
worg_file = "./../relation_mapping/wikidataCanonicalOrganization.csv"

def generate_dictionary(filename):
	dct = dict()
	with open(filename) as infile:
		reader = csv.reader(infile)
		dct = {rows[0] : rows[1] for rows in reader}
		return dct
def fetch_dictionaries():
	dper = generate_dictionary(dper_file)
	print(len(dper.keys()))
	dloc = generate_dictionary(dloc_file)
	print(len(dloc.keys()))
	dorg = generate_dictionary(dorg_file)
	print(len(dorg.keys()))
	wper = generate_dictionary(wper_file)
	print(len(wper.keys()))
	wloc = generate_dictionary(wloc_file)
	print(len(wloc.keys()))
	worg = generate_dictionary(worg_file)
	print(len(worg.keys()))

	return dper, dloc, dorg, wper, wloc, worg

inp_file = sys.argv[1]
out_file = sys.argv[2]

if __name__ == '__main__':
	dper, dloc, dorg, wper, wloc, worg = fetch_dictionaries()

	if 'dtuples' in inp_file:
		f_code = 'd'
	elif 'wtuples' in inp_file:
		f_code = 'w'

	with open(out_file, 'w+') as outfile:
		writecsv = csv.writer(outfile, delimiter='\t')
		if f_code == 'd':
			with open(inp_file) as infile:
				readcsv = csv.reader(infile, delimiter=' ')
				for row in readcsv:
					if row[1] == 'Person' and row[6] in dper.keys():
						writecsv.writerow([row[0], row[1], row[3], row[4], dper[row[6]]])
					elif row[1] == 'Organisation' and row[6] in dorg.keys():
						writecsv.writerow([row[0], 'Organization', row[3], row[4], dorg[row[6]]])
					elif row[1] == 'Place' and row[6] in dloc.keys():
						writecsv.writerow([row[0], 'Location', row[3], row[4], dloc[row[6]]])
		elif f_code == 'w':
			with open(inp_file) as infile:
				readcsv = csv.reader(infile, delimiter='\t')
				for row in readcsv:
					if row[1] == 'Person' and row[2] in wper.keys():
						writecsv.writerow([row[0], row[1], row[3], row[4], wper[row[2]]])
					elif row[1] == 'Organisation' and row[2] in worg.keys():
						writecsv.writerow([row[0], 'Organization', row[3], row[4], worg[row[2]]])
					elif row[1] == 'Place' and row[2] in wloc.keys():
						writecsv.writerow([row[0], 'Location', row[3], row[4], wloc[row[2]]])
