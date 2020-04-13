
from os.path import join
import pandas as pd
from py_deseq import py_DESeq2


if __name__ == '__main__':
    
    #dir_data = '../../module3_data'
    dir_data = '../results'
 
    design_matrix = pd.read_csv(join(dir_data, 'design_matrix.csv'))   
    count_matrix = pd.read_csv(join(dir_data, 'count_matrix.csv'))
    
    design_matrix.index = design_matrix['Cultivar']
    
    count_matrix = count_matrix.stack()
    count_matrix[ pd.isna(count_matrix) ] = 0
    count_matrix = count_matrix.unstack()
       
    dds = py_DESeq2(count_matrix,
               design_matrix,
               design_formula = '~ sample',
               gene_column = 'gene') # <- telling DESeq2 this should be the gene ID column

    dds.run_deseq() 
    dds.get_deseq_result()
    res = dds.deseq_result 
    res.head()
    
    
