from datetime import datetime, timedelta
import pandas as pd
import numpy as np

def add_milliseconds(df):
                
    #togli gli eventi accensione/spegnimento        
    df = df[df['Tipo di registrazione'].isna()].reset_index(drop=True)   

    #trova il time_delta tra le misure
    num_values_per_second = df['Tempo'].value_counts().max()        
    time_delta = 1000./num_values_per_second
    
#    print(num_values_per_second)
    numero_bin = int(1000./time_delta)
#    print(numero_bin)
        
    out_list = []

    num_millisec = 0

    #la misura non inizia mai da 0
    id_tempo_iniziale = df.index[0]
    
    tempo_iniziale = df.loc[id_tempo_iniziale, 'Tempo']

    id_tempo_finale = df[df['Tempo'] > tempo_iniziale].index[0]    
    diff = id_tempo_finale - id_tempo_iniziale
    
#    print(id_tempo_finale, diff)
    
    num_millisec += (numero_bin - diff - 1)
    num_millisec = int(num_millisec)
        
    for ind, row in df.iterrows():
        if (ind - diff ) % numero_bin == 0:
            num_millisec = 0
        else:
            num_millisec += 1

        out_list.append(row['Tempo'] + timedelta(milliseconds = num_millisec * time_delta))
        
    df['Tempo'] = out_list

    #aggiungi timestamp
    timestamp = df['Tempo'].apply(pd.Timestamp.timestamp)
        
    df['timestamp'] = timestamp - timestamp.iloc[0]        
        
    return df




def get_masks(df): 

    list_indices = list(df[df['masked'] == True].index)
        
    list_ind_min = []
    list_ind_max = []
    dummy_list = []

    for ind in range(0, len(list_indices)):
        if ind < len(list_indices)-1:
            if (list_indices[ind+1] - list_indices[ind]) == 1:
                dummy_list.append(list_indices[ind])
            else:     
                list_ind_min.append(np.min(dummy_list))
                dummy_list = []
                list_ind_max.append(list_indices[ind])

        elif ind == len(list_indices)-1:
            list_ind_min.append(np.min(dummy_list))
            list_ind_max.append(list_indices[ind])        

    list_masks = []
        
    for ind in range(0, len(list_ind_min)):
        list_masks.append((round(df.loc[list_ind_min[ind]]['timestamp'], 1), round(df.loc[list_ind_max[ind]]['timestamp'], 1)))
    
    return list_masks



def is_masked(timestamp, list_masks):    
    """
    Funzione per verificare se un timestamp è
    dentro gli intervalli di mascheramento    
    """
    list_masks = np.asarray(list_masks)
    
    masked = False
    
    if len(list_masks) > 0:
        res = (timestamp > list_masks[:, 0]) & (timestamp < list_masks[:, 1])

        if True in res:
            masked = True
    
    return masked


def add_masks_to_df(list_masks, df):
    df['masked'] = df['timestamp'].apply(lambda x: is_masked(x, list_masks))

    
def read_preprocessed_data(file_path):
    
    df = pd.read_excel(file_path, index_col=0)
    
    return df
