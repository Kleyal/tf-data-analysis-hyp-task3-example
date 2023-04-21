import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 405993924 # Ваш chat ID, не меняйте название переменной

def solution(x, y) -> bool:
    significance_level = 0.07
    pvalue = ttest_ind(x, y, equal_var=False, alternative='two-sided').pvalue
    return pvalue < significance_level
