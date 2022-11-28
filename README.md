# Welcome to LIME (Long-read Isoform Mapping to (alternative splicing) Events)
**Contents**

- [Data](#data)
- [Instructions](#instructions)

## Data
### Files and folders needed to run LIME** 
#### rMATS output
- Output folder of rMATS
#### Long-read RNA sequencing data corresponding to conditions compared in rMATS
- Condition 1
    - Annotation file: .gtf
    - Transcript quantification file: .tsv
        - Note: examine .tsv file to identify the name of the column containing transcript raw count data
- Condition 2
    - Transcript quantification file: .tsv

## Instructions
### The following parameters are necessary to run LIME
``` 
  --condition1 TEXT        Name of condition 1
  --condition2 TEXT        Name of condition 2
  --rmats_out_folder PATH  Path to output of rMATS
  -t, --type TEXT          specify whether using JC or JCEC read-based data
                           from rMATS output (to do: update this to be a selector option)
  --c1_quantcol TEXT       name of condition 1 quantification.tsv column
                           corresponding to condition 1 counts
  --c2_quantcol TEXT       name of condition 2 quantification.tsv column
                           corresponding to condition 2 counts
  --c1annot PATH           Path to long read annotation GTF for condition 1
  --c1quant PATH           Path to long read quantification TSV for condition
                           1
  --c2quant PATH           Path to long read quantification TSV for condition
                           2
  -o, --outputpath PATH    Path to output
``` 
For a list of commands, run lime --help

### Run process
#### Step 0: Navigate to main repository folder (should be named splice-event-to-isoform-pipeline)
#### Step 1: Ensure you have the python packages Click, gtfparse, and pandas installed. If necessary, create a conda environment and activate using the following command:
``` conda activate LIME ```
#### Step 2: Run the following command to install LIME:
``` pip install --editable . ```
#### run LIME with the following command line prompt
``` lime --condition1 --condition2 --rmats_out_folder --type --c1_quantcol --c2_quantcol --c1annot --c1quant --c2quant --outputpath ```

> For Gloria: run.sh has the lime command line prompt configured with paths to the tester input files in project storage. Please run the following command in your terminal after cloning the repository and navigating to the main folder splice-event-to-isoform-pipeline in Terminal:
``` bash run.sh ```

