
from os.path import join
import pandas as pd
import numpy as np


if __name__ == '__main__':
    dir_data = '../../module3_data'
    dir_result = '../results'
    f_eqtl = join(dir_data, 'eQTL_final.csv')
    f_snp = join(dir_data, 'tpj13174-sup-0016-datas6.xls')
    
    df_eqtl = pd.read_csv(f_eqtl)
    df_snp = pd.read_excel(f_snp)
        
    label = np.zeros(len(df_eqtl))
    
    df_eqtl['label'] = label
       
    for i in range( len(df_snp) -2 ):
        snp_flower = df_snp.iloc[i+1,2].split('_')
        n_chrom = int( snp_flower[0][1:] )
        if snp_flower[1][-1] == '*':
            snp_flower[1] = snp_flower[1][:-1] 
        pos = int(snp_flower[1])
        
        msk = ( df_eqtl['snps'] == pos ) & ( df_eqtl['chrom'] == n_chrom )
              
        if msk.sum() > 0:
            df_eqtl['label'][msk] = 1
        
        
    df_eqtl.to_csv(join(dir_result, 'eQTL_label.csv'), encoding='utf-8', index=False)
        
        
        
        
        
        