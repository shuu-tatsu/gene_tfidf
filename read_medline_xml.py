'''
AbstractTextを抽出する
<AbstractText>
</AbstractText>
'''

from tqdm import tqdm
from bs4 import BeautifulSoup 
import os
import sys


def xml_parser(filename, abst_list):
    # BeautifulSoup
    xml = open(filename, "r", encoding="utf-8").read()
    soup = BeautifulSoup(xml, 'html.parser')

    for abst in tqdm(soup.find_all("abstracttext")):
        abst_list.append(abst.string)
    return abst_list


def load_abst(no):
    path = '/cl/work/shusuke-t/mori_lab_cluster/data/medline_2019/'
    #path = '/cl/work/shusuke-t/mori_lab_cluster/data/toy_medline_2019/'
    files = []
    abst_list = []

    for x in os.listdir(path):
        if os.path.isfile(path + x) and x[-4:] == '.xml':
            files.append(x)

    for filename in files:
        if int(filename[-8:-4]) == no:
            filename = path + filename
            abst_list = xml_parser(filename, abst_list)

    return abst_list


def main():
    no = int(sys.argv[1])
    path = '/cl/work/shusuke-t/mori_lab_cluster/data/extracted_data_2019_05_13/medline2019/'
    write_file = path + 'abst_' + str(no) + '.tsv'
    print('Loading...')
    abst_list = load_abst(no)
    print('Loading Done')
    print('Writing...')
    with open(write_file, 'w') as w:
        for index, abst in tqdm(enumerate(abst_list)):
            w.write(str(no) + '\t' + str(index) + '\t' + str(abst) + '\n')


if __name__ == '__main__':
    main()
