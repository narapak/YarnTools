import sys
import argparse
import os

def isContainerStartLine(line):
    return line.startswith("Container: container_")

def setupOutputDir(dirname):
    os.mkdir(dirname)

def readArgs() :
    # Create the parser
    parser=argparse.ArgumentParser(description='Python program to parse yarn aggregated log file')

    # Add the arguments
    parser.add_argument('--infile', type=str, help='Input yarn aggregated log file.')
    parser.add_argument('--outdir', type=str, help='Output directory, where container log files are created.')

    # Parse the arguments
    args = parser.parse_args()
    
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit()
    
    return args


##### MAIN   ############

args=readArgs()

outputdir=str(args.outdir)
inputfile=str(args.infile)

setupOutputDir(outputdir)

outputfile=outputdir + '/' + "misc_container.txt"
outfd=open(outputfile,'a')

with open(inputfile, 'r') as f:
    # loop through the file, one line at a time
    for line in f:
        # Check whether line starts with Container string
        if isContainerStartLine(line):  
            containerName=line.split()[1]
            outfd.close()
            outputfile=outputdir + '/' + containerName
            outfd=open(outputfile,'a')
        
        outfd.write(line)
        
outfd.close()

