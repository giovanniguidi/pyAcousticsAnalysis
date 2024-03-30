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


def plot_min_SPL(nome_misura, filename, df, plots_dir, show = True):
    
    min_Leq = get_min_levels(df, apply_masks=True)
    min_Leq = min_Leq[cols]
    min_Leq.drop("min_masked", inplace=True)
    
#    min_Leq[cols[13]] = 70

#    print(min_Leq)

    #genera curve isofoniche
    curve_isofoniche = generate_equal_loudness_contours()
    
    #creo la figura
    fig1, ax1 = plt.subplots(figsize=(12, 4))

    #min_y = min(SPL_1_3_min) - 5.
    #max_y = max(SPL_1_3_min) + 5.
#    min_y = 0
#    max_y = 50

    y_min = min_Leq.min(axis=1)['min_not_masked'] - 3
    y_max = min_Leq.max(axis=1)['min_not_masked'] + 3
    
#    freq = ['6,3', '8,0', '10,0', '12,5', '16,0', '20,0', '25,0', '31,5', '40,0', '50,0', '63,0', '80,0', '100', '125', '160', 
#        '200', '250', '315', '400', '500', '630', '800', '1000', '1250', '1600', '2000', '2500', '3150', '4000',
#        '5000', '6300', '8000', '10000', '12500', '16000', '20000']

    freq = [6.3, 8, 10.0, 12.5, 16.0, 20.0, 25.0, 31.5, 40.0, 50.0, 63.0, 80.0, 100, 125, 160, 
        200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000,
        5000, 6300, 8000, 10000, 12500, 16000, 20000]
    
#freq = [float(x.replace(",", ".")) for x in freq]
    
    #identifica le tonali            
    #ind_tonali = trova_componenti_tonali(freq, SPL_1_3_min, curve_isofoniche)

    #print(ind_tonali)

    #questi servono per disegnare gli assi cartesiani
    plt.title(nome_misura + " - 1/3 SPL Spectrum Min Lineare", fontsize=15)
    ax1.grid(True, color='black', linewidth=0.5)
    ax1.set_xlim(-1, 36) 
    ax1.set_ylim(y_min, y_max) 

    ax1.set_xlabel("Hz", size=18)
    ax1.set_ylabel("dB", size=18)
    ax1.set_axisbelow(True)

#plt.xticks(range(0, len(generate_freq_third_octaves())), [str(x) for x in generate_freq_third_octaves()], rotation=-35)  # Set text labels and properties.

#plt.savefig(os.path.join("output", filename.split(".")[0] + "_SPL_spectrum.jpg"))
#plt.show()        
        
        
#ax1.set_ylabel("dB", size=18)

#plt.xticks(list(freq_ticks.values()), list(freq_ticks.keys()), rotation=-50)  # Set text labels and properties.

#    print(curve_isofoniche)
        
    for ind, key in enumerate(curve_isofoniche.keys()):
        if key > 10:
            x_curva = []
            y_curva = []
            for ind, f in enumerate(freq):
#                print(f)
#                print(curve_isofoniche[key]['x'])
                if f in curve_isofoniche[key]['x']:
                    new_ind = curve_isofoniche[key]['x'].index(f)
                    x_curva.append(ind)
                    y_curva.append(curve_isofoniche[key]['y'][new_ind])
#                    print("here")
                    
#            print(x_curva, y_curva)
            ax1.plot(x_curva, y_curva, color='black', linestyle='solid', linewidth=1, label=None)
            text_ind = 18
            if y_curva[text_ind] < y_max and  y_curva[text_ind] > y_min:
                ax1.text(text_ind, y_curva[text_ind], key, fontsize=20)
                                
    L_N_max, ind_L_N_max, col_tonale = find_tonal_components(min_Leq)
        
    x_new = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]        
        
    freq, equal_loudness_contour = get_equal_loudness_contour_from_L_N(L_N_max)                
    ax1.plot(x_new, equal_loudness_contour, color='red', linestyle='dashed', linewidth=2)
#    print(x_curva)
#    freq = list(df_OBA.columns[1:])
#    freq = [float(x.replace(",", ".")) for x in freq]

    minor_locator = AutoMinorLocator(3)
    ax1.xaxis.set_minor_locator(minor_locator)

    plt.xticks(range(1, len(generate_freq_third_octaves()), 3), 
               ["8", "16", "31.5", "63", "125", "250", "500", "1K", "2K", "4K", "8K", "16K"])

    #plot min SPL
    for ind_col, col in enumerate(min_Leq.columns):        
        ax1.bar(ind_col, min_Leq[col], color= "#80FEFE", linewidth=2, edgecolor='#3030A3', zorder=10)

    if col_tonale:
        ax1.bar(ind_L_N_max, min_Leq[col_tonale], color= "#1309bd", linewidth=2,  zorder=10, label = "tonale")
        plt.legend(loc='best')
#    print(ind_L_N_max, col_tonale)

    
    #for ind_tonale in ind_tonali:    
    #    ax1.text(ind_tonale, SPL_1_3_min[ind_tonale] + 1, "tonale", fontsize=20)

    #plt.savefig(images_dir + "/grafico3.png")
    plt.savefig(os.path.join(plots_dir, filename[:-5] + "_SPL_min.png"), bbox_inches='tight', dpi=800)
    #plt.xticks(rotation = 45)
    if show:
        plt.show()

    plt.close(fig1)


def get_freq_x_ticks():
    
    print([str(x) for x in generate_freq_third_octaves()])
           
    freq_x_ticks = range(0, len(generate_freq_third_octaves())), [str(x) for x in generate_freq_third_octaves()]

    return freq_x_ticks
   