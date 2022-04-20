#!/usr/bin/env python3

import argparse
from os import chdir
from os.path import abspath
from string import Template
from job_scripts import fmriprep_job_template
from subprocess import getstatusoutput as run_command

# Parse the input arguments
parser = argparse.ArgumentParser(
    description='Read subject IDs from a file and run fmriprep for each.'
)

parser.add_argument('-f', '--file', required=True,
    help="Path to the file that contains the subject IDs"
)

# Get input file with subjects listed one per line.  Save full path to the file
# as we will change directory before opening it.
inputs = parser.parse_args()
subj_list = abspath(inputs.file)


if __name__ == "__main__":

    # This is where job information is kept:  .sbat files, and the output file each
    # generates.
    chdir('job_info')
    with open(subj_list, 'r') as subs:
        # Confirm input file to user
        print(f"Using subjects listed in:  {inputs.file}\n")
        while True:
            subject = subs.readline().strip()
            if not subject:
                break
            sbat_file = subject + '.sbat'
            sbat = open(sbat_file, 'w')
            sbat.write(fmriprep_job_template.substitute(subject = subject))
            sbat.close()
            # Construct the sbatch command
            output_file = subject + '_fmriprep_output.txt'
            sbatch_command = f"sbatch -o {output_file} -e {output_file} {sbat_file}"
            submit_output = run_command(sbatch_command)
            print(f"    Submitted job to run fmriprep on {subject}")
            print(f"       {submit_output[1]}\n")
