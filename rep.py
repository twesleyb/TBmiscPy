import numpy as np

def rep(x, reps=1, each=False, length=0):
    """ implementation of functionality of rep() and rep_len() from R

    Attributes:
        x: numpy array, which will be flattened
        reps: int, number of times x should be repeated
        each: logical; should each element be repeated reps times before the next
        length: int, length desired; if >0, overrides reps argument
    """
    if length > 0:
        reps = np.int(np.ceil(length / x.size))
    x = np.repeat(x, reps)
    if(not each):
        x = x.reshape(-1, reps).T.ravel() 
    if length > 0:
        x = x[0:length]
    return(x)