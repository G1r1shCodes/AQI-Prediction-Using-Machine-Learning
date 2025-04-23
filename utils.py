import numpy as np

def get_input_array(co, no2, o3, t, rh, ah):
    return np.array([[co, no2, o3, t, rh, ah]])
