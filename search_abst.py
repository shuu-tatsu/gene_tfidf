import re


class Cluster:

    def __init__(self, cluster_no):
        self.cluster_no = cluster_no

        #クラスターに含まれるgeneのリスト
        self.gene_name_list = []
        #クラスターのabst set
        self.cluster_abst_id_list = []

    def add(self, gene_name, gene_abst_id_list):
        self.gene_name_list.append(gene_name)
        self.cluster_abst_id_list.extend(gene_abst_id_list)
        self.cluster_abst_id_list = list(set(self.cluster_abst_id_list))

    def get_context(self):
        self.context_words_list = []
        for abst in self.cluster_abst_id_list:
            self.context_words_list.extend(re.split('[-+() ,./]', abst[2]))

    def show(self):
        print('#')
        print('cluster_no:{}'.format(self.cluster_no))
        print('cluster_context:{}'.format(self.context_words_list))
        #print('gene_name_set:{}'.format(self.gene_name_list))
        #for abst in self.cluster_abst_id_list:
        #    print(abst[2])
        #    print('')


def load(f):
    with open(f, 'r') as r:
        load_list = [abst for abst in r]
    return load_list


def search_abst(gene_name, abst_list):
    abst_id_list = []
    for abst_info in abst_list:
        splited = abst_info.split('\t')
        file_no = splited[0].strip()
        abst_no = splited[1].strip()
        abst_text = splited[2].strip()
        if gene_name in abst_text.split(' '):
            abst_id = (file_no, abst_no, abst_text)
            abst_id_list.append(abst_id)
    return abst_id_list


def main():
    # File load
    #abst_file = '/cl/work/shusuke-t/mori_lab_cluster/data/extracted_data_2019_05_13/medline2019/abst_total.tsv'
    abst_file = '/cl/work/shusuke-t/mori_lab_cluster/data/extracted_data_2019_05_13/medline2019/abst_total_toy.tsv'
    #gene_file = '/cl/work/shusuke-t/mori_lab_cluster/data/extracted_data_2019_05_13/gene/gene.tsv'
    gene_file = '/cl/work/shusuke-t/mori_lab_cluster/data/extracted_data_2019_05_13/gene/gene_toy.tsv'
    abst_list = load(abst_file)
    gene_list = load(gene_file)

    # key: cluster_no, value: Cluster instance
    gene_dict = {}

    for gene in gene_list:
        splited = gene.split('\t')
        cluster_no = splited[0].strip()
        gene_name = splited[1].strip()
        abst_id_list = search_abst(gene_name, abst_list)
        if cluster_no in gene_dict.keys():
            temp_cls = gene_dict[cluster_no]
        else:
            temp_cls = Cluster(cluster_no)
        temp_cls.add(gene_name, abst_id_list)
        gene_dict[cluster_no] = temp_cls

    # get cluster context
    for dic_key in gene_dict.keys():
        gene_dict[dic_key].get_context()

    # show
    for dic_key in gene_dict.keys():
        gene_dict[dic_key].show()


if __name__ == '__main__':
    main()
