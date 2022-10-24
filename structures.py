from tabnanny import NannyNag
import pandas as pd

### ________ CLASSES ___________
    

### EVENT CLASS

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

### SE CLASS

class SE(Event):
    def __init__(self, source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand, target, upstream, downstream):
        super().__init__(source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand)
        self.target = target
        self.upstream = upstream
        self.downstream = downstream
        self.incjunction = SE.inclusionJunctionString(self)
        self.excjunction = SE.exclusionJunctionString(self)
        self.incid = self.eventid + ".inc"
        self.excid = self.eventid + ".exc"

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
        

### MXE CLASS

class MXE(Event):
    def __init__(self, source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand, exon1, exon2, upstream, downstream):
        super().__init__(source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand)
        self.exon1 = exon1
        self.exon2 = exon2
        self.upstream = upstream
        self.downstream = downstream
        self.incjunction = MXE.inclusionJunctionString(self)
        self.excjunction = MXE.exclusionJunctionString(self)
        self.incid = self.eventid + ".inc"
        self.excid = self.eventid + ".exc"
        

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


### A3SS CLASS

class A3SS(Event):

    def __init__(self, source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand, exonlong, exonshort, exonflanking):
        super().__init__(source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand)
        self.exonlong = exonlong
        self.exonshort = exonshort
        self.exonflanking = exonflanking
        self.incjunction = A3SS.inclusionJunctionString(self)
        self.excjunction = A3SS.exclusionJunctionString(self)
        self.incid = self.eventid + ".inc"
        self.excid = self.eventid + ".exc"
    
    def __str__(self):
        return super(A3SS, self).__str__()

    def inclusionJunctionString(self):
        exonlongList = self.exonlong.split("-")
        exonflankingList = self.exonflanking.split("-")
        inclusion = exonflankingList[1] + "-" + exonlongList[0]
        return(inclusion)

    def exclusionJunctionString(self):
        exonshortList = self.exonshort.split("-")
        exonflankingList = self.exonflanking.split("-")
        exclusion = exonflankingList[1] + "-" + exonshortList[0]
        return(exclusion)

### A5SS CLASS

class A5SS(Event):
    def __init__(self, source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand, exonlong, exonshort, exonflanking):
        super().__init__(source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand)
        self.exonlong = exonlong
        self.exonshort = exonshort
        self.exonflanking = exonflanking
        self.incjunction = A5SS.inclusionJunctionString(self)
        self.excjunction = A5SS.exclusionJunctionString(self)
        self.incid = self.eventid + ".inc"
        self.excid = self.eventid + ".exc"

    def __str__(self):
        return super(A5SS, self).__str__()

    def inclusionJunctionString(self):
        exonlongList = self.exonlong.split("-")
        exonflankingList = self.exonflanking.split("-")
        inclusion = exonlongList[1] + "-" + exonflankingList[0]
        return(inclusion)

    def exclusionJunctionString(self):
        exonshortList = self.exonshort.split("-")
        exonflankingList = self.exonflanking.split("-")
        exclusion = exonshortList[1] + "-" + exonflankingList[0]
        return(exclusion)

### QUICK ISOFORM CLASSES

class Transcript():
    def __init__(self, transcript_id, ExonsDict):
        self.transcript_id = transcript_id
        self.ExonsDict = ExonsDict
        self.junctionString = Transcript.makeJunctionString(self)
    
    def __str__(self):
        printstring = self.transcript_id + " --> " + self.junctionString
        return(printstring)

    def makeJunctionString(self):
        #ExonsDict = {1: [70928, 70945], 2: [66346, 66499]}
        junctionString = ""
        for i in self.ExonsDict:
            if i+1 in self.ExonsDict:
                exon = self.ExonsDict[i]
                next_exon = self.ExonsDict[i+1]
                junction = str(exon[1]) + "-" + str(next_exon[0])
                junctionString = junctionString + junction + ":"
        return junctionString
            
