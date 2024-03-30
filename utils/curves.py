import numpy as np

def get_equal_loudness_contour_from_L_N(L_N):
    
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
    
    equal_loudness_contour = (L_N - (L_N * b_f * T_f) - 4.2 + 4.2 * (b_f * T_f) + a_f * T_f)/(a_f - L_N * b_f + 4.2 * b_f)
    
    freq = np.array([20., 25., 31.5, 40., 50., 63., 80., 100., 125.,
                    160., 200., 250., 315., 400., 500., 630, 800.,
                    1000., 1250., 1600., 2000., 2500., 3150, 
                    4000., 5000., 6300., 8000., 10000., 12500
                    ])
    
    return freq, equal_loudness_contour



def generate_equal_loudness_contours(year='1987'):
        
    contours_1987 = {0: {'x': [20.0, 25.0, 31.5, 40.0, 50.0, 63.0, 80.0, 100.0, 125.0, 160.0, 200.0, 250.0, 315.0, 400.0, 500.0, 630.0, 
                          800.0, 1000.0, 1250.0, 1600.0, 2000.0, 2500.0, 3150.0, 4000.0, 5000.0, 6300.0, 8000.0, 10000.0, 12500.0], 
                    'y': [72.53, 63.1, 54.27, 46.18, 39.28, 32.89, 27.04, 22.26, 17.78, 13.81, 10.76, 8.1, 5.7, 3.88, 2.53, 1.31, 
                          0.45, 0.0, -0.65, -1.87, -3.53, -5.72, -8.1, -8.33, -5.42, 2.51, 11.61, 13.11, 8.84]},
                10: {'x': [20.0, 25.0, 31.5, 40.0, 50.0, 63.0, 80.0, 100.0, 125.0, 160.0, 200.0, 250.0, 315.0, 400.0, 500.0, 630.0,
                           800.0, 1000.0, 1250.0, 1600.0, 2000.0, 2500.0, 3150.0, 4000.0, 5000.0, 6300.0, 8000.0, 10000.0, 12500.0], 
                     'y': [76.81, 67.69, 59.17, 51.53, 45.1, 39.17, 33.67, 29.1, 24.81, 21.01, 18.07, 15.56, 13.39, 11.86, 10.86, 
                           10.14, 9.88, 10.0, 9.68, 8.73, 7.19, 4.98, 2.55, 2.16, 4.84, 12.25, 20.43, 21.03, 15.54]},
                20: {'x': [20.0, 25.0, 31.5, 40.0, 50.0, 63.0, 80.0, 100.0, 125.0, 160.0, 200.0, 250.0, 315.0, 400.0, 500.0, 630.0,
                           800.0, 1000.0, 1250.0, 1600.0, 2000.0, 2500.0, 3150.0, 4000.0, 5000.0, 6300.0, 8000.0, 10000.0, 12500.0],
                    'y': [81.3, 72.5, 64.3, 57.1, 51.16, 45.68, 40.54, 36.18, 32.1, 28.47, 25.66, 23.31, 21.36, 20.11, 19.42, 19.14, 
                          19.39, 20.0, 19.94, 19.17, 17.69, 15.44, 12.97, 12.46, 14.98, 21.98, 29.4, 29.22, 22.7]},
                 30: {'x': [20.0, 25.0, 31.5, 40.0, 50.0, 63.0, 80.0, 100.0, 125.0, 160.0, 200.0, 250.0, 315.0, 400.0, 500.0, 630.0,
                        800.0, 1000.0, 1250.0, 1600.0, 2000.0, 2500.0, 3150.0, 4000.0, 5000.0, 6300.0, 8000.0, 10000.0, 12500.0],                                  'y': [86.02, 77.56, 69.7, 62.94, 57.46, 52.44, 47.65, 43.53, 39.67, 36.22, 33.55, 31.36, 29.62, 28.63, 28.22, 
                        28.32, 29.0, 30.0, 30.11, 29.47, 27.99, 25.67, 23.17, 22.57, 25.01, 31.72, 38.5, 37.69, 30.36]},
                40: {'x': [20.0, 25.0, 31.5, 40.0, 50.0, 63.0, 80.0, 100.0, 125.0, 160.0, 200.0, 250.0, 315.0, 400.0, 500.0, 630.0,
                           800.0, 1000.0, 1250.0, 1600.0, 2000.0, 2500.0, 3150.0, 4000.0, 5000.0, 6300.0, 8000.0, 10000.0, 12500.0],
                    'y': [90.98, 82.89, 75.36, 69.04, 64.03, 59.45, 55.02, 51.16, 47.53, 44.28, 41.75, 39.72, 38.2, 37.44, 37.27,
                          37.69, 38.71, 40.0, 40.19, 39.62, 38.1, 35.68, 33.15, 32.5, 34.93, 41.46, 47.75, 46.47, 38.59]},
                50: {'x': [20.0, 25.0, 31.5, 40.0, 50.0, 63.0, 80.0, 100.0, 125.0, 160.0, 200.0, 250.0, 315.0, 400.0, 500.0, 630.0,
                           800.0, 1000.0, 1250.0, 1600.0, 2000.0, 2500.0, 3150.0, 4000.0, 5000.0, 6300.0, 8000.0, 10000.0, 12500.0],
                    'y': [96.21, 88.5, 81.33, 75.44, 70.89, 66.74, 62.67, 59.07, 55.7, 52.66, 50.27, 48.42, 47.09, 46.55, 46.57, 
                          47.24, 48.52, 50.0, 50.2, 49.64, 48.02, 45.48, 42.91, 42.26, 44.74, 51.2, 57.16, 55.57, 47.45]},
                60: {'x': [20.0, 25.0, 31.5, 40.0, 50.0, 63.0, 80.0, 100.0, 125.0, 160.0, 200.0, 250.0, 315.0, 400.0, 500.0, 630.0,
                           800.0, 1000.0, 1250.0, 1600.0, 2000.0, 2500.0, 3150.0, 4000.0, 5000.0, 6300.0, 8000.0, 10000.0, 12500.0],
                    'y': [101.73, 94.43, 87.62, 82.15, 78.04, 74.32, 70.61, 67.29, 64.19, 61.38, 59.16, 57.48, 56.34, 55.98, 56.15,
                          57.0, 58.42, 60.0, 60.13, 59.52, 57.75, 55.07, 52.48, 51.84, 54.44, 60.93, 66.71, 65.0, 57.01]},
                70: {'x': [20.0, 25.0, 31.5, 40.0, 50.0, 63.0, 80.0, 100.0, 125.0, 160.0, 200.0, 250.0, 315.0, 400.0, 500.0, 630.0, 
                           800.0, 1000.0, 1250.0, 1600.0, 2000.0, 2500.0, 3150.0, 4000.0, 5000.0, 6300.0, 8000.0, 10000.0, 12500.0],
                    'y': [107.57, 100.7, 94.26, 89.19, 85.52, 82.21, 78.85, 75.84, 73.02, 70.46, 68.41, 66.92, 65.95, 65.75, 66.01,
                          66.96, 68.42, 70.0, 69.99, 69.26, 67.29, 64.46, 61.84, 61.25, 64.04, 70.67, 76.43, 74.78, 67.37]},
                80: {'x': [20.0, 25.0, 31.5, 40.0, 50.0, 63.0, 80.0, 100.0, 125.0, 160.0, 200.0, 250.0, 315.0, 400.0, 500.0, 630.0,
                           800.0, 1000.0, 1250.0, 1600.0, 2000.0, 2500.0, 3150.0, 4000.0, 5000.0, 6300.0, 8000.0, 10000.0, 12500.0],
                    'y': [113.74, 107.33, 101.27, 96.6, 93.34, 90.42, 87.41, 84.73, 82.23, 79.93, 78.07, 76.77, 75.95, 75.88, 76.17,
                          77.13, 78.53, 80.0, 79.76, 78.87, 76.67, 73.66, 71.02, 70.51, 73.53, 80.41, 86.3, 84.93, 78.61]},
                90: {'x': [20.0, 25.0, 31.5, 40.0, 50.0, 63.0, 80.0, 100.0, 125.0, 160.0, 200.0, 250.0, 315.0, 400.0, 500.0, 630.0,
                           800.0, 1000.0, 1250.0, 1600.0, 2000.0, 2500.0, 3150.0, 4000.0, 5000.0, 6300.0, 8000.0, 10000.0, 12500.0],
                    'y': [120.29, 114.37, 108.7, 104.39, 101.53, 98.98, 96.32, 93.99, 91.82, 89.81, 88.15, 87.05, 86.37, 86.38, 86.64,
                          87.52, 88.73, 90.0, 89.46, 88.36, 85.87, 82.66, 80.01, 79.6, 82.92, 90.14, 96.35, 95.48, 90.88]} 
                    }
        
    contours_2003 = {0: {'x': [20.0, 25.0, 31.5, 40.0, 50.0, 63.0, 80.0, 100.0, 125.0, 160.0, 200.0, 250.0, 315.0, 400.0, 500.0, 630.0, 
                               800.0, 1000.0, 1250.0, 1600.0, 2000.0, 2500.0, 3150.0, 4000.0, 5000.0, 6300.0, 8000.0, 10000.0, 12500.0],
                        'y': [76.55, 65.62, 55.12, 45.53, 37.63, 30.86, 25.02, 20.51, 16.65, 13.12, 10.09, 7.54, 5.11, 3.06, 1.48, 0.3,
                              -0.3, -0.01, 1.03, -1.19, -4.11, -7.05, -9.03, -8.49, -4.48, 3.28, 9.83, 10.48, 8.38]},
                    10: {'x': [20.0, 25.0, 31.5, 40.0, 50.0, 63.0, 80.0, 100.0, 125.0, 160.0, 200.0, 250.0, 315.0, 400.0, 500.0, 630.0,
                               800.0, 1000.0, 1250.0, 1600.0, 2000.0, 2500.0, 3150.0, 4000.0, 5000.0, 6300.0, 8000.0, 10000.0, 12500.0],
                        'y': [83.75, 75.76, 68.21, 61.14, 54.96, 49.01, 43.24, 38.13, 33.48, 28.77, 24.84, 21.33, 18.05, 15.14, 12.98,
                              11.18, 9.99, 10.0, 11.26, 10.43, 7.27, 4.45, 3.04, 3.8, 7.46, 14.35, 20.98, 23.43, 22.33]},
                    20: {'x': [20.0, 25.0, 31.5, 40.0, 50.0, 63.0, 80.0, 100.0, 125.0, 160.0, 200.0, 250.0, 315.0, 400.0, 500.0, 630.0,
                               800.0, 1000.0, 1250.0, 1600.0, 2000.0, 2500.0, 3150.0, 4000.0, 5000.0, 6300.0, 8000.0, 10000.0, 12500.0],
                        'y': [89.58, 82.65, 75.98, 69.62, 64.02, 58.55, 53.19, 48.38, 43.94, 39.37, 35.51, 31.99, 28.69, 25.67, 23.43,
                              21.48, 20.1, 20.01, 21.46, 21.4, 18.15, 15.38, 14.26, 15.14, 18.63, 25.02, 31.52, 34.43, 33.04]},
                    30: {'x': [20.0, 25.0, 31.5, 40.0, 50.0, 63.0, 80.0, 100.0, 125.0, 160.0, 200.0, 250.0, 315.0, 400.0, 500.0, 630.0,
                               800.0, 1000.0, 1250.0, 1600.0, 2000.0, 2500.0, 3150.0, 4000.0, 5000.0, 6300.0, 8000.0, 10000.0, 12500.0],
                        'y': [94.85, 88.52, 82.36, 76.45, 71.26, 66.2, 61.22, 56.76, 52.64, 48.38, 44.78, 41.47, 38.36, 35.5, 33.37, 31.49,
                              30.11, 30.01, 31.65, 32.04, 28.76, 26.03, 25.05, 26.02, 29.42, 35.48, 41.74, 44.57, 42.55]},
                    40: {'x': [20.0, 25.0, 31.5, 40.0, 50.0, 63.0, 80.0, 100.0, 125.0, 160.0, 200.0, 250.0, 315.0, 400.0, 500.0, 630.0, 
                               800.0, 1000.0, 1250.0, 1600.0, 2000.0, 2500.0, 3150.0, 4000.0, 5000.0, 6300.0, 8000.0, 10000.0, 12500.0],
                        'y': [99.85, 93.94, 88.17, 82.63, 77.78, 73.08, 68.48, 64.37, 60.59, 56.7, 53.41, 50.4, 47.58, 44.98, 43.05, 41.34,
                              40.06, 40.01, 41.82, 42.51, 39.23, 36.51, 35.61, 36.65, 40.01, 45.83, 51.8, 54.28, 51.49]},
                    50: {'x': [20.0, 25.0, 31.5, 40.0, 50.0, 63.0, 80.0, 100.0, 125.0, 160.0, 200.0, 250.0, 315.0, 400.0, 500.0, 630.0, 
                               800.0, 1000.0, 1250.0, 1600.0, 2000.0, 2500.0, 3150.0, 4000.0, 5000.0, 6300.0, 8000.0, 10000.0, 12500.0],
                        'y': [104.72, 99.14, 93.69, 88.49, 83.96, 79.61, 75.36, 71.61, 68.17, 64.68, 61.72, 59.04, 56.55, 54.26, 52.59, 
                              51.1, 49.98, 50.01, 51.99, 52.88, 49.62, 46.91, 46.05, 47.15, 50.48, 56.11, 61.76, 63.78, 60.14]},
                    60: {'x': [20.0, 25.0, 31.5, 40.0, 50.0, 63.0, 80.0, 100.0, 125.0, 160.0, 200.0, 250.0, 315.0, 400.0, 500.0, 630.0,
                               800.0, 1000.0, 1250.0, 1600.0, 2000.0, 2500.0, 3150.0, 4000.0, 5000.0, 6300.0, 8000.0, 10000.0, 12500.0],
                        'y': [109.51, 104.23, 99.08, 94.18, 89.96, 85.94, 82.05, 78.65, 75.56, 72.47, 69.86, 67.53, 65.39, 63.45, 62.05,
                              60.81, 59.89, 60.01, 62.15, 63.19, 59.96, 57.26, 56.42, 57.57, 60.89, 66.36, 71.66, 73.16, 68.63]},
                    70: {'x': [20.0, 25.0, 31.5, 40.0, 50.0, 63.0, 80.0, 100.0, 125.0, 160.0, 200.0, 250.0, 315.0, 400.0, 500.0, 630.0, 
                               800.0, 1000.0, 1250.0, 1600.0, 2000.0, 2500.0, 3150.0, 4000.0, 5000.0, 6300.0, 8000.0, 10000.0, 12500.0],
                        'y': [114.26, 109.25, 104.38, 99.78, 95.87, 92.18, 88.64, 85.6, 82.85, 80.17, 77.92, 75.94, 74.16, 72.58, 71.47, 
                              70.5, 69.78, 70.01, 72.32, 73.47, 70.28, 67.58, 66.76, 67.95, 71.26, 76.59, 81.54, 82.46, 77.04]},
                    80: {'x': [20.0, 25.0, 31.5, 40.0, 50.0, 63.0, 80.0, 100.0, 125.0, 160.0, 200.0, 250.0, 315.0, 400.0, 500.0, 630.0,
                               800.0, 1000.0, 1250.0, 1600.0, 2000.0, 2500.0, 3150.0, 4000.0, 5000.0, 6300.0, 8000.0, 10000.0, 12500.0],
                        'y': [118.99, 114.23, 109.65, 105.34, 101.72, 98.36, 95.17, 92.48, 90.09, 87.82, 85.92, 84.31, 82.89, 81.68, 80.86,
                              80.17, 79.67, 80.01, 82.48, 83.74, 80.59, 77.88, 77.07, 78.31, 81.62, 86.81, 91.41, 91.74, 85.41]},
                    90: {'x': [20.0, 25.0, 31.5, 40.0, 50.0, 63.0, 80.0, 100.0, 125.0, 160.0, 200.0, 250.0, 315.0, 400.0, 500.0, 630.0, 
                               800.0, 1000.0, 1250.0, 1600.0, 2000.0, 2500.0, 3150.0, 4000.0, 5000.0, 6300.0, 8000.0, 10000.0, 12500.0],
                        'y': [123.71, 119.2, 114.88, 110.87, 107.55, 104.51, 101.67, 99.33, 97.29, 95.43, 93.89, 92.65, 91.6, 90.76, 90.24,
                              89.84, 89.55, 90.01, 92.65, 94.0, 90.88, 88.18, 87.38, 88.66, 91.96, 97.02, 101.26, 100.99, 93.75]}
                    }
        
    if year=='1987':
        return contours_1987
    elif year=='2003':                     
        return contours_2003
    else:
        return {}
                     
def generate_weighting_curve(min_freq=0, max_freq = 20000., weigthing='A', octave=False):
    """
    Generate weighting cruves in octave or 1/3 octave bands
    """
    
    if octave:
        #octave band
        A_weighting_dict = {16: -56.7, 31.5: -39.4, 63: -26.2, 125: -16.1, 
                          250: -8.6, 500: -3.2, 1000: 0, 2000: 1.2, 4000: 1, 
                          8000: -1.1, 16000: -6.6, 20000: -9.3 
                         }

        A_weighting = np.asarray([v for k, v in A_weighting_dict.items() if k >= min_freq and k <= max_freq])

    else:        
        A_weighting_dict = {10: -70.4, 12.5: -63.4, 16: -56.7, 20: -50.5,
                               25: -44.7, 31.5: -39.4, 40: -34.6, 50: -30.2,
                               63: -26.2, 80: -22.5, 100: -19.1, 125: -16.1, 
                               160: -13.4, 200: -10.9, 250: -8.6, 315: -6.6,
                               400: -4.8, 500: -3.2, 630: -1.9, 800: -0.8,
                               1000: 0, 1250: 0.6, 1600: 1., 2000: 1.2, 2500: 1.3, 
                               3150: 1.2, 4000: 1., 5000: 0.5, 6300: -0.1,
                               8000: -1.1, 10000: -2.5, 12500: -4.3, 
                               16000: -6.6, 20000: -9.3
                            }

        A_weighting = np.asarray([v for k, v in A_weighting_dict.items() if k >= min_freq and k <= max_freq])
        
    return A_weighting     


def generate_NC():
    out_dict = {"NC_15": {63: 47, 125: 36, 250: 29, 500: 22, 1000: 17, 2000: 14, 4000: 12, 8000: 11},
                "NC_20": {63: 51, 125: 40, 250: 33, 500: 26, 1000: 22, 2000: 19, 4000: 17, 8000: 16},
                "NC_25": {63: 54, 125: 44, 250: 37, 500: 31, 1000: 27, 2000: 24, 4000: 22, 8000: 21},
                "NC_30": {63: 57, 125: 48, 250: 41, 500: 35, 1000: 31, 2000: 29, 4000: 28, 8000: 27},
                "NC_35": {63: 60, 125: 52, 250: 45, 500: 40, 1000: 36, 2000: 34, 4000: 33, 8000: 32},
                "NC_40": {63: 64, 125: 56, 250: 50, 500: 45, 1000: 41, 2000: 39, 4000: 38, 8000: 37},
                "NC_45": {63: 67, 125: 60, 250: 54, 500: 49, 1000: 46, 2000: 44, 4000: 43, 8000: 42},
                "NC_50": {63: 71, 125: 64, 250: 58, 500: 54, 1000: 51, 2000: 49, 4000: 48, 8000: 47},
                "NC_55": {63: 74, 125: 67, 250: 62, 500: 58, 1000: 56, 2000: 54, 4000: 53, 8000: 52},
                "NC_60": {63: 77, 125: 71, 250: 67, 500: 63, 1000: 61, 2000: 59, 4000: 58, 8000: 57},
                "NC_65": {63: 80, 125: 75, 250: 71, 500: 68, 1000: 66, 2000: 64, 4000: 63, 8000: 62},
                "NC_70": {63: 83, 125: 79, 250: 75,500:  72, 1000: 71, 2000: 70, 4000: 69, 8000: 68},
    }
    
    return out_dict


def generate_NR_curves():
    out_dict = {"NC_0": {31.5: 55, 63: 36, 125: 22, 250: 12, 500: 5, 1000: 0, 2000: -4, 4000: -6, 8000: -8},
                "NC_10": {31.5: 62, 63: 43, 125: 31, 250: 21, 500: 15, 1000: 10, 2000: 7, 4000: 4, 8000: 2},
                "NC_20": {31.5: 69, 63: 51, 125: 39, 250: 31, 500: 24, 1000: 20, 2000: 17, 4000: 14, 8000: 13},
                "NC_30": {31.5: 76, 63: 59, 125: 48, 250: 40, 500: 34, 1000: 30, 2000: 27, 4000: 25, 8000: 23},
                "NC_40": {31.5: 83, 63: 67, 125: 57, 250: 49, 500: 44, 1000: 40, 2000: 37, 4000: 35, 8000: 33},
                "NC_50": {31.5: 89, 63: 75, 125: 66, 250: 59, 500: 54, 1000: 50, 2000: 47, 4000: 45, 8000: 44},
                "NC_60": {31.5: 96, 63: 83, 125: 74, 250: 68, 500: 63, 1000: 60, 2000: 57, 4000: 55, 8000: 54},
                "NC_70": {31.5: 103, 63: 91, 125: 83, 250: 77, 500: 73, 1000: 70, 2000: 68, 4000: 66, 8000: 64},
                "NC_80": {31.5: 110, 63: 99, 125: 92, 250: 86, 500: 83, 1000: 80, 2000: 78, 4000: 76, 8000: 74},
                "NC_90": {31.5: 117, 63: 107, 125: 100, 250: 96, 500: 93, 1000: 90, 2000: 88, 4000: 86, 8000: 85},
                "NC_100": {31.5: 124, 63: 115, 125: 109, 250: 105, 500: 102, 1000: 100, 2000: 98, 4000: 96, 8000: 95},
                "NC_110": {31.5: 130, 63: 122, 125: 118, 250: 114, 500: 112, 1000: 110, 2000: 108, 4000: 107, 8000: 105},
                "NC_120": {31.5: 137, 63: 130, 125: 126, 250: 124, 500: 122, 1000: 120, 2000: 118, 4000: 117, 8000: 116},
                "NC_130": {31.5: 144, 63: 138, 125: 135, 250: 133, 500: 131, 1000: 130, 2000: 128, 4000: 127, 8000: 126},
                
    }
    
    return out_dict

