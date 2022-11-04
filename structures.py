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
    def __init__(self, source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand, targetES, targetEE, upstreamES, upstreamEE, downstreamES, downstreamEE):
        super().__init__(source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand)
        self.targetES = targetES
        self.targetEE = targetEE
        self.upstreamES = upstreamES
        self.upstreamEE = upstreamEE
        self.downstreamES = downstreamES
        self.downstreamEE = downstreamEE
        self.incjunction = SE.inclusionJunctionString(self)
        self.excjunction = SE.exclusionJunctionString(self)
        self.incid = self.eventid + ".inc"
        self.excid = self.eventid + ".exc"
        self.row = SE.rowDict(self)


    def rowDict(self):
        row = {"source": self.source, "eventType":self.eventType, "eventid":self.eventid, "ensg":self.ensg, "gene": self.gene, "pvalue":self.pvalue, "fdr":self.fdr, "dpsi":self.dpsi, "chrom":self.chrom, "strand":self.strand, "incjunction" : self.incjunction, "excjunction":self.excjunction, "incid":self.incid, "excid":self.excid}
        return row

    def __str__(self):
        return super(SE, self).__str__()

    def inclusionJunctionString(self):
        inclusion = self.upstreamEE + "-" + self.targetES + ":" + self.targetEE + "-" + self.downstreamES
        return(inclusion)

    def exclusionJunctionString(self):
        #print("target for exon" + self.eventid + " " + self.target)
        exclusion = self.upstreamEE + ":" + self.downstreamES
        return(exclusion)
        

### MXE CLASS

class MXE(Event):
    def __init__(self, source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand, exon1ES, exon1EE, exon2ES, exon2EE, upstreamES, upstreamEE, downstreamES, downstreamEE):
        super().__init__(source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand)
        self.exon1ES = exon1ES
        self.exon1EE = exon1EE
        self.exon2ES = exon2ES
        self.exon2EE = exon2EE
        self.upstreamES = upstreamES
        self.upstreamEE = upstreamEE
        self.downstreamES = downstreamES
        self.downstreamEE = downstreamEE
        self.incjunction = MXE.inclusionJunctionString(self)
        self.excjunction = MXE.exclusionJunctionString(self)
        self.incid = self.eventid + ".inc"
        self.excid = self.eventid + ".exc"
        self.row = MXE.rowDict(self)


    def rowDict(self):
        row = {"source": self.source, "eventType":self.eventType, "eventid":self.eventid, "ensg":self.ensg, "gene": self.gene, "pvalue":self.pvalue, "fdr":self.fdr, "dpsi":self.dpsi, "chrom":self.chrom, "strand":self.strand, "incjunction" : self.incjunction, "excjunction":self.excjunction, "incid":self.incid, "excid":self.excid}
        return row
        

    def __str__(self):
        return super(MXE, self).__str__()

    def inclusionJunctionString(self):
        inclusion = self.upstreamEE + "-" + self.exon1ES + ":" + self.exon1EE + "-" + self.downstreamES
        return(inclusion)
    
    def exclusionJunctionString(self):
        exclusion = self.upstreamEE + "-" + self.exon2ES + ":" + self.exon2EE + "-" + self.downstreamES
        return(exclusion)


### A3SS CLASS

class A3SS(Event):

    def __init__(self, source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand, longES, longEE, shortES, shortEE, flankingES, flankingEE):
        super().__init__(source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand)
        self.longES = longES
        self.longEE = longEE
        self.shortES = shortES
        self.shortEE = shortEE
        self.flankingES = flankingES
        self.flankingEE = flankingEE
        self.incjunction = A3SS.inclusionJunctionString(self)
        self.excjunction = A3SS.exclusionJunctionString(self)
        self.incid = self.eventid + ".inc"
        self.excid = self.eventid + ".exc"
        self.row = A3SS.rowDict(self)


    def rowDict(self):
        row = {"source": self.source, "eventType":self.eventType, "eventid":self.eventid, "ensg":self.ensg, "gene": self.gene, "pvalue":self.pvalue, "fdr":self.fdr, "dpsi":self.dpsi, "chrom":self.chrom, "strand":self.strand, "incjunction" : self.incjunction, "excjunction":self.excjunction, "incid":self.incid, "excid":self.excid}
        return row
    
    def __str__(self):
        return super(A3SS, self).__str__()

    def inclusionJunctionString(self):
        inclusion = self.flankingEE + "-" + self.longES
        return(inclusion)

    def exclusionJunctionString(self):
        exclusion = self.flankingEE + "-" + self.shortES
        return(exclusion)

### A5SS CLASS

class A5SS(Event):
    def __init__(self, source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand, longES, longEE, shortES, shortEE, flankingES, flankingEE):
        super().__init__(source, eventType, eventid, ensg, gene, pvalue, fdr, dpsi, chrom, strand)
        self.longES = longES
        self.longEE = longEE
        self.shortES = shortES
        self.shortEE = shortEE
        self.flankingES = flankingES
        self.flankingEE = flankingEE
        self.incjunction = A5SS.inclusionJunctionString(self)
        self.excjunction = A5SS.exclusionJunctionString(self)
        self.incid = self.eventid + ".inc"
        self.excid = self.eventid + ".exc"
        self.row = A5SS.rowDict(self)


    def rowDict(self):
        row = {"source": self.source, "eventType":self.eventType, "eventid":self.eventid, "ensg":self.ensg, "gene": self.gene, "pvalue":self.pvalue, "fdr":self.fdr, "dpsi":self.dpsi, "chrom":self.chrom, "strand":self.strand, "incjunction" : self.incjunction, "excjunction":self.excjunction, "incid":self.incid, "excid":self.excid}
        return row

    def __str__(self):
        return super(A5SS, self).__str__()

    def inclusionJunctionString(self):
        inclusion = self.longEE + "-" + self.flankingES
        return(inclusion)

    def exclusionJunctionString(self):
        exclusion = self.shortEE + "-" + self.flankingES
        return(exclusion)

### QUICK ISOFORM CLASSES

class Transcript():
    def __init__(self, transcript_id, ExonsDict, gene_name, gene_id):
        self.transcript_id = transcript_id
        self.ExonsDict = ExonsDict
        self.gene_name = gene_name
        self.gene_id = gene_id
        self.junctionString = Transcript.makeJunctionString(self)
        self.row = Transcript.rowDict(self)
    
    def __str__(self):
        printstring = self.transcript_id + " --> " + self.junctionString
        return(printstring)


    def rowDict(self):
        row = {"transcript_id" : self.transcript_id, "ExonsDict":self.ExonsDict, "gene_name":self.gene_name, "gene_id":self.gene_id, "junctionString":self.junctionString}
        return row

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
            
