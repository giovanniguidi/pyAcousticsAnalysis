

def find_impulse_components(df):
    print("finding impulses")
    
    #time bin where to check for impulse components
    time_bin = 10
    
    time_bin_half = time_bin/2  #dividi a meta il time_bin per centrarlo sul valore che stai valutando
    impulsive = set()

    for ind, row in df[:].iterrows():
#        print(ind)
#        if not math.isnan (row['LAeq']):
        LAF = row['LAF']

        #misure nel range di un secondo
        df_1s = df.loc[ind - time_bin_half:ind + time_bin_half, ['LAeq', 'LAS', 'LAF', 'LAI', 'timestamp']]

        LAI_max = df_1s['LAI'].max()
        LAS_max = df_1s['LAS'].max()
        
#        print(df_1s)
        
        #misure nel range di 500ms prima e dopo
        df_500ms_before = df.loc[ind-time_bin_half:ind, ['LAeq', 'LAS', 'LAF', 'LAI','timestamp']]
        df_500ms_after = df.loc[ind:ind+time_bin_half, ['LAeq', 'LAS', 'LAF', 'LAI', 'timestamp']]

#        print("----")
#        print(df_500ms_before)
        
#        print("----")
#        print(df_500ms_after)

        LAF_min_before = df_500ms_before['LAF'].min()
        LAF_min_after = df_500ms_after['LAF'].min()

        LAI_max = df_1s['LAI'].max()
        LAS_max = df_1s['LAS'].max()

        if (LAF - LAF_min_before) > 10. and (LAF - LAF_min_after) > 10. and (LAI_max - LAS_max) > 6.:
            index_max = df_1s['LAF'].idxmax()
            impulsive.add(index_max)
    
    impulsive = sorted(list(impulsive))
        
    return impulsive