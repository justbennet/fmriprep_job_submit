# Sample fmriprep job submission scripts

Some Python script examples to submit multiple fmriprep jobs
from the Armis cluster run by ARC at the University of
Michigan.

These scripts were written using Python 3.7 and should run on
it and any newer versions.  They do use f-strings, but only
import from standard libraries.

Clone the repository to create a directory `job_submit`,
then change into it.

Modify each of the job script templates in the `job_scripts.py`
to have the correct information on these lines (14-15).

```
#SBATCH --account=support     # change to PH Slurm account
#SBATCH --partition=standard  # change to PH partition
```

The provided template has a placeholder `echo` command which
should be removed and replaced by any job-specific commands,
e.g., copying data to `/tmp`, removing it at the end of the
job, and by the actual `fmriprep` command.  Save the file.

To run as a test to make sure that all the job submission
parameters are right, change the account and partition, then

```
$ module load python
$ python3 submit_jobs.py --file subs.txt
```

That should create two files for each of `sub01` and `sub02`
in the `job_info` directory, the names of which should indicate
their contents.

```
$ ls job_info/sub*
job_info/sub01_fmriprep_output.txt  job_info/sub02_fmriprep_output.txt
job_info/sub01.sbat                 job_info/sub02.sbat
```
