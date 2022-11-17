import pandas as pd
from archive.getEvents import *
from archive.structures import *
from getTranscripts import *
from archive.getEvents import *
import os
from gtfparse import read_gtf

def EventDictToTable(eventDict):
    eventTable = pd.DataFrame()
    for event_id in eventDict:
        tmp = eventDict[event_id]
        ser = pd.Series(tmp.row)
        eventTable = pd.concat([eventTable, ser.to_frame().T], ignore_index = True)
    #print(eventTable)
    return eventTable

def TranscriptDictToTable(transcriptDict):
    transcriptTable = pd.DataFrame()
    for transcript_id in transcriptDict:
        tmp = transcriptDict[transcript_id]
        ser = pd.Series(tmp.row)
        transcriptTable = pd.concat([transcriptTable, ser.to_frame().T], ignore_index = True)
    #print(transcriptTable)
    return transcriptTable