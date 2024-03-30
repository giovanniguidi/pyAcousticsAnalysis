from pyAcousticsAnalysis.utils.helper_functions import get_mean_levels, get_min_levels, generate_freq_third_octaves, logarithmic_average
from datetime import timedelta 

def calculate_quantiles(df, channel = 'LAF', apply_masks=True):
    
    out_dict = {}

    if apply_masks:
#        print("applying mask")
        df = df[df['masked'] == False] 
    
    out_dict['-L1-'] = df['LAF'].quantile(q = .99)
    out_dict['-L5-'] = df['LAF'].quantile(q = .95)
    out_dict['-L10-'] = df['LAF'].quantile(q = .9)
    out_dict['-L50-'] = df['LAF'].quantile(q = .5)
    out_dict['-L90-'] = df['LAF'].quantile(q = .1)
    out_dict['-L95-'] = df['LAF'].quantile(q = .05)
    
    out_dict = {k: round(v, 1) for k, v in out_dict.items()}
        
    LAeq = logarithmic_average(df['LAeq'])
    out_dict['-LAeq-'] = LAeq
        
    return out_dict


def calculate_global_quantities(df, apply_masks=True):
    
    out_dict = {}
    
    if apply_masks:
#        print("applying mask")
        df_non_masked = df[df['masked'] == False] 
        df_masked = df[df['masked'] == True] 
    
        LAeq_non_masked = logarithmic_average(df_non_masked['LAeq'])
#        print(df_masked.shape)
        if len(df_masked) > 0: 
            LAeq_masked = logarithmic_average(df_masked['LAeq'])
        else:
            LAeq_masked = 0.
    else:
        LAeq_non_masked = logarithmic_average(df['LAeq'])
        LAeq_masked = 0.
            
    LAeq_tot = logarithmic_average(df['LAeq'])     

    sec_tot = round(df.shape[0] * 0.1)
    durata_tot = str(timedelta(seconds = sec_tot))        
    sec_non_masked = round(df_non_masked.shape[0] * 0.1)
    durata_non_masked = str(timedelta(seconds = sec_non_masked))        
    sec_masked = round(df_masked.shape[0] * 0.1)
    durata_masked = str(timedelta(seconds = sec_masked))        
        
    out_dict['-LAeq-'] = LAeq_non_masked
    out_dict["-LAeq!tot-"] = LAeq_tot
    out_dict["-LAeq!non!mask-"] = LAeq_non_masked
    out_dict["-LAeq!mask-"] = LAeq_masked
    out_dict["-durata!tot-"] = durata_tot
    out_dict["-durata!non!mask-"] = durata_non_masked
    out_dict["-durata!mask-"] = durata_masked
       
#    print("here", out_dict)
    
    return out_dict
