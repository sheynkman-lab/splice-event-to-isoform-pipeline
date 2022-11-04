import pandas as pd
import os
from gtfparse import read_gtf

def loadAll():
    # rmatsPath = input("Give path to rMATS output folder: ")
    # type = input("give type: ")
    # condition1 = input("give condition 1: ")
    # condition2 = input("give condition 2: ")

    rmatsPath = "/Volumes/sheynkman/projects/EC_stem_cell_differentiation/001_ips-s1s2/003_ips-s1s2_output/002_ips-s1s2_rmats-out"
    type = "JCEC"
    condition1 = "iPSC"
    condition2 = "iEC"

    SE = loadSE(rmatsPath, type)
    MXE = loadMXE(rmatsPath, type)
    A3SS = loadA3SS(rmatsPath, type)
    A5SS = loadA5SS(rmatsPath, type)

def loadSE(rmatsPath, type): 
    SEpath = rmatsPath + "/SE.MATS." + type + ".txt"
    if not os.path.exists(SEpath):
        raise Exception("path not found: " + SEpath)

    SE = pd.read_table(SEPath)
    return SE

def loadMXE(rmatsPath): 
    MXEpath = rmatsPath + "/MXE.MATS." + type + ".txt"
    if not os.path.exists(MXEpath):
        raise Exception("path not found: " + MXEpath)

    MXE = pd.read_table(MXEPath)
    return MXE

def loadA3SS(rmatsPath): 
    A3SSpath = rmatsPath + "/A3SS.MATS." + type + ".txt"

    if not os.path.exists(A3SSpath):
        raise Exception("path not found: " + A3SSpath)

    A3SS = pd.read_table(A3SSpath)
    return A3SS

def loadA5SS(rmatsPath): 
    A5SSpath = rmatsPath + "/A5SS.MATS." + type + ".txt"
    if not os.path.exists(A5SSpath):
        raise Exception("path not found: " + A5SSpath)

    A5SS = pd.read_table(A5SSpath)
    return A5SS

loadAll()