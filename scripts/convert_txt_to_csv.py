"""
Script to loop over .txt files and extract the throughput data only.
Each .txt file is saved to corresponding .csv file.


Reading csv is done in a very rudimentary way, where the first 27 lines of the file are skipped and only 2 lines are read.
Code to read and extract the data taken (and altered) from:
https://www.bomberbot.com/python/converting-text-files-to-csv-using-python-pandas-a-comprehensive-guide-for-data-enthusiasts/

Extra help to remove whitespace from:
https://www.programiz.com/python-programming/pandas/methods/strip

Example of doing one file:

df = pd.read_csv('../snails/sysbench-results/results/btrfs-default_rndrd_0.txt', sep=':', skiprows=27, nrows=2, names=["Throughput", "value"])

df["Throughput"] = df["Throughput"].str.strip()

df.to_csv("test.csv", index=False)

"""

import pandas as pd

file_directory = "../snails/sysbench_backup/results_backup"
new_file_directory = "../snails/sysbench_backup/results_backup_csv"

setups = ["ext4-default", "ext4-tuned", "btrfs-default", "btrfs-tuned"]

# to match the filenames of the jsons
workloads = {"seqrd": "seqread",
             "rndrd": "randread",
             "seqwr": "seqwrite",
             "rndwr": "randwrite"}

for w in workloads:
    for s in setups:
        for rep in range(1, 31):

            # we need file operations value for the random tests
            if "rnd" in w:
                skip = 22
            else:
                skip = 25

            df = pd.read_csv(f"{file_directory}/{s}_{w}_{rep}.txt",
                             sep=":", skiprows=skip, nrows=2,
                             names=["Metric", "value"])

            df["Metric"] = df["Metric"].str.strip()

            df.to_csv(f"{new_file_directory}/{s}_{workloads[w]}_{rep}.csv", index=False)