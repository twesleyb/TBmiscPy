#!/usr/bin/env python3
''' Implementation of R's rep() and rep_len() in python.'''

import numpy as np

def rep(x, times=1, length=0, each=False):
    """ implementation of functionality of rep() and rep_len() from R
    Adapted from miker's function np_rep() on StackOverflow.
    Usage:
        >>> rep([1,2],2) # output array([1,2,1,2])
    Attributes:
        x: list or numpy array, which will be flattened
        times: int, number of times x should be repeated
        length: int, length desired; if >0, overrides times argument
        each: logical; should each element be repeated reps times before the next
    """
    x = np.asarray(x)
    if length > 0:
        times = np.int(np.ceil(length / x.size))
    x = np.repeat(x, times)
    if(not each):
        x = x.reshape(-1, times).T.ravel() 
    if length > 0:
        x = x[0:length]
    return(x)
