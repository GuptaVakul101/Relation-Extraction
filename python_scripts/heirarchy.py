import sys
import csv
dloc_file = "./../relation_mapping/dbLocation_v1.1.csv"
dorg_file = "./../relation_mapping/dbOrganization_v1.1.csv"
dper_file = "./../relation_mapping/dbPerson_v1.1.csv"
wloc_file = "./../relation_mapping/wikidataLocation_v1.1.csv"
worg_file = "./../relation_mapping/wikidataOrganization_v1.1.csv"
wper_file = "./../relation_mapping/wikidataPerson_v1.1.csv"

def generate_dictionary(filename):
    dct = dict()
    with open(filename) as infile:
        reader = csv.reader(infile,delimiter='.')
        for rows in reader:
            # print(rows)
            rows[len(rows)-1]=rows[len(rows)-1][0:-1]
            # print(rows)
            for i in range(2,len(rows)):
                children=[]
                for j in range(i,len(rows)):
                    children.append(rows[j])
                # print(rows[i])
                # print(children)
                if not rows[i] in dct:
                    dct[rows[i]]=children
                else:
                    for item in children:
                        dct[rows[i]].append(item)
                # print(list(set(dct[rows[i]]))
                # print(rows[i])
                # print(dct[rows[i]])
                dct[rows[i]] = list(set(dct[rows[i]]))
                # dct[rows[i]]=dct[rows[i]].distinct()
    return dct

def write_dictionaries(dict,outfile):
    with open(outfile, 'w+') as outfile:
        writecsv = csv.writer(outfile, delimiter=',')
        for key, val in dict.items():
            list = []
            list.append(key)
            for item in val:
                list.append(item)
            writecsv.writerow(list)

if __name__ == '__main__':
    dper = generate_dictionary(dper_file)
    dloc = generate_dictionary(dloc_file)
    dorg = generate_dictionary(dorg_file)
    wper = generate_dictionary(wper_file)
    wloc = generate_dictionary(wloc_file)
    worg = generate_dictionary(worg_file)
    write_dictionaries(dper,"./../heirarchy_mapping/dper_heirarchy.csv")
    write_dictionaries(dloc,"./../heirarchy_mapping/dloc_heirarchy.csv")
    write_dictionaries(dorg,"./../heirarchy_mapping/dorg_heirarchy.csv")
    write_dictionaries(wper,"./../heirarchy_mapping/wper_heirarchy.csv")
    write_dictionaries(wloc,"./../heirarchy_mapping/wloc_heirarchy.csv")
    write_dictionaries(worg,"./../heirarchy_mapping/worg_heirarchy.csv")
