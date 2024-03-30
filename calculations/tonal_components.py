import numpy as np

def find_tonal_components(min_Leq):

#    col_tonale = None

#    print(min_Leq.shape)
    cols = list(min_Leq)
#    print(cols)
    
    #    L_N = 42
    loudness_list = []
    for ind_col, column in enumerate(min_Leq):
#        print(column)
#        print(ind_col, column)
        freq = float(column.split(" ")[-1].replace(",", "."))
        SPL = min_Leq[column].values[0]
#        print(SPL)
        loudness = calculate_loudness(freq, SPL)
        loudness_list.append(loudness)
        
#    print(loudness_list)
    loudness_list = np.array(loudness_list)# if x is not None])
#    print(loudness_list.shape)
    L_N_max = np.max(loudness_list)
    ind_L_N_max = np.argmax(loudness_list)

    
#    print(cols[ind_L_N_max])
#    print(L_N)
    
#    min_Leq[
#    print(min_Leq['1/3 LZF 250'])
    
#    min_Leq['1/3 LZF 250'] = 50
    
    min_Leq_list = min_Leq.values[0]
#    print(min_Leq_list)
    
    if ind_L_N_max > 0 and ind_L_N_max < len(min_Leq_list) - 1:
#            print(ind)
#        freq_1_3 = freq[ind]
        SPL = min_Leq_list[ind_L_N_max]
        SPL_prev = min_Leq_list[ind_L_N_max - 1]
        SPL_post = min_Leq_list[ind_L_N_max + 1]
        
        if ((SPL - SPL_prev) > 5.) and ((SPL - SPL_post) > 5.):
#            print("tonale")
            col_tonale = cols[ind_L_N_max]
        else:
#            print("non tonale")
            col_tonale = None
    
#    print(L_N_max, ind_L_N_max)
        
    return L_N_max, ind_L_N_max, col_tonale


def calculate_loudness(freq, SPL):
    
    all_freq = [20., 25., 31.5, 40., 50., 63., 80., 100., 125.,
                160., 200., 250., 315., 400., 500., 630, 800.,
                1000., 1250., 1600., 2000., 2500., 3150, 
                4000., 5000., 6300., 8000., 10000., 12500
                ]
    
    a_f = np.array([2.347, 2.190, 2.050, 1.879, 1.724, 1.597,
                   1.512, 1.466, 1.426, 1.394, 1.372, 1.344, 1.304,
                    1.256, 1.203, 1.135, 1.062, 1, 0.967, 0.943, 0.932,
                    0.933, 0.937, 0.952, 0.974, 1.027, 1.135, 1.266, 1.501
               ])
    
    b_f = np.array([0.00561, 0.00527, 0.00481, 0.00404, 0.00338,
                    0.00286, 0.00259, 0.00257, 0.00256, 0.00255,
                    0.00254, 0.00248, 0.00229, 0.00201, 0.00162,
                    0.00111, 0.00052, 0., -0.00039, -0.00067, -0.00092,
                    -0.00105, -0.00104, -0.00088, -0.00055, 0., 0.00089,
                    0.00211, 0.00488
                ])
    
    T_f = np.array([74.3, 65., 56.3, 48.4, 41.7, 35.5, 29.8, 25.1,
                    20.7, 16.8, 13.8, 11.2, 8.9, 7.2, 6., 5., 4.4, 4.2,
                    3.7, 2.6, 1., -1.2, -3.6, -3.9, -1.1, 6.6, 15.3,
                    16.4, 11.6    
                ])
    
    if freq in all_freq:
#        print(freq)
        ind = all_freq.index(freq)
        loudness = 4.2 + ((a_f[ind] * (SPL - T_f[ind]))/(1. + (b_f[ind] * (SPL - T_f[ind]))))

    else:
        loudness = -9999.
        
    return loudness

def find_tonal_components_old(freq, SPL_1_3_min, curve_isofoniche):
    
    loudness_list = trova_loudness(curve_isofoniche, freq, SPL_1_3_min)
    
#    print(loudness_list)
    
    ind_tonali = []
    
    for ind in range(0, len(SPL_1_3_min)):
#    for ind in range(9, 10):
    
        #verifica che non sei agli estremi dello spettro
        if ind > 0 and ind < len(SPL_1_3_min) - 1:
#            print(ind)

            freq_1_3 = freq[ind]
            SPL = SPL_1_3_min[ind]
            SPL_prev = SPL_1_3_min[ind-1]
            SPL_post = SPL_1_3_min[ind+1]
            loudness = loudness_list[ind]
            
#            print(freq_1_3)
    #        print(SPL_post)
    #        print(SPL)

            if ((SPL - SPL_prev) > 5.) and ((SPL - SPL_post) > 5.) and loudness >= max(loudness_list):
#                print("tonale")
                ind_tonali.append(ind)
                
    return ind_tonali



def trova_loudness(curve_isofoniche, freq, SPL_1_3_min):

    list_loudness = []
    
#    for ind in range(10, 16):
    for ind in range(0, len(SPL_1_3_min)):        
        freq_1_3 = freq[ind]
        SPL = SPL_1_3_min[ind]
            
#        print(freq_1_3, SPL)
        loudness = 0
    
        for key in curve_isofoniche.keys():
#            print(key)
            if freq_1_3 in curve_isofoniche[key]['x']:
                index = curve_isofoniche[key]['x'].index(freq_1_3)
                valore_curva = curve_isofoniche[key]['y'][index]

                if valore_curva > SPL:
#                    list_loudness.append(loudness)
                    break
                else:
                    loudness = key
#            else:
#                print("here")
        
        list_loudness.append(loudness)
                                        
    return list_loudness

