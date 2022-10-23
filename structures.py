import pandas as pd

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