import pandas as pd
from structures import *
from getTranscripts import *
import os
from gtfparse import read_gtf

def getEvents(df, source, eventType, eventDict):
    #eventDict should be an empty dictionary...
    eventTypes = ("se", "mxe", "a3ss", "a5ss")

##  make sure event type is real
    if eventType not in eventTypes:
        print("error: invalid event type")
        return

    for i in range(len(df)):
##      make an event out of each row
##      source = rMATS, etc etc... in main() it's srSource = "rmats"
##      eventType = eventType
        eventid = df.iloc[i, 0]
        ensg = df.iloc[i, 1]
        gene = df.iloc[i, 2]
        chrom = df.iloc[i, 3]
        strand = df.iloc[i, 4]

        if eventType == "se":
            pvalue = df.iloc[i, 18]
            fdr = df.iloc[i, 19]
            dpsi = df.iloc[i, 22]
            targetES = df.iloc[i, 5]
            targetEE = df.iloc[i, 6]
            upstreamES = df.iloc[i, 7]
            upstreamEE = df.iloc[i, 8]
            downstreamES = df.iloc[i, 9]
            downstreamEE = df.iloc[i, 10]
            newEvent = SE(source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand, targetES, targetEE, upstreamES, upstreamEE, downstreamES, downstreamEE)
            eventDict[eventid] = newEvent
            
        elif eventType == "mxe":
            pvalue = df.iloc[i, 20]
            fdr = df.iloc[i, 21]
            dpsi = df.iloc[i, 24]
            exon1ES = df.iloc[i, 5]
            exon1EE = df.iloc[i, 6]
            exon2ES = df.iloc[i, 7]
            exon2EE = df.iloc[i, 8]
            upstreamES = df.iloc[i, 9]
            upstreamEE = df.iloc[i, 10]
            downstreamES = df.iloc[i, 11]
            downstreamEE = df.iloc[i, 12]
            newEvent = MXE(source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand, exon1ES, exon1EE, exon2ES, exon2EE, upstreamES, upstreamEE, downstreamES, downstreamEE)
            eventDict[eventid] = newEvent
            
        elif eventType == "a3ss":
            pvalue = df.iloc[i, 18]
            fdr = df.iloc[i, 19]
            dpsi = df.iloc[i, 22]
            longES = df.iloc[i, 5]
            longEE = df.iloc[i, 6]
            shortES = df.iloc[i, 7]
            shortEE = df.iloc[i, 8]
            flankingES = df.iloc[i, 9]
            flankingEE = df.iloc[i, 10]
            newEvent = A3SS(source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand, longES, longEE, shortES, shortEE, flankingES, flankingEE) 
            eventDict[eventid] = newEvent
            
        elif eventType == "a5ss":
            pvalue = df.iloc[i, 18]
            fdr = df.iloc[i, 19]
            dpsi = df.iloc[i, 22]
            longES = df.iloc[i, 5]
            longEE = df.iloc[i, 6]
            shortES = df.iloc[i, 7]
            shortEE = df.iloc[i, 8]
            flankingES = df.iloc[i, 9]
            flankingEE = df.iloc[i, 10]
            newEvent = A5SS(source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand, longES, longEE, shortES, shortEE, flankingES, flankingEE)
            eventDict[eventid] = newEvent
            
    return eventDict