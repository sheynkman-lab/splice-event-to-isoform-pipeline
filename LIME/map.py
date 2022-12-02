import pandas as pd
from LIME.readData import *
from LIME.TranscriptClass import *
import os

# returns simple dictionary of transcript_id --> mapDict
# should write a function to use this to create transcript-centric table & event-centric table


def mapper(objectDictionary, rmats, outputpath):
    df = pd.DataFrame(columns = ["gene_id", "gene_name", "strand", "rMATS_eventID", "rMATS_coord", "c1_rmats_psi", "c2_rmats_psi", "rmats_dpsi", "transcript_id", "long-read_UJC", "lr_tpm_c1", "lr_tpm_c2"])
    for lrUJC in objectDictionary.keys():
        tobj = objectDictionary[lrUJC]
        gene_id = tobj.gene_id #
        gene_name = tobj.gene_name #
        transcript_id = tobj.transcript_id #
        tpm_c1 = tobj.tpm_WTC11
        tpm_c2 = tobj.tpm_EC
        for index, eventRow in rmats.iterrows():
            if str(eventRow["incJunction"]) in lrUJC:
                # print("found event", str(eventRow["incID"]), "in", lrUJC)
                eventID = eventRow["incID"] #
                strand = eventRow["strand"] #
                coord = eventRow["incJunction"]
                c1_psi = eventRow["IncLevel1"]
                c2_psi = eventRow["IncLevel2"]
                dpsi = eventRow["IncLevelDifference"]
                row = [gene_id, gene_name, strand, eventID, coord, c1_psi, c2_psi, dpsi, transcript_id, lrUJC, tpm_c1, tpm_c2]
                df.loc[len(df)] = row
                # print(row)
            elif str(eventRow["excJunction"] in lrUJC):
                # print("found event", str(eventRow["excID"]), "in", lrUJC)
                eventID = eventRow["excID"]
                strand = eventRow["strand"]
                coord = eventRow["incJunction"]
                c1_psi = eventRow["IncLevel1"]
                c2_psi = eventRow["IncLevel2"]
                dpsi = eventRow["IncLevelDifference"]
                row = [gene_id, gene_name, strand, eventID, coord, c1_psi, c2_psi, dpsi, transcript_id, lrUJC, tpm_c1, tpm_c2]
                df.loc[len(df)] = row
                # print(row)
    print(df)
    # outputfile = str(outputpath) + "/mapping_LINC01128.csv"
    # df.to_csv(outputfile, index = False)
    return df

# mergeannotquants_LINC = pd.read_csv("/Volumes/sheynkman/projects/shay_thesis/output/01_tmp/02_long-read-pandas/mnzpLINC01128.csv")
# SELINC = pd.read_csv("/Volumes/sheynkman/projects/shay_thesis/output/01_tmp/01_short-read_pandas/SELINC.csv")
# objectDictionary = getLRDict(mergeannotquants_LINC)
# mapper(objectDictionary, SELINC, outputpath = "/Volumes/sheynkman/projects/shay_thesis/output")
