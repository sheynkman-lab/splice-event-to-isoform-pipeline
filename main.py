import pandas as pd
from map import *
from archive.getEvents import *
from archive.structures import *
from getTranscripts import *
from archive.getEvents import *
from archive.convertToTable import *
from readData import *
import os
from gtfparse import read_gtf

def main():

    ## step 1: read rMATS data
    srSource = "rmats"
    lrSource = "pacbio"
    rmatsPath = "/Volumes/sheynkman/projects/EC_stem_cell_differentiation/001_ips-s1s2/003_ips-s1s2_output/002_ips-s1s2_rmats-out"
    type = "JCEC"
    eventTypes = ("se", "mxe", "a3ss", "a5ss")
    eventDict = {}

    # se = loadSE(rmatsPath, type)
    # mxe = loadMXE(rmatsPath, type)
    # a3ss = loadA3SS(rmatsPath, type)
    # a5ss = loadA5SS(rmatsPath, type)


    lrannotpath = "/Volumes/sheynkman/projects/shay_thesis/data/EC-LR/long-read-EC-data/03_chr19_gtfs/chr19_EC.gtf"

    lrannot = loadLRannot(lrannotpath)

    quantpath_c1 = "/Volumes/sheynkman/projects/shay_thesis/data/EC-LR/long-read-EC-data/01_tsv/WTC11-1.tsv"
    quantpath_c2 = "/Volumes/sheynkman/projects/shay_thesis/data/EC-LR/long-read-EC-data/01_tsv/EC.tsv"
    count_column_name_c1 = "rep1ENCSR507JOF"
    count_column_name_c2 = "rep1ENCSR148IIG"

    lrquant_c1 = loadLRquant(quantpath_c1, count_column_name_c1, "WTC11-1")
    lrquant_c2 = loadLRquant(quantpath_c2, count_column_name_c2, "EC")

    lr_alldata = mergeAnnotQuants(lrannot, lrquant_c1, lrquant_c2)
    #JunctionDict = getLRJunctionDict(lr_alldata) 
    # addJunctionsToTable(lr_alldata, JunctionDict)
    # map(lr_alldata, [se, mxe, a3ss, a5ss])
main()