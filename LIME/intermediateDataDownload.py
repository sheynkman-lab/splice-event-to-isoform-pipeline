import pandas as pd
from pathlib import Path
from LIME.readData import *
from gtfparse import read_gtf

def main():
    # rmats_out_folder = "/Volumes/sheynkman/projects/shay_thesis/input-data/01_ips-s1s2_rmats-out_input"
    # output_folder = "/Volumes/sheynkman/projects/shay_thesis/output/01_tmp/01_short-read_pandas"
    # c1annot = "/Volumes/sheynkman/projects/shay_thesis/input-data/02_long-read-EC-WTC11-1_input/01_annotation/WTC11-1.gtf"
    # c1quant = "/Volumes/sheynkman/projects/shay_thesis/input-data/02_long-read-EC-WTC11-1_input/02_quantification/WTC11-1.tsv"
    # c2quant = "/Volumes/sheynkman/projects/shay_thesis/input-data/02_long-read-EC-WTC11-1_input/02_quantification/EC.tsv"
    # c1_quantcol = "rep1ENCSR507JOF"
    # c2_quantcol = "rep1ENCSR148IIG"
    # condition1 = "WTC11"
    # condition2 = "EC"
    # type = "JC"
    # se = loadSE(rmats_out_folder, type, output_folder)
    # print("se done")
    # mxe = loadMXE(rmats_out_folder, type, output_folder)
    # print("mxe done")
    # a3ss = loadA3SS(rmats_out_folder, type, output_folder)
    # print("a3ss done")
    # a5ss = loadA5SS(rmats_out_folder, type, output_folder)
    # print("a5ss done")

    # lrannot = loadLRannot(c1annot)
    # print("lr annot done")
    # lrquant_c1 = loadLRquant(c1quant, c1_quantcol, condition1)
    # print("lrquant1 done")
    # lrquant_c2 = loadLRquant(c2quant, c2_quantcol, condition2)
    # print("lrquant2 done")

    # print("merging")
    # outputfilelr = "/Volumes/sheynkman/projects/shay_thesis/output/01_tmp/02_long-read-pandas/merge.csv"

    # lr_alldata = mergeAnnotQuants(lrannot, lrquant_c1, lrquant_c2)
    # lr_alldata.to_csv(outputfilelr, index = False)
    
    # print("all done")
    return

main()