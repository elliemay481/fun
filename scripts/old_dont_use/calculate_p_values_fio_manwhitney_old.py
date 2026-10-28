import json
from scipy.stats import mannwhitneyu

# results taken from the json files
# dictionary for each worload
file_directory = "../../snails/fio_results/results"

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

# extract the data we want from the results and store in a dictionary
# a dictionary entry looks like: data[workload][setup] = result
# e.g. data["seqread"]["ext4-default"] = [500, 490, ...]
data = {}
for w in workloads:
    data[w] = {}
    for s in setups:
        data[w][s] = []
        for rep in range(1, 31):
            with open(f"{file_directory}/{s}_{w}_{rep}.json") as f:
                job = json.load(f)["jobs"][0]
            if "rand" in w:
                if "read" in w:
                    data[w][s].append(job["read"]["iops"])
                if "write" in w:
                    data[w][s].append(job["write"]["iops"])
            else:
                if "read" in w:
                    data[w][s].append(job["read"]["bw"] / 1024)  # to MiB/s
                if "write" in w:
                    data[w][s].append(job["write"]["bw"] / 1024)  # to MiB/s



# Function taken from: https://www.geeksforgeeks.org/machine-learning/how-to-find-a-p-value-from-a-t-score-in-python/
def interpret_p_value(p_value, alpha=0.05):
    if p_value < alpha:
        return "Reject the null hypothesis. There is a statistically significant difference."
    else:
        return "Fail to reject the null hypothesis. There is no statistically significant difference."


def run_comparisons(comparisons):
    for workload in workloads:
        print("Results for workload:", workload)

        for setup1, setup2 in comparisons:
            a = data[workload][setup1]
            b = data[workload][setup2]

            # Mann-Whitney test to get p value
            # method taken from: https://mcpanalytics.ai/articles/mann-whitney-u-test-practical-guide-for-data-driven-decisions
            # explains that man-whitney more appropriate for outliers
            u, p = mannwhitneyu(a, b, alternative="two-sided")

            result = interpret_p_value(p)

            print(workload, setup1, "vs", setup2, "p-value:", p)
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
