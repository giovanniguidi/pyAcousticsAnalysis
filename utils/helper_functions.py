import numpy as np
import pandas as pd


def get_mean_levels(df, apply_masks=True):
 
    cols = [x for x in df.columns if (x.startswith("L") or x.startswith("1/3")) and not (x.endswith("min") or x.endswith("max"))]
    
    out_dict = {}
    
#    df_out = pd.DataFrame()
    
    if apply_masks:
        df_not_masked = df[df['masked'] == False]#.copy()        
        df_masked = df[df['masked'] == True]#.copy()    
        
        df_not_masked = np.expand_dims(df_not_masked[cols].apply(lambda x: logarithmic_average(x)).values, axis=0)        
        df_not_masked = pd.DataFrame(df_not_masked, columns=cols, index=['avg_not_masked'])
        
        if len(df_masked) > 0:
            df_masked = np.expand_dims(df_masked[cols].apply(lambda x: logarithmic_average(x)).values, axis=0)        
            df_masked = pd.DataFrame(df_masked, columns=cols, index=['avg_masked'])
        else:
            df_masked = pd.DataFrame(np.zeros((1, len(cols))), columns=cols, index=['avg_masked'])
                    
        df_out = pd.concat([df_not_masked, df_masked])
    
    else:
        df_out = np.expand_dims(df[cols].apply(lambda x: logarithmic_average(x)).values, axis=0)        
        df_out = pd.DataFrame(df_out, columns=cols, index=['avg'])
        
    return df_out

def get_min_levels(df, apply_masks=True):
 
    cols = [x for x in df.columns if (x.startswith("L") or x.startswith("1/3")) and not (x.endswith("min") or x.endswith("max"))]
    
#    out_dict = {}
    
    df_out = pd.DataFrame()
    
    if apply_masks:
        df_not_masked = df[df['masked'] == False]#.copy()        
        df_masked = df[df['masked'] == True]#.copy()    
        
        df_not_masked = np.expand_dims(df_not_masked[cols].apply(lambda x: np.min(x)).values, axis=0)   
        df_not_masked = pd.DataFrame(df_not_masked, columns=cols, index=['min_not_masked'])
                
        if len(df_masked) > 0:
            df_masked = np.expand_dims(df_masked[cols].apply(lambda x: np.min(x)).values, axis=0)        
            df_masked = pd.DataFrame(df_masked, columns=cols, index=['min_masked'])
        else:
            df_masked = pd.DataFrame(np.zeros((1, len(cols))), columns=cols, index=['min_masked'])
                    
        df_out = pd.concat([df_not_masked, df_masked])
    
    else:
        df_out = np.expand_dims(df[cols].apply(lambda x: np.min(x)).values, axis=0)        
        df_out = pd.DataFrame(df_out, columns=cols, index=['min'])
        
    return df_out


def logarithmic_average(*args, octave=False):
#    print(args)

    levels = np.array(args)
#    print(livelli)
 
#    print(octave)
    L_p_tot = 10. * np.log10(np.mean(np.power(10., levels * 0.1), axis=0))

    if octave == False:
        L_p_tot = 10. * np.log10(np.mean(np.power(10., L_p_tot * 0.1)))
    
    
    return round(L_p_tot, 1)



def generate_freq_third_octaves(freq_min=0, freq_max = 20000.):
    """
    Funzione per generare le frequenze in bande di terzi d'ottava
    """
    
    all_freq_one_third_octave = np.array([6.3, 8, 10., 12.5, 16., 20., 25., 31.5, 40., 50., 63., 80., 100., 125., 
                                          160., 200., 250., 315., 400., 500., 630., 800., 1000., 1250., 1600., 2000., 
                                          2500., 3150., 4000., 5000., 6300., 8000., 10000., 12500., 16000., 20000.])

    freq_one_third_octave = all_freq_one_third_octave[(all_freq_one_third_octave >= freq_min) & (all_freq_one_third_octave <= freq_max)]
    
    
    return freq_one_third_octave