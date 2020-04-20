
from os.path import join
import pandas as pd
import numpy as np


if __name__ == '__main__':
    dir_data = '../../module3_data'
    dir_result = '../results'
    f_eqtl = join(dir_data, 'eqtl_related_100.csv')
    f_snp = join(dir_data, 'tpj13174-sup-0016-datas6.xls')
    f_snp2 = join(dir_data, 'pone.0071377.s004.xls')
    
    df_eqtl = pd.read_csv(f_eqtl)
    df_snp = pd.read_excel(f_snp)
    df_snp2 = pd.read_excel(f_snp2)
        
    label = np.zeros(len(df_eqtl))
    
    df_eqtl['label'] = label
    
    chrom_snp_list = []
    
    for i in range( len(df_snp) -2 ):
        snp_flower = df_snp.iloc[i+1,2].split('_')
        n_chrom = snp_flower[0][1:]
        if snp_flower[1][-1] == '*':
            snp_flower[1] = snp_flower[1][:-1] 
        pos = snp_flower[1]
        chrom_snp_list.append( (n_chrom, pos) )
        
    for i in range(181):
        n_chrom = str( int( df_snp2.iloc[i,2] ) )
        snp_flower = str( int( df_snp2.iloc[i,3] ) )
        chrom_snp_list.append( (n_chrom, pos) )
        
    
    for chrom, pos in chrom_snp_list:
        s = 'rs' + chrom + '_' + pos
        msk = ( df_eqtl['SNP_ID'] == 'rs' + chrom + '_' + pos)    
          
        if msk.sum() > 0:
            df_eqtl['label'][msk] = 1

    
    print(df_eqtl['label'].sum())

    #df_eqtl.to_csv(join(dir_result, 'eqtl_related_100_label.csv'), encoding='utf-8', index=False)
        
        
        
        
        
        