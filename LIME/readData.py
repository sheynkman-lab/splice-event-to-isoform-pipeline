import pandas as pd
import os
from gtfparse import read_gtf
from LIME.TranscriptClass import *


## loading all the event data
def loadSE(rmatsPath, type, outputpath):
    SEpath = str(rmatsPath) + "/SE.MATS." + str(type) + ".txt"
    if not os.path.exists(SEpath):
        raise Exception("path not found: " + SEpath)

    SE = pd.read_table(SEpath)
    SE["incJunction"] = SE.apply(lambda row: getInclusionJunctionEvent(row, "se"), axis = 1)
    SE["excJunction"] = SE.apply(lambda row: getExclusionJunctionEvent(row, "se"), axis = 1)
    SE["ID"] = SE.apply(lambda row: getID_specific(row, "se"), axis = 1)
    SE["incID"] = SE.apply(lambda row: getInclusionID(row, "se"), axis = 1)
    SE["excID"] = SE.apply(lambda row: getExclusionID(row, "se"), axis = 1)
    
    outputfile = str(outputpath) + "/SE.csv"
    SE.to_csv(outputfile, index = False)
    return SE

def loadMXE(rmatsPath, type, outputpath): 
    MXEpath = str(rmatsPath) + "/MXE.MATS." + str(type) + ".txt"
    if not os.path.exists(MXEpath):
        raise Exception("path not found: " + MXEpath)

    MXE = pd.read_table(MXEpath)
    MXE["incJunction"] = MXE.apply(lambda row: getInclusionJunctionEvent(row, "mxe"), axis = 1)
    MXE["excJunction"] = MXE.apply(lambda row: getExclusionJunctionEvent(row, "mxe"), axis = 1)
    MXE["ID"] = MXE.apply(lambda row: getID_specific(row, "mxe"), axis = 1)
    MXE["incID"] = MXE.apply(lambda row: getInclusionID(row, "mxe"), axis = 1)
    MXE["excID"] = MXE.apply(lambda row: getExclusionID(row, "mxe"), axis = 1)
    outputfile = str(outputpath) + "/MXE.csv"
    MXE.to_csv(outputfile, index = False)

    return MXE

def loadA3SS(rmatsPath, type, outputpath): 
    A3SSpath = str(rmatsPath) + "/A3SS.MATS." + str(type) + ".txt"
    if not os.path.exists(A3SSpath):
        raise Exception("path not found: " + A3SSpath)

    A3SS = pd.read_table(A3SSpath)
    A3SS["incJunction"] = A3SS.apply(lambda row: getInclusionJunctionEvent(row, "a3ss"), axis = 1)
    A3SS["excJunction"] = A3SS.apply(lambda row: getExclusionJunctionEvent(row, "a3ss"), axis = 1)
    A3SS["ID"] = A3SS.apply(lambda row: getID_specific(row, "a3ss"), axis = 1)
    A3SS["incID"] = A3SS.apply(lambda row: getInclusionID(row, "a3ss"), axis = 1)
    A3SS["excID"] = A3SS.apply(lambda row: getExclusionID(row, "a3ss"), axis = 1)

    outputfile = str(outputpath) + "/A3SS.csv"
    A3SS.to_csv(outputfile, index = False)
    return A3SS

def loadA5SS(rmatsPath, type, outputpath): 
    A5SSpath = str(rmatsPath) + "/A5SS.MATS." + str(type) + ".txt"
    if not os.path.exists(A5SSpath):
        raise Exception("path not found: " + A5SSpath)

    A5SS = pd.read_table(A5SSpath)
    A5SS["incJunction"] = A5SS.apply(lambda row: getInclusionJunctionEvent(row, "a5ss"), axis = 1)
    A5SS["excJunction"] = A5SS.apply(lambda row: getExclusionJunctionEvent(row, "a5ss"), axis = 1)
    A5SS["ID"] = A5SS.apply(lambda row: getID_specific(row, "a5ss"), axis = 1)
    A5SS["incID"] = A5SS.apply(lambda row: getInclusionID(row, "a5ss"), axis = 1)
    A5SS["excID"] = A5SS.apply(lambda row: getExclusionID(row, "a5ss"), axis = 1)
    outputfile = str(outputpath) + "/A5SS.csv"
    A5SS.to_csv(outputfile, index = False)
    return A5SS


def getInclusionJunctionEvent(EventDF_row, type):
    type = type.lower()
    if type == "se":
        # NTS: i should change these to refer to the rows by name but rMATS output will stay consistent so it's not a pressing issue
        targetES = str(EventDF_row.iloc[5])
        targetEE = str(EventDF_row.iloc[6])
        upstreamEE = str(EventDF_row.iloc[8])
        downstreamES = str(EventDF_row.iloc[9])
        inclusion = upstreamEE + "-" + targetES + ":" + targetEE + "-" + downstreamES

    elif type == "mxe":
        exon1ES = EventDF_row.iloc[5]
        exon1EE = EventDF_row.iloc[6]
        upstreamEE = EventDF_row.iloc[10]
        downstreamES = EventDF_row.iloc[11]
        inclusion = str(upstreamEE) + "-" + str(exon1ES) + ":" + str(exon1EE) + "-" + str(downstreamES)
    
    elif type == "a3ss":
        longES = EventDF_row.iloc[5]
        flankingEE = EventDF_row.iloc[10]
        inclusion = str(flankingEE) + "-" + str(longES)

    elif type == "a5ss":
        longES = EventDF_row.iloc[5]
        flankingEE = EventDF_row.iloc[10]
        inclusion = str(longES) + "-" + str(flankingEE)
    
    return inclusion


def getExclusionJunctionEvent(EventDF_row, type):
    type = type.lower()
    if type == "se":
        targetES = EventDF_row.iloc[5]
        targetEE = EventDF_row.iloc[6]
        upstreamES = EventDF_row.iloc[7]
        upstreamEE = EventDF_row.iloc[8]
        downstreamES = EventDF_row.iloc[9]
        downstreamEE = EventDF_row.iloc[10]
        exclusion = str(upstreamEE) + ":" + str(downstreamES)

    elif type == "mxe":
        exon1ES = EventDF_row.iloc[5]
        exon1EE = EventDF_row.iloc[6]
        exon2ES = EventDF_row.iloc[7]
        exon2EE = EventDF_row.iloc[8]
        upstreamES = EventDF_row.iloc[9]
        upstreamEE = EventDF_row.iloc[10]
        downstreamES = EventDF_row.iloc[11]
        downstreamEE = EventDF_row.iloc[12]
        exclusion = str(upstreamEE) + "-" + str(exon2ES) + ":" + str(exon2EE) + "-" + str(downstreamES)

    
    elif type == "a3ss":
        longES = EventDF_row.iloc[5]
        longEE = EventDF_row.iloc[6]
        shortES = EventDF_row.iloc[7]
        shortEE = EventDF_row.iloc[8]
        flankingES = EventDF_row.iloc[9]
        flankingEE = EventDF_row.iloc[10]

        exclusion = str(flankingEE) + "-" + str(shortES)


    elif type == "a5ss":
        longES = EventDF_row.iloc[5]
        longEE = EventDF_row.iloc[6]
        shortES = EventDF_row.iloc[7]
        shortEE = EventDF_row.iloc[8]
        flankingES = EventDF_row.iloc[9]
        flankingEE = EventDF_row.iloc[10]

        exclusion = str(shortEE) + "-" + str(flankingES)

    
    return exclusion

def getID_specific(EventDF_row, type):
    ID = EventDF_row.loc["ID"]
    newID = type + "." + str(ID)
    return newID

def getInclusionID(EventDF_row, type):
    ID = EventDF_row.loc["ID"]
    newID = str(ID) + ".inc"
    return newID

def getExclusionID(EventDF_row, type):
    ID = EventDF_row.loc["ID"]
    newID = str(ID) + ".exc"
    return newID

############## LONG READ DATA READING ###################

def loadLRannot(gtfpath):
    # read in raw GTF, select columns that I want, return 
    # as long as gencode version is the same, i can merge ENSTs; but for novel transcripts, need to compare unique junction chains ** 
    # Where I left off before error thrown: need to make a superset of annotation from C1 and C2
    annot_raw = read_gtf(gtfpath)
    LRannot = annot_raw[["gene_id", "gene_name", "transcript_id", "feature", "seqname", "strand", "exon_number", "start", "end"]]
    return LRannot

def loadLRquant(tsvpath, count_column_name, condition_name):
    # quantpath_c1 = "/Volumes/sheynkman/projects/shay_thesis/data/EC-LR/long-read-EC-data/01_tsv/WTC11-1.tsv"
    # quantpath_c2 = "/Volumes/sheynkman/projects/shay_thesis/data/EC-LR/long-read-EC-data/01_tsv/EC.tsv"
    # count_column_name_c1 = "rep1ENCSR507JOF"
    # count_column_name_c2 = "rep1ENCSR148IIG"
    # loading the transcript quantification (for one condition)
    # included raw counts in output
    quant = pd.read_table(tsvpath)[["annot_transcript_id", count_column_name]]
    sumcounts = quant[count_column_name].sum()
    tpm_colname = "tpm_" + condition_name
    quant[tpm_colname] = quant.apply(lambda row: calcTPM(row, count_column_name, sumcounts), axis = 1)
    # quant = quant[["annot_transcript_id", tpm_colname]]
    quant = quant.rename(columns = {'annot_transcript_id':'transcript_id'})
    return quant

def calcTPM(quantrow, count_column_name, sumcounts):
    # Helper function to apply to each row of quantification file, referenced in loadLRquant
    tpm = ((quantrow[count_column_name]/sumcounts)*1000000)
    return tpm

def mergeAnnotQuants(LRannot, LRquant_c1, LRquant_c2):
    # merging annotation & quantification file on a left-join by transcript-id, as annotation contains more than just 
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
    
def getLRDict(mergedDF):
    # Overall goal: transcript table
    # Specific goal of this code: 
    grouped = mergedDF.groupby('transcript_id')
    ExonsDict = {}
    objectDictionary = {}
    for transcript_id, group in grouped:
        #initialize empty dict of exons
        #for each entry corresponding to an isoform
        for index, row in group.iterrows():
            #add all exons as lists to the dictionary
            if row.loc["feature"] == "exon":
                exon_number = int(row[6])
                start = row[7]
                stop = row[8]
                exonRange = [start, stop]
                ExonsDict[exon_number] = exonRange
            #making Transcript objects
            gene_id = row.loc["gene_id"]
            gene_name = row.loc["gene_name"]
            transcript_id = row.loc["transcript_id"]
            feature = row.loc["feature"]
            seqname = row.loc["seqname"]
            strand = row.loc["strand"]
            tpm_c1 = row.loc["tpm_WTC11"]
            tpm_c2 = row.loc["tpm_EC"]
            object = Transcript(gene_id, gene_name, transcript_id, feature, seqname, strand, tpm_c1, tpm_c2, ExonsDict)
        objectDictionary[object.UJC] = object
        # {chr|+|ENST|0:100 : TranscriptObject}
    #print(objectDictionary)
    return objectDictionary

# mergeannotquant = pd.read_csv("/Volumes/sheynkman/projects/shay_thesis/output/01_tmp/02_long-read-pandas/merge_nonzero_WASH7P.csv")
# getLRDict(mergeannotquant)
