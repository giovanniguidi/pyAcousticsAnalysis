import pandas as pd
#import sys
#sys.path.append("C:\\Users\\giogu\\Documents\\Acustica\\python_routines")


from pyAcousticsAnalysis.instruments.commons import add_milliseconds

def read_LD_831_data(file_path):
        
#    data_dict = {}
    
    xl = pd.ExcelFile(file_path)
    sheet_names = xl.sheet_names

#    print(sheet_names)
    
    for sheet_name in sheet_names[:]:    
#        if sheet_name == "Sommario":
#            df = pd.read_excel(file_path, sheet_name=sheet_name)

 #           measure_name = df.loc[0, 'Unnamed: 1']
#            SLM_serial_number = df.loc[3, 'Unnamed: 1']
#            start_time = df.loc[12, 'Unnamed: 1']
#            end_time = df.loc[13, 'Unnamed: 1']
#            run_time = df.loc[14, 'Unnamed: 1']
           
#            data_dict['info'] = pd.DataFrame([[measure_name, SLM_serial_number, start_time, end_time, run_time]], 
#                                             columns=['measure_name', 'SLM_serial_number', 'start_time', 'end_time',
#                                                  'run_time'], index=['info'])
 

        if sheet_name == "Profilo storico":
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            df = add_milliseconds(df)
            df["masked"] = False
            
            list_to_remove = ['OVLD', 'ENTRAMBI OVLD', 'Marcatrice','Commenti', 
                 'Disco #', 'Tipo di registrazione']
            
            list_cols = [x for x in df.columns if x not in list_to_remove]            
            df = df[list_cols]
                
#            data_dict['time_history'] = df            
#            data_dict['globals'] = calculate_global_levels(df, apply_masks=True)
                   
#            df_freq_mask = create_frequency_mask(df)
#            print(df_freq_mask)
#            data_dict['frequency_mask'] = df_freq_mask
      
#    list_masks = []
#        if sheet_name == "Sommario":
#            df_somm = pd.read_excel(file_path, sheet_name=sheet_name)
#            print(df_somm)
    
    return df   #, df_somm   
