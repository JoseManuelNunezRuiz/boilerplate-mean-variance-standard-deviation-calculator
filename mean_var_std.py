import numpy as np
import math

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')

    # Convert the list into 3x3 array:

    array = np.array(list).reshape(3,3

    # Caculate the mean:

    mean_1 = array.mean(axis = 0).to_list()
    mean_2 = array.mean(axis = 1).to_list()
    mean_3 = array.mean().to_list()
    mean = [mean_1, mean_2, mean_3]

    # Variance:

    var_1 = array.var(axis = 0).to_list()
    var_2 = array.var(axis = 0).to_list()
    var_3 = array.var().to_list()
    var = [var_1, var_2, var_3]

    # SD:

    std_1 = array.std(axis = 0).to_list()
    std_2 = array.std(axis = 1).to_list()
    std_3 = array.std().to_list()
    std = [std_1, std_2, std_3]

    # MAX:

    max_1 = array.max(axis = 0).to_list()
    max_2 = array.max(axis = 1).to_list()
    max_3 = array.max().to_list()
    max = [max_1 max_2, max_3]

    # MIN:

    min_1 = array.min(axis = 0).to_list()
    min_2 = array.min(axis = 1).to_list()
    min_3 = array.min().to_list()
    min = [min_1, min_2, min_3]

    # SUM:

    sum_1 = array.sum(axis = 0).to_list()
    sum_2 = array.sum(axis = 1).to_list()
    sum_3 = array.sum().to_list()
    sum = [sum_1, sum_2, sum_3]

    # Creating the dictionary:

    calculations = {
        'mean' : mean,
        'variance' : var,
        'standard deviation' : std,
        'max' : max,
        'min' : min,
        'sum' : sum
    }

    return calculations
