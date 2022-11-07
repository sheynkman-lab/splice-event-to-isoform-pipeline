import pandas as pd
import os
from gtfparse import read_gtf


## loading all the event data
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


def loadLRannot(gtfpath):
    # read in raw GTF, select columns that I want, return 
    # currently, throwing an error where read_gtf is starting one loop, then starting another loop
    # Where I left off before error thrown: need to make a superset of annotation from C1 and C2
    print("load LR annot: annot raw")
    annot_raw = read_gtf(gtfpath)
    print("load LR annot: selecting cols")
    LRannot = annot_raw[["gene_id", "gene_name", "transcript_id", "feature", "seqname", "strand", "exon_number", "start", "end"]]
    print("load LR annot: returning cols")
    return LRannot

def loadLRquant(tsvpath, count_column_name, condition_name):
    # quantpath_c1 = "/Volumes/sheynkman/projects/shay_thesis/data/EC-LR/long-read-EC-data/01_tsv/WTC11-1.tsv"
    # quantpath_c2 = "/Volumes/sheynkman/projects/shay_thesis/data/EC-LR/long-read-EC-data/01_tsv/EC.tsv"
    # count_column_name_c1 = "rep1ENCSR507JOF"
    # count_column_name_c2 = "rep1ENCSR148IIG"

    # loading the transcript quantification (for one condition)
    print("load LR quant: reading table, selecting annotation & counts")
    quant = pd.read_table(tsvpath)[["annot_transcript_id", count_column_name]]
    print("load LR quant: summing counts")
    sumcounts = quant[count_column_name].sum()
    print("load LR quant: making col name")
    tpm_colname = "tpm_" + condition_name
    print("load LR quant: applying calcTPM function")
    quant[tpm_colname] = quant.apply(lambda row: calcTPM(row, count_column_name, sumcounts), axis = 1)
    print("load LR quant: selecting ID and tpm")
    quant = quant[["annot_transcript_id", tpm_colname]]
    print("load LR quant: renaming annot_transcript_id to transcript_id")
    quant = quant.rename(columns = {'annot_transcript_id':'transcript_id'})
    print("---LR quantification file has been read for condition", condition_name)
    return quant

def calcTPM(quantrow, count_column_name, sumcounts):
    # Helper function to apply to each row of quantification file, referenced in loadLRquant
    tpm = ((quantrow[count_column_name]/sumcounts)*1000000)
    return tpm

def mergeAnnotQuants(LRannot, LRquant_c1, LRquant_c2):
    # 
    print("merge Annot & Quants: left joining LR annotations to condition 1 TPMs (left join)")
    joined = pd.merge(LRannot, LRquant_c1, on='transcript_id', how ='left')
    print("merge Annot & Quants: left joining LR annotations to condition 2 TPMs (left join)")
    joined = pd.merge(joined, LRquant_c2, on='transcript_id', how='left')
    print("merge Annot & Quants: filling NAs")
    joined = joined.fillna(0)
    print("---LR annotation and TPMs have been merged---")
    #print("-----------------------------------")
    #print(joined.tail(20))
    
    return joined