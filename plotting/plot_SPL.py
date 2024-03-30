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
from pyAcousticsAnalysis.calculations.tonal_components import calculate_loudness, find_tonal_components

cols = ['1/3 LZF 6,3', '1/3 LZF 8,0', '1/3 LZF 10,0', '1/3 LZF 12,5', '1/3 LZF 16,0', '1/3 LZF 20,0', '1/3 LZF 25,0', '1/3 LZF 31,5', '1/3 LZF 40,0', '1/3 LZF 50,0',
       '1/3 LZF 63,0', '1/3 LZF 80,0', '1/3 LZF 100', '1/3 LZF 125', '1/3 LZF 160', '1/3 LZF 200', '1/3 LZF 250', '1/3 LZF 315',
       '1/3 LZF 400', '1/3 LZF 500', '1/3 LZF 630', '1/3 LZF 800', '1/3 LZF 1000', '1/3 LZF 1250', '1/3 LZF 1600', '1/3 LZF 2000',
       '1/3 LZF 2500', '1/3 LZF 3150', '1/3 LZF 4000', '1/3 LZF 5000',
       '1/3 LZF 6300', '1/3 LZF 8000', '1/3 LZF 10000', '1/3 LZF 12500',
       '1/3 LZF 16000', '1/3 LZF 20000']


def plot_SPL(nome_misura, filename, df, plots_dir, show = True):
    
    mean_Leq = get_mean_levels(df, apply_masks=True)
    mean_Leq = mean_Leq[cols]
    mean_Leq.drop("avg_masked", inplace=True)
     
    fig1, ax1 = plt.subplots(figsize=(12, 5))

    plt.title(nome_misura + " - 1/3 SPL Spectrum Leq Lineare", fontsize=15)
    ax1.grid(True, color='black', linewidth=0.5)
    ax1.set_axisbelow(True)
    ax1.set_xlim(-1, 36) 

#    print("here", mean_Leq.min())
#    print("here2", mean_Leq.max(axis=0))    
#    print(mean_Leq)

    y_min = mean_Leq.min(axis=1)['avg_not_masked'] - 3
    y_max = mean_Leq.max(axis=1)['avg_not_masked'] + 3
    
#    print(y_min, y_max)
    
    ax1.set_ylim(y_min, y_max) 

    for ind_col, col in enumerate(mean_Leq.columns):
    #    color = 'green'

        ax1.bar(ind_col, mean_Leq[col], color= "#80FEFE", linewidth=2, edgecolor='#3030A3')

    ax1.set_xlabel("Hz", size=18)
    ax1.set_ylabel("dB", size=18)

    #plt.xticks(range(0, len(generate_freq_third_octaves())), [str(x) for x in generate_freq_third_octaves()], rotation=-35)  # Set text labels and properties.
    #xtick = ["8", "16", "31.5", "63", "125", "250", "500", "1K", "2K", "4K", "8K", "16K"]

    ax1.xaxis.set_tick_params(labelsize=14)
    ax1.yaxis.set_tick_params(labelsize=14)

    #ax1.minorticks_on()
    #ax1.tick_params(axis='x', which='minor', bottom=True)

    minor_locator = AutoMinorLocator(3)
    ax1.xaxis.set_minor_locator(minor_locator)

    plt.xticks(range(1, len(generate_freq_third_octaves()), 3), 
               ["8", "16", "31.5", "63", "125", "250", "500", "1K", "2K", "4K", "8K", "16K"])


    plt.savefig(os.path.join(plots_dir, filename[:-5] + "_SPL.png"), bbox_inches='tight', dpi=800)
    if show:
        plt.show()
        
    plt.close(fig1)

