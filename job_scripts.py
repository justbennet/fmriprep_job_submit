from string import Template

fmriprep_job_template = Template(f'''#!/bin/bash

#----------- Begin preamble -----------#

#SBATCH --job-name=sub01_fmriprep
#SBATCH --time=05:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=20gb            # 5 * cpus-per-task minimum

#SBATCH --account=support     # change to PH Slurm account
#SBATCH --partition=standard  # change to PH partition

#-----------  End preamble  -----------#

module purge
module load singularity
my_job_header

#-----------   Begin work   -----------#

echo "I would have run fmriprep [bunch of options] here if this were real"

#-----------    End work    -----------#

''')
