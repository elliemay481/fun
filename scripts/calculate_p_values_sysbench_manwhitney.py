import pandas as pd
from scipy.stats import mannwhitneyu

file_directory = "../../snails/sysbench_backup/results_backup_csv"

setups = ["ext4-default", "ext4-tuned", "btrfs-default", "btrfs-tuned"]
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

# load the raw per-rep results, same way as in the plotting script
# data[workload][setup] = list of 30 results
data = {}
for w in workloads:
    data[w] = {}
    for s in setups:
        data[w][s] = []
        for rep in range(1, 31):
            df = pd.read_csv(f"{file_directory}/{s}_{w}_{rep}.csv", usecols=["value"])

            if "read" in w:
                data[w][s].append(df["value"][0])   # the read value is the first row
            else:
                data[w][s].append(df["value"][1])   # the written value is the second row


def interpret_p_value(p_value, alpha=0.05):
    if p_value < alpha:
        return "Reject the null hypothesis. There is a statistically significant difference."
    else:
        return "Fail to reject the null hypothesis. There is no statistically significant difference."


def run_comparisons(comparisons):
    for workload in workloads:
        print("Results for workload:", workload)

        for setup1, setup2 in comparisons:
            x = data[workload][setup1]
            y = data[workload][setup2]

            # two-sided Mann-Whitney U test
            u_stat, p_value = mannwhitneyu(x, y, alternative="two-sided")
            result = interpret_p_value(p_value)

            print(workload, setup1, "vs", setup2, "p-value:", p_value)
            print(result)
            print("------------------------------------------")


print("Checking hypothesis 1: ext4 vs btrfs")
print("*****************************************")
run_comparisons(comparisons_hypothesis_1)

print(" ")
print(" -")

print("Checking hypothesis 2: default vs tuned")
print("*****************************************")
run_comparisons(comparisons_hypothesis_2)

print(" ")
print(" -")

print("Checking the others")
print("*****************************************")
run_comparisons(comparisons_the_others)