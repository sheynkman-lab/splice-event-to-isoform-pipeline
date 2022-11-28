import pandas as pd
from archive.map import *
from archive.getEvents import *
from archive.structures import *
from LIME.getTranscripts import *
from archive.getEvents import *
from archive.convertToTable import *
from LIME.readData import *
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

    print("loading SE")
    se = loadSE(rmatsPath, type)
    print("SE loaded. loading MXE")
    mxe = loadMXE(rmatsPath, type)
    print("MXE loaded. loading A3SS")
    a3ss = loadA3SS(rmatsPath, type)
    print("A3SS loaded. loading A5SS")
    a5ss = loadA5SS(rmatsPath, type)
    print("A5SS loaded")

    #eventDict = getEvents(se, srSource, "se", eventDict)
    #eventDict = getEvents(mxe, srSource, "mxe", eventDict)
    #eventDict = getEvents(a3ss, srSource, "a3ss", eventDict)
    #eventDict = getEvents(a5ss, srSource, "a5ss", eventDict)
    print("chr19 events, SE")
    eventDict = getEventsByChr(se, srSource, "chr19", "se", eventDict)
    print("chr19 events, MXE")
    eventDict = getEventsByChr(mxe, srSource, "chr19", "mxe", eventDict)
    print("chr19 events, A3SS")
    eventDict = getEventsByChr(a3ss, srSource, "chr19", "a3ss", eventDict)
    print("chr19 events, A5SS")
    eventDict = getEventsByChr(a5ss, srSource, "chr19", "a5ss", eventDict)
    print("loading eventTable")
    eventTableChr19 = EventDictToTable(eventDict)
    print("eventTable loaded")

    #eventTable.to_csv("/Volumes/sheynkman/projects/shay_thesis/output/rmats_events_chr19.csv")
    filepath = "/Volumes/sheynkman/projects/shay_thesis/data/chr19-lr-proc/EC-transcript-annotation.csv"
    transcriptDict = getTranscripts(filepath)
    transcriptTable = TranscriptDictToTable(transcriptDict)
    
    mapTable = mappingEventsToTranscripts(eventTableChr19, transcriptTable)
    #outputpath = "/Volumes/sheynkman/projects/shay_thesis/output/mapping_test_1.csv"
    #mapTable.to_csv(outputpath)

#main()
