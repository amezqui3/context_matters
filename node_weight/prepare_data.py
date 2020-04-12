
from os.path import join
import pandas as pd
import numpy as np


if __name__ == '__main__':
    
    dir_data = '../../module3_data'
    f_key = join(dir_data, 'obs_2018_key.csv')
    f_pheno = join(dir_data, '2018_ground_data_mean_purpleness.csv')
    
    df_key = pd.read_csv(f_key)
    df_pheno = pd.read_csv(f_pheno)
        
    
    df_pheno = df_pheno[ pd.notna(df_pheno['AnthesisDate']) ]
    
    t_num_list = []
    for date in df_pheno['AnthesisDate']:
        t = date.split('/')
        t_num_list.append( int( t[0] ) * 30 + int( t[1] ) )
        
    
    dic_plot2time = dict( zip(df_pheno['plot'], t_num_list) )
    
        
    dic_cultivar2plot = {}    
    for i, c in enumerate(df_key['Genotype']):
        if c not in dic_cultivar2plot:
            dic_cultivar2plot[c] = []
        dic_cultivar2plot[c].append( df_key['Plot'][i] )
        
    
    dic_cultivar2time = {}
    for c in dic_cultivar2plot:
        t_ave = 0
        n_plt = 0
        for p in dic_cultivar2plot[c]:
            if p in dic_plot2time:
                n_plt += 1
                t_ave += dic_plot2time[p]
       
        if n_plt >= 1:
            t_ave = t_ave / n_plt
            dic_cultivar2time[c] = t_ave
            
    
    thres = 0.05
    
    t_num_sort_list = np.sort(t_num_list)
    n_element = len(t_num_list)
    
    low = t_num_sort_list[round(thres * n_element)]
    high = t_num_sort_list[round( (1 - thres) * n_element )]
    
       
    cultivar_list = []
    treatment_list = []
    
    for c in dic_cultivar2time:
        if dic_cultivar2time[c] < low:
            cultivar_list.append(c)
            treatment_list.append('A')
        elif dic_cultivar2time[c] > high:
            cultivar_list.append(c)
            treatment_list.append('B')
            
   
    
    f_expression = join(dir_data, '942_FPKM_B73_genes_w_feature.txt')   
    df_expression = df_map=pd.read_csv(f_expression, sep='\t')
    
    
    cultivar_list_reduced = [c for c in cultivar_list if c in df_expression.columns]    
    
    df_expression = df_expression[['gene'] + cultivar_list_reduced ]
    df_expression = df_expression.set_index(df_expression.columns[0])
    df_expression.to_csv(join(dir_data,'count_matrix.csv'), encoding='utf-8', index=True)
          
    treatment_list_reduced = []
    for i, c in enumerate(cultivar_list):
        if c in cultivar_list_reduced:
            treatment_list_reduced.append(treatment_list[i])
            
                
    design_matrix = pd.DataFrame({
     'Cultivar'  : cultivar_list_reduced,
     'treatment' : treatment_list_reduced,
    })

    design_matrix = design_matrix.set_index(design_matrix.columns[0])    
    design_matrix.to_csv(join(dir_data,'design_matrix.csv'), encoding='utf-8', index=True)
    
    
    
    
    
 
        