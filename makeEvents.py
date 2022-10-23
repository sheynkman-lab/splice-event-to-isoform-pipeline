import pandas as pd
# note: ISSUE LINE 62: rMATS IDs are only unique in local scope of event type!
# note: how do i define junction coordinates for retained intron? 
                
def makeEvents(df, source, eventType, eventDict):
    #eventDict should be an empty dictionary...
    eventTypes = ("se", "mxe", "ri", "a3ss", "a5ss")

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
        pvalue = df.iloc[i, 3]
        fdr = df.iloc[i, 4]
        dpsi = df.iloc[i, 5]
        chrom = df.iloc[i, 8] # skipping rows 6 and 7, which are lists of PSI values for conditions 1 and 2 respectively
        strand = df.iloc[i, 9]

        if eventType == "se":
            target = df.iloc[i, 10]
            upstream = df.iloc[i, 11]
            downstream = df.iloc[i, 12]
            newEvent = SE(source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand, target, upstream, downstream)
            eventDict[eventid] = newEvent
            
        elif eventType == "mxe":
            exon1 = df.iloc[i, 10]
            exon2 = df.iloc[i, 11]
            upstream = df.iloc[i, 12]
            downstream = df.iloc[i, 13]
            newEvent = MXE(source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand, exon1, exon2, upstream, downstream)
            eventDict[eventid] = newEvent
            
        elif eventType == "ri":
            exonir = df.iloc[i, 10]
            upstream = df.iloc[i, 11]
            downstream = df.iloc[i, 12]
            newEvent = RI(source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand, exonir, upstream, downstream)
            eventDict[eventid] = newEvent
            
        elif eventType == "a3ss":
            exonlong = df.iloc[i, 10]
            exonshort = df.iloc[i, 11]
            exonflanking = df.iloc[i, 12]
            newEvent = A3SS(source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand, exonlong, exonshort, exonflanking)
            eventDict[eventid] = newEvent
            
        elif eventType == "a5ss":
            exonlong = df.iloc[i, 10]
            exonshort = df.iloc[i, 11]
            exonflanking = df.iloc[i, 12]
            newEvent = A5SS(source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand, exonlong, exonshort, exonflanking)
            eventDict[eventid] = newEvent
            
    return eventDict
