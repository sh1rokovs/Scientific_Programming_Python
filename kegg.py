def parse_gene_paths(table_text):
    table_el = []
    for el in table_text.split('\n'):
        table_el.append(el[:-1].split('\t'))

    result = {}
    for el in table_el:
        result[el[0]] = set()
        for elem in range(2, len(el)):
            if el[elem] == '': break
            result[el[0]].add(el[elem])

    return result


def count_paths_for_gene(gene_in_path, gene, path_part):
    quantity = 0

    for el in gene_in_path:
        if path_part in el.split('_'):
            if gene in gene_in_path[el]:
                quantity += 1

    return quantity


nw_str = ''
with open("kegg_hsa_gmt.txt", "r") as f:
    for line in f:
        nw_str += line
gene_in_path = parse_gene_paths(nw_str)
path_count = count_paths_for_gene(
    gene_in_path,
    'SDS',
    'metabolism'
)
print(path_count)
