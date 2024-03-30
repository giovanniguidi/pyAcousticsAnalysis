import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import os
#import pickle
import numpy as np
from datetime import timedelta
#import sys
#project_folder = "C:\\Users\\giogu\\Documents\\Acustica\\python_routines" 
#sys.path.append(project_folder)

from pyAcousticsAnalysis.utils.helper_functions import generate_freq_third_octaves
from pyAcousticsAnalysis.utils.helper_functions import get_mean_levels, get_min_levels, generate_freq_third_octaves, logarithmic_average
from pyAcousticsAnalysis.utils.curves import generate_equal_loudness_contours, get_equal_loudness_contour_from_L_N
from pyAcousticsAnalysis.instruments.commons import read_preprocessed_data, get_masks
#from pyAcousticsAnalysis.calculations.tonal_components import calculate_loudness, find_tonal_components
from pyAcousticsAnalysis.calculations.impulse_components import find_impulse_components

cols = ['1/3 LZF 6,3', '1/3 LZF 8,0', '1/3 LZF 10,0', '1/3 LZF 12,5', '1/3 LZF 16,0', '1/3 LZF 20,0', '1/3 LZF 25,0', '1/3 LZF 31,5', '1/3 LZF 40,0', '1/3 LZF 50,0',
       '1/3 LZF 63,0', '1/3 LZF 80,0', '1/3 LZF 100', '1/3 LZF 125', '1/3 LZF 160', '1/3 LZF 200', '1/3 LZF 250', '1/3 LZF 315',
       '1/3 LZF 400', '1/3 LZF 500', '1/3 LZF 630', '1/3 LZF 800', '1/3 LZF 1000', '1/3 LZF 1250', '1/3 LZF 1600', '1/3 LZF 2000',
       '1/3 LZF 2500', '1/3 LZF 3150', '1/3 LZF 4000', '1/3 LZF 5000',
       '1/3 LZF 6300', '1/3 LZF 8000', '1/3 LZF 10000', '1/3 LZF 12500',
       '1/3 LZF 16000', '1/3 LZF 20000']

    
def plot_time_history(nome_misura, filename, df, plots_dir, find_impulses = True, show = False):
    
#    t = df['Tempo']
#    timestamp = df['timestamp']

    t = df['timestamp']
#    timestamp = df['timestamp']
    
    LAF = df['LAF']
#    LAeq = df['LAeq']
#    runnig_LEq = df['LAF'].expanding().mean() 

#    def new_func(x):
#        res = np.power(10., x * 0.1)        
#        return res
    
    #calculate running Leq
    df['LAF_pow'] = np.power(10., df['LAF'] * 0.1)#.apply(new_func)
    runnig_LEq = df['LAF_pow'].expanding().mean() 
    runnig_LEq = 10 *  np.log10(runnig_LEq)    
    df.drop(columns=['LAF_pow'], inplace=True)
    
    fig1, ax1 = plt.subplots(figsize=(12, 3))

    plt.title(nome_misura + " - Time history", fontsize=15)
    ax1.grid(True)

    ax1.plot(t, LAF, label = 'LAF')
    #ax1.plot(t, LAeq, label = 'LAeq')
    ax1.plot(t, runnig_LEq, label = 'LAF - Running Leq')

#    y_min = mean_Leq.min(axis=1)['avg_not_masked'] - 3
#    y_max = mean_Leq.max(axis=1)['avg_not_masked'] + 3
    y_min = LAF.min() - 3
    y_max = LAF.max() + 3
    
    ax1.set_xlim(-30, max(t) + 30) 
    ax1.set_ylim(y_min, y_max) 

    #for ind_col, col in enumerate(mean_Leq.columns):
    #    color = 'green'
    #    ax1.bar(ind_col, mean_Leq[col], color= "blue", linewidth=2, edgecolor='black')

    df['x_ticks'] = df['timestamp'].apply(lambda x: str(timedelta(seconds = x)))
    
#    ax1.yaxis.set_tick_params(labelsize=14)
    ticks_interval = 1800    
    plt.xticks(df.iloc[::ticks_interval]['timestamp'], df.iloc[::ticks_interval]['x_ticks'])
      
    df.drop(columns=['x_ticks'], inplace=True)
    
    ax1.set_xlabel("h:m:s", size=18)
    ax1.set_ylabel("dBA", size=18)

    list_masks = get_masks(df)
#    print(list_masks) 
    
    L_min = y_min + 1
    L_max = y_max - 1
    
    for mask in list_masks:
        ax1.plot([mask[0], mask[1]], [L_max, L_max], linewidth=1, color='black')    
        ax1.plot([mask[0], mask[1]], [L_min, L_min], linewidth=1, color='black')    
        ax1.plot([mask[0], mask[0]], [L_min, L_max], linewidth=1, color='black')    
        ax1.plot([mask[1], mask[1]], [L_min, L_max], linewidth=1, color='black')    
        
    #impulsive components    
    if find_impulses: 
        list_impulses = find_impulse_components(df)
        print(list_impulses)
            
#    delta = 1
#    for impulse in list_impulses[0:1]:
#        print(impulse)
#        ax1.plot([impulse - delta, impulse + delta], [L_max, L_max], linewidth=1, color='red')    
#        ax1.plot([impulse - delta, impulse + delta], [L_min, L_min], linewidth=1, color='red')    
#        ax1.plot([impulse - delta, impulse - delta], [L_min, L_max], linewidth=1, color='red')    
#        ax1.plot([impulse - delta, impulse + delta], [L_min, L_max], linewidth=1, color='red')    
        
        
    #plt.xticks(range(0, len(generate_freq_third_octaves())), [str(x) for x in generate_freq_third_octaves()], rotation=-35)  # Set text labels and properties.
    plt.legend(loc='upper right')

    plt.savefig(os.path.join(plots_dir, filename[:-5] + "_time_history.png"), bbox_inches='tight', dpi=800)

    if show:
        plt.show()
        
    plt.close(fig1)

def get_freq_x_ticks():
    
    print([str(x) for x in generate_freq_third_octaves()])
           
    freq_x_ticks = range(0, len(generate_freq_third_octaves())), [str(x) for x in generate_freq_third_octaves()]

    return freq_x_ticks
   