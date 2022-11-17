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
    rmatsPath = "/Volumes/sheynkman/projects/shay_thesis/input-data/01_ips-s1s2_rmats-out_input"
    type = "JCEC"
    eventTypes = ("se", "mxe", "a3ss", "a5ss")
    eventDict = {}

    se = loadSE(rmatsPath, type)
    mxe = loadMXE(rmatsPath, type)
    a3ss = loadA3SS(rmatsPath, type)
    a5ss = loadA5SS(rmatsPath, type)

    output_folder = "/Volumes/sheynkman/projects/shay_thesis/output/01_intermediate-output/"

    lrannotpath = "/Volumes/sheynkman/projects/shay_thesis/input-data/02_long-read-EC-WTC11-1_input/01_annotation/EC.gtf"
    # lrannotpath_2 = "/Volumes/sheynkman/projects/shay_thesis/input-data/02_long-read-EC-WTC11-1_input/01_annotation/WTC11-1.gtf"
    lrannot = loadLRannot(lrannotpath)

    quantpath_c1 = "/Volumes/sheynkman/projects/shay_thesis/input-data/02_long-read-EC-WTC11-1_input/02_quantification/WTC11-1.tsv"
    quantpath_c2 = "/Volumes/sheynkman/projects/shay_thesis/input-data/02_long-read-EC-WTC11-1_input/02_quantification/EC.tsv"
    

    count_column_name_c1 = "rep1ENCSR507JOF"
    count_column_name_c2 = "rep1ENCSR148IIG"
    
    lrquant_c1 = loadLRquant(quantpath_c1, count_column_name_c1, "WTC11-1")
    lrquant_c2 = loadLRquant(quantpath_c2, count_column_name_c2, "EC")

     # se.to_csv((output_folder + "01_short-read_pandas/se.csv"), index = False)
    # mxe.to_csv((output_folder + "01_short-read_pandas/mxe.csv"), index = False)
    # a3ss.to_csv((output_folder + "01_short-read_pandas/a3ss.csv"), index = False)
    # a5ss.to_csv((output_folder + "01_short-read_pandas/a5ss.csv"), index = False)
    # lrannot.to_csv((output_folder + "02_long-read_pandas/lr_annotation-file.csv"), index = False)
    # lrquant_c1.to_csv((output_folder + "02_long-read_pandas/lr_quantification_c1.csv"), index = False)
    # lrquant_c2.to_csv((output_folder + "02_long-read_pandas/lr_quantification_c2.csv"), index = False)

    lr_alldata = mergeAnnotQuants(lrannot, lrquant_c1, lrquant_c2)

    lr_alldata.to_csv((output_folder + "lr_annot-quant.csv"), index = False)

    
    #JunctionDict = getLRJunctionDict(lr_alldata) 
    # addJunctionsToTable(lr_alldata, JunctionDict)
    # map(lr_alldata, [se, mxe, a3ss, a5ss])
main()