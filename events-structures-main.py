import pandas as pd
# note: ISSUE LINE 62: rMATS IDs are only unique in local scope of event type!
# note: how do i define junction coordinates for retained intron? 

def main():
    # step 0: determine source of SR data
    srSource = "rmats"
    lrSource = "pacbio"

    #implement later: if statement for source event types, to accommodate variation
    eventTypes = ("se", "mxe", "ri", "a3ss", "a5ss")
    # init empty dictionary for tool
    eventDict = {}

    for eventType in eventTypes:
        filepath = "/Volumes/sheynkman/projects/shay_thesis/data/toy-rmats-maserproc/" + eventType + "Toy.csv"
        if eventType == "se":
            se = pd.read_csv(filepath, index_col = 0)
            
        elif eventType == "mxe":
            mxe = pd.read_csv(filepath, index_col = 0)
            
        elif eventType == "ri":
            ri = pd.read_csv(filepath, index_col = 0)
                    
        elif eventType == "a3ss":
            a3ss = pd.read_csv(filepath, index_col = 0)
            
        elif eventType == "a5ss":
            a5ss = pd.read_csv(filepath, index_col = 0)

        else:
            print("Error: event type not registered")

    #THIS IS INEFFICIENT; JUST TESTING IF IT WORKS! 
    #eventDict = makeEvents(se, srSource, "se", eventDict)
    #eventDict = makeEvents(mxe, srSource, "mxe", eventDict)

##    for eventType in eventTypes:
##        eventDict = makeEvents(eval(eventType), srSource, eventType, eventDict)
    eventDict = makeEvents(se, srSource, "se", eventDict)
    eventDict = makeEvents(mxe, srSource, "mxe", eventDict)
    eventDict = makeEvents(ri, srSource, "ri", eventDict)
    eventDict = makeEvents(a3ss, srSource, "a3ss", eventDict)
    eventDict = makeEvents(a5ss, srSource, "a5ss", eventDict)
    #print(eventDict)
    #print(len(eventDict))

##    Looping thru event maker function
##    for eventType in eventTypes:
##        makeEvents(eventType, srSource, eventType, eventDict)
                
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

    


### ________ CLASSES ___________
    
class Event():
    def __init__(self, source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand):
        self.source = source
        self.eventType = eventType
        self.eventid = str(self.eventType) + "." + str(eventid)
        self.ensg = ensg
        self.gene = gene
        self.pvalue = pvalue
        self.fdr = fdr
        self.dpsi = dpsi
        self.chrom = chrom
        self.strand = strand

    def __str__(self):
        return f"Event ID: {self.eventid} (Gene: {self.gene})" 

class SE(Event):
    def __init__(self, source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand, target, upstream, downstream):
        super().__init__(source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand)
        self.target = target
        self.upstream = upstream
        self.downstream = downstream
        self.incjunction = SE.inclusionJunctionString(self)
        self.excjunction = SE.exclusionJunctionString(self)

    def __str__(self):
        return super(SE, self).__str__()

    def inclusionJunctionString(self):
        #print("target for exon" + self.eventid + " " + self.target)
        targetList = self.target.split("-")
        upstreamList = self.upstream.split("-")
        downstreamList = self.downstream.split("-")
        inclusion = upstreamList[1] + "-" + targetList[0] + ":" + targetList[1] + "-" + downstreamList[0]
        return(inclusion)

    def exclusionJunctionString(self):
        #print("target for exon" + self.eventid + " " + self.target)
        upstreamList = self.upstream.split("-")
        downstreamList = self.downstream.split("-")
        exclusion = upstreamList[1] + "-" + downstreamList[0]
        return(exclusion)
        

class MXE(Event):
    def __init__(self, source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand, exon1, exon2, upstream, downstream):
        super().__init__(source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand)
        self.exon1 = exon1
        self.exon2 = exon2
        self.upstream = upstream
        self.downstream = downstream
        self.incjunction = MXE.inclusionJunctionString(self)
        self.excjunction = MXE.exclusionJunctionString(self)

    def __str__(self):
        return super(MXE, self).__str__()

    def inclusionJunctionString(self):
        upstreamList = self.upstream.split("-")
        downstreamList = self.downstream.split("-")
        exon1List = self.exon1.split("-")
        inclusion = upstreamList[1] + "-" + exon1List[0] + ":" + exon1List[1] + "-" + downstreamList[0]
        return(inclusion)
    
    def exclusionJunctionString(self):
        upstreamList = self.upstream.split("-")
        downstreamList = self.downstream.split("-")
        exon2List = self.exon2.split("-")
        exclusion = upstreamList[1] + "-" + exon2List[0] + ":" + exon2List[1] + "-" + downstreamList[0]
        return(exclusion)

class RI(Event):
    def __init__(self, source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand, exonir, upstream, downstream):
        super().__init__(source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand)
        self.exonir = exonir
        self.upstream = upstream
        self.downstream = downstream
        self.incjunction = RI.inclusionJunctionString(self)
        self.excjunction = RI.exclusionJunctionString(self)
        
    def __str__(self):
        return super(RI, self).__str__()

    def inclusionJunctionString(self):
        exonirList = self.exonir.split("-")
        upstreamList = self.upstream.split("-")
        downstreamList = self.downstream.split("-")
        inclusion = "not sure what to include here, since there's no junction"
        return(inclusion)
    
    def exclusionJunctionString(self):
        exonirList = self.exonir.split("-")
        upstreamList = self.upstream.split("-")
        downstreamList = self.downstream.split("-")
        exclusion = upstreamList[1] + "-" + downstreamList[0]
        return(exclusion)


class A3SS(Event):
    def __init__(self, source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand, exonlong, exonshort, exonflanking):
        super().__init__(source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand)
        self.exonlong = exonlong
        self.exonshort = exonshort
        self.exonflanking = exonflanking
        self.incjunction = A3SS.inclusionJunctionString(self)
        self.excjunction = A3SS.exclusionJunctionString(self)
    
    def __str__(self):
        return super(A3SS, self).__str__()

    def inclusionJunctionString(self):
        exonlongList = self.exonlong.split("-")
        exonshortList = self.exonshort.split("-")
        exonflankingList = self.exonflanking.split("-")
        inclusion = "emptstring"
        
        return(inclusion)

    ##finish
    def exclusionJunctionString(self):
        exclusion = "emptstring"
        return(exclusion)    

class A5SS(Event):
    def __init__(self, source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand, exonlong, exonshort, exonflanking):
        super().__init__(source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand)
        self.exonlong = exonlong
        self.exonshort = exonshort
        self.exonflanking = exonflanking
        self.incjunction = A5SS.inclusionJunctionString(self)
        self.excjunction = A5SS.exclusionJunctionString(self)

    def __str__(self):
        return super(A5SS, self).__str__()

    ##finish
    def inclusionJunctionString(self):
        inclusion = "emptstring"
        return(inclusion)
    ##finish
    def exclusionJunctionString(self):
        exclusion = "emptstring"
        return(exclusion)

main()