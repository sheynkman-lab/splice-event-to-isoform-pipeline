import pandas as pd
import os
from gtfparse import read_gtf

def loadSE(rmatsPath, type): 
    SEpath = rmatsPath + "/SE.MATS." + type + ".txt"
    if not os.path.exists(SEpath):
        raise Exception("path not found: " + SEpath)

    SE = pd.read_table(SEpath)
    return SE

def loadMXE(rmatsPath, type): 
    MXEpath = rmatsPath + "/MXE.MATS." + type + ".txt"
    if not os.path.exists(MXEpath):
        raise Exception("path not found: " + MXEpath)

    MXE = pd.read_table(MXEpath)
    return MXE

def loadA3SS(rmatsPath, type): 
    A3SSpath = rmatsPath + "/A3SS.MATS." + type + ".txt"

    if not os.path.exists(A3SSpath):
        raise Exception("path not found: " + A3SSpath)

    A3SS = pd.read_table(A3SSpath)
    return A3SS

def loadA5SS(rmatsPath, type): 
    A5SSpath = rmatsPath + "/A5SS.MATS." + type + ".txt"
    if not os.path.exists(A5SSpath):
        raise Exception("path not found: " + A5SSpath)

    A5SS = pd.read_table(A5SSpath)
    return A5SS