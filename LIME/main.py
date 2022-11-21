import pandas as pd
from pathlib import Path
import click
from readData import *
from gtfparse import read_gtf


@click.command("load_data")
@click.option('--condition1', required = True, help = "specify name of condition 1")
@click.option('--condition2', required = True, help = "specify name of condition 2")
@click.option('--rmats_out_folder', required = True, type = click.Path(exists = True, path_type=Path), help = "Path to output of rMATS")
@click.option('-t', '--type', required = True, help = "specify whether using JC or JCEC read-based data from rMATS output")
@click.option('--c1_quantcol', required = True, help = 'name of condition 1 quantification.tsv column corresponding to condition 1 counts')
@click.option('--c2_quantcol', required = True, help = 'name of condition 2 quantification.tsv column corresponding to condition 2 counts')
@click.option('--c1annot', required = True, type = click.Path(exists = True, path_type=Path), help = "Path to long read annotation GTF for condition 1")
#@click.option('--c2annot', required = True, type = click.Path(exists = True, path_type=Path), help = "Path to long read annotation GTF for condition 2")
@click.option('--c1quant', required = True, type = click.Path(exists = True, path_type=Path), help = "Path to long read quantification TSV for condition 1")
@click.option('--c2quant', required = True, type = click.Path(exists = True, path_type=Path), help = "Path to long read quantification TSV for condition 2")
@click.option('-o', '--outputpath', type = click.Path(exists = True, path_type = Path), help = "Path to output. Default '.'")

def main(condition1: str, condition2: str, rmats_out_folder: Path, type: str, c1_quantcol: str, c2_quantcol: str, c1annot: Path, c1quant: Path, c2quant: Path, outputpath: Path):
    click.echo('')
    se = loadSE(rmats_out_folder, type)
    mxe = loadMXE(rmats_out_folder, type)
    a3ss = loadA3SS(rmats_out_folder, type)
    a5ss = loadA5SS(rmats_out_folder, type)

    lrannot = loadLRannot(c1annot)
    lrquant_c1 = loadLRquant(c1quant, c1_quantcol, condition1)
    lrquant_c2 = loadLRquant(c2quant, c2_quantcol, condition2)

    lr_alldata = mergeAnnotQuants(lrannot, lrquant_c1, lrquant_c2)

    #JunctionDict = getLRJunctionDict(lr_alldata) 
    # addJunctionsToTable(lr_alldata, JunctionDict)
    # map(lr_alldata, [se, mxe, a3ss, a5ss])
    
main()