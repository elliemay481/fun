import csv
import numpy as np
from scipy.stats import t
import pandas as pd

workloads = ["seqread", "randread", "seqwrite", "randwrite"]

# pairs of setups to compare
comparisons_hypothesis_1 = [
    ("ext4-default", "btrfs-default"),
    ("ext4-tuned", "btrfs-tuned"),
]

comparisons_hypothesis_2 = [
    ("ext4-default", "ext4-tuned"),
    ("btrfs-default", "btrfs-tuned"),
]

comparisons_the_others = [
    ("btrfs-default", "ext4-tuned"),
    ("ext4-default", "btrfs-tuned"),
]

# load the statistics calcluated earlier
summary = pd.read_csv("../results/summary_all_workloads_sysbench_backup.csv")
# turn csv into a dict using help from:
# https://www.reddit.com/r/learnpython/comments/mf6dwl/creating_a_dictionary_from_a_csv_file/
summary_dict = summary.to_dict("records")

# Step 1: Calculate the T-score
# Function based on: https://www.geeksforgeeks.org/machine-learning/how-to-find-a-p-value-from-a-t-score-in-python/ä
# But changed to use our statistics
def calculate_t_score(stats1, stats2):
    mean1 = stats1["mean"]
    mean2 = stats2["mean"]
    n1 = stats1["n"]
    n2 = stats2["n"]
    std1 = stats1["SD"] * np.sqrt(n1 / (n1 - 1))
    std2 = stats2["SD"] * np.sqrt(n2 / (n2 - 1))

    t_score = (mean1 - mean2) / np.sqrt((std1**2 / n1) + (std2**2 / n2))
    return t_score

# Step 2: Determine the degrees of freedom (df)
# Function source: https://www.geeksforgeeks.org/machine-learning/how-to-find-a-p-value-from-a-t-score-in-python/
def calculate_degrees_of_freedom(stats1, stats2):
    n1 = stats1["n"]
    n2 = stats2["n"]
    df = n1 + n2 - 2  # For a two-sample t-test
    return df


# Step 3: Identify the appropriate t-distribution
# (The scipy.stats.t distribution is used, which automatically considers the degrees of freedom)
# Source: https://www.geeksforgeeks.org/machine-learning/how-to-find-a-p-value-from-a-t-score-in-python/

# Step 4: Find the p-value
# Source: https://www.geeksforgeeks.org/machine-learning/how-to-find-a-p-value-from-a-t-score-in-python/
def calculate_p_value(t_score, df):
    p_value = 2 * (1 - t.cdf(np.abs(t_score), df))
    return p_value

# Step 5: Interpret the p-value
def interpret_p_value(p_value, alpha=0.05):
    if p_value < alpha:
        return "Reject the null hypothesis. There is a statistically significant difference."
    else:
        return "Fail to reject the null hypothesis. There is no statistically significant difference."
    
print("Checking hypothesis 1: ext4 vs btrfs")
print("*****************************************")
for workload in workloads:
    print("Results for workload:", workload)

    for setup1, setup2 in comparisons_hypothesis_1:

        for row in summary_dict:
            if row["workload"] == workload:
                if row["setup"] == setup1:
                    stats1 = row
                if row["setup"] == setup2:
                    stats2 = row


        t_score = calculate_t_score(stats1, stats2)
        df = calculate_degrees_of_freedom(stats1, stats2)
        p_value = calculate_p_value(t_score, df)
        result = interpret_p_value(p_value)

        print(workload, setup1, "vs", setup2, "p-value:", p_value)
        print(result)
    print("------------------------------------------")

print(" ")
print(" -")

print("Checking hypothesis 2: default vs tuned")
print("*****************************************")
for workload in workloads:
    print("Results for workload:", workload)
    rows = summary[summary["workload"] == workload]

    for setup1, setup2 in comparisons_hypothesis_2:

        for row in summary_dict:
            if row["workload"] == workload:
                if row["setup"] == setup1:
                    stats1 = row
                if row["setup"] == setup2:
                    stats2 = row

        t_score = calculate_t_score(stats1, stats2)
        df = calculate_degrees_of_freedom(stats1, stats2)
        p_value = calculate_p_value(t_score, df)
        result = interpret_p_value(p_value)

        print(workload, setup1, "vs", setup2, "p-value:", p_value)
        print(result)
    print("------------------------------------------")


print(" ")
print(" -")

print("Checking the other ones")
print("*****************************************")
for workload in workloads:
    print("Results for workload:", workload)
    rows = summary[summary["workload"] == workload]

    for setup1, setup2 in comparisons_the_others:

        for row in summary_dict:
            if row["workload"] == workload:
                if row["setup"] == setup1:
                    stats1 = row
                if row["setup"] == setup2:
                    stats2 = row

        t_score = calculate_t_score(stats1, stats2)
        df = calculate_degrees_of_freedom(stats1, stats2)
        p_value = calculate_p_value(t_score, df)
        result = interpret_p_value(p_value)

        print(workload, setup1, "vs", setup2, "p-value:", p_value)
        print(result)
    print("------------------------------------------")