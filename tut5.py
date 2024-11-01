import numpy as np # type: ignore
from scipy.signal import convolve2d # type: ignore

def simple_1d_convolution(input_array, conv_mask):
    """
    Perform 1D convolution on an input array using a convolution mask.
    
    Parameters:
    input_array (list or np.array): The input numbers array.
    conv_mask (list or np.array): The convolution mask.
    
    Returns:
    np.array: The convolution result.
    """
    return np.convolve(input_array, conv_mask, mode='full')

def simple_2d_convolution(input_array, conv_mask):
    """
    Perform 2D convolution on an input array using a convolution mask.
    
    Parameters:
    input_array (np.array): The 2D input array.
    conv_mask (np.array): The convolution mask.
    
    Returns:
    np.array: The convolution result.
    """
    return convolve2d(input_array, conv_mask, mode='full')