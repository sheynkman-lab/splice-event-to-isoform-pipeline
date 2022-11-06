import pandas as pd
from map import *
from getEvents import *
from structures import *
from getTranscripts import *
from getEvents import *
from convertToTable import *
from readData import *
import os
from gtfparse import read_gtf

def main():
    # step 0: determine source of SR data
    srSource = "rmats"
    lrSource = "pacbio"
    rmatsPath = "/Volumes/sheynkman/projects/EC_stem_cell_differentiation/001_ips-s1s2/003_ips-s1s2_output/002_ips-s1s2_rmats-out"
    type = "JCEC"

    #implement later: if statement for source event types, to accommodate variation
    eventTypes = ("se", "mxe", "a3ss", "a5ss")
    # init empty dictionary for tool
    eventDict = {}

    se = loadSE(rmatsPath, type)
    mxe = loadMXE(rmatsPath, type)
    a3ss = loadA3SS(rmatsPath, type)
    a5ss = loadA5SS(rmatsPath, type)


    eventDict = getEvents(se, srSource, "se", eventDict)
    #eventDict = getEvents(mxe, srSource, "mxe", eventDict)
    #eventDict = getEvents(a3ss, srSource, "a3ss", eventDict)
    #eventDict = getEvents(a5ss, srSource, "a5ss", eventDict)
    eventTable = EventDictToTable(eventDict)
    
    filepath = "/Volumes/sheynkman/projects/shay_thesis/data/chr19-lr-proc/EC-transcript-annotation.csv"
    #transcriptDict = getTranscripts(filepath)
    #transcriptTable = TranscriptDictToTable(transcriptDict)
    
    #mapTable = mappingEventsToTranscripts(eventTable, transcriptTable)
    #outputpath = "/Volumes/sheynkman/projects/shay_thesis/output/mapping_test_1.csv"
    #mapTable.to_csv(outputpath)

main()
