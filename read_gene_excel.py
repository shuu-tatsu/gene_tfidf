import pandas as pd

def load_gene(path):
    filename = path + 'epsilon2_GIgenes6_DTU190308_LB_genome_dip_normed3_clust1000_geneinfo_cp.xlsx'
    sheet_name = 'epsilon2_GIgenes6_DTU190308_LB_'

    book = pd.read_excel(filename, sheet_name=sheet_name)

    # [[no_cluster, b_no, gene_name], [], ..., []]
    gene_list = book.iloc[:,1:4].values.tolist()
    return gene_list


def main():
    path = '/cl/work/shusuke-t/mori_lab_cluster/data/'
    write_file = path + 'extracted_data_2019_05_13/gene/gene.tsv'
    gene_list = load_gene(path)

    '''
    name_list = [name[2] for name in gene_list if not name[2] == 'Noinfo_in_table']
    print(len(name_list))
    print(len(set(name_list))) 
    '''

    with open(write_file, 'w') as w:
        for gene in gene_list:
            cluster = str(gene[0])
            name = str(gene[2])
            if not name == 'Noinfo_in_table':
                w.write(cluster + '\t' + name + '\n')


if __name__ == '__main__':
    main()
