import json
import matplotlib.pyplot as plt
import numpy as np

import csv
import matplotlib

import pandas as pd

file_directory = "../../snails/sysbench_backup/results_backup_csv"

setups = ["ext4-default", "ext4-tuned", "btrfs-default", "btrfs-tuned"]
workloads = ["seqread", "randread", "seqwrite", "randwrite"]

titles = {
    "seqread": "(a) Sequential read",
    "randread": "(b) Random read",
    "seqwrite": "(c) Sequential write",
    "randwrite": "(d) Random write",
}

# extract the data we want from the results and store in a dictionary
# a dictionary entry looks like: data[workload][setup] = list of results
# e.g. data["seqread"]["ext4-default"] = [500, ...]
data = {}
for w in workloads:
    data[w] = {}
    for s in setups:
        data[w][s] = []
        for rep in range(1, 31):
            # read a specific column from a csv file, following: https://www.geeksforgeeks.org/pandas/python-read-csv-using-pandas-read_csv/
            df = pd.read_csv(f"{file_directory}/{s}_{w}_{rep}.csv", usecols=["value"])

            if "read" in w:
                data[w][s].append(df["value"][0])   # the read value is the first row in the column
            else:
                data[w][s].append(df["value"][1])   # and the written value is the second


# *************************** create boxplots ***************************

for i, workload in enumerate(workloads):    # 1 boxplot for each workload

    fig, ax = plt.subplots(1, 1, figsize=(6, 6))

    # matplotlib's boxplot function wants a list of lists
    # so values is a list where each element of the list is all 30 values for a given setup
    # this is how its done in: https://www.geeksforgeeks.org/data-visualization/box-plot-in-python-using-matplotlib/
    values = [
        data[workload]["ext4-default"],
        data[workload]["ext4-tuned"],
        data[workload]["btrfs-default"],
        data[workload]["btrfs-tuned"],
    ]

    # plot and plot settings using code from: https://matplotlib.org/stable/plot_types/stats/boxplot_plot.html
    # NOTE: using matplotlib's default whisker definition of 1.5 x IQR
    ax.boxplot(
        values,
        widths=0.6,
        medianprops={"color": "black", "ls": "--"},
        )
    ax.set(xticks=np.arange(1, 5))
    ax.set_xticklabels([s.replace("-", "\n") for s in setups])
    # setting x ticks with words: https://www.geeksforgeeks.org/python/matplotlib-setting-ticks-and-tick-labels/
    # replacing dashes with spaces, using: https://pythonguides.com/replace-whitespaces-with-underscore-in-python/

    if "seq" in workload:
        ax.set_ylabel("Throughput (MiB/s)")
    else:
        ax.set_ylabel("IOPS")

    ax.grid(True, color="lightgrey")  # add gridlines so plot can be read easily, following https://www.geeksforgeeks.org/python/grids-in-matplotlib/

    #fig.suptitle("Sysbench, " + str(workload), fontsize=12)
    # from: https://www.geeksforgeeks.org/python/how-to-add-title-to-subplots-in-matplotlib/

    plt.tight_layout() # otherwise text overlaps plots, from: https://pythonguides.com/matplotlib-tight-layout/

    plt.savefig(f"../results/figures_sysbench_pilot/boxplot_{workload}_combined_sysbench_pilot.png", dpi=300, bbox_inches = "tight")
    # saving figures code from:
    # https://pythonguides.com/matplotlib-save-graph-as-png/
    # bbox_inches used because edges of plot were cut off without it
    # found at: https://stackoverflow.com/questions/45239261/savefig-text-chopped-off


# *************************** create boxplots v2 ***************************
# the Btrfs and ext4 boxplots were sometimes very far apart in some workloads, so the boxes looked squashed
# this is the same code as above, we just plot Btrfs and ext4 in separate panels here
# code for making plot with two panels taken from: https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html


fig = plt.figure(figsize=(10, 8))
subfigs = fig.subfigures(2, 2, wspace=0.25, hspace=0.07)  # gap between the 4 panels themselves

for subfig, workload in zip(subfigs.flatten(), workloads):
    ax1, ax2 = subfig.subplots(1, 2, gridspec_kw={"wspace": 0.02})
    subfig.subplots_adjust(left=0.08, right=0.98, top=0.93, bottom=0.12)

    values_ext4 = [data[workload]["ext4-default"], data[workload]["ext4-tuned"]]
    values_btrfs = [data[workload]["btrfs-default"], data[workload]["btrfs-tuned"]]

    # NOTE: using matplotlib's default whisker definition of 1.5 x IQR
    ax1.boxplot(values_ext4, widths=0.6, medianprops={"color": "black", "ls": "--"})
    ax2.boxplot(values_btrfs, widths=0.6, medianprops={"color": "black", "ls": "--"})

    ax1.set_xticks([1, 2])
    ax2.set_xticks([1, 2])
    ax1.set_xticklabels(["ext4\ndefault", "ext4\ntuned"])
    ax2.set_xticklabels(["btrfs\ndefault", "btrfs\ntuned"])
    ax2.yaxis.tick_right()

    ax1.grid(True, color="lightgrey")
    ax2.grid(True, color="lightgrey")

    #ax1.set_title(titles[workload], loc="left")
    subfig.suptitle(titles[workload], fontsize=12)
    #ax2.set_title(workload + ", btrfs")

    if "seq" in workload:
        ax1.set_ylabel("Throughput (MiB/s)")
    else:
        ax1.set_ylabel("IOPS")

plt.tight_layout() 
    
plt.savefig(f"../results/figures_sysbench_pilot/boxplots_sysbench_pilot.png", dpi=300, bbox_inches = "tight")



# *************************** create csv files ***************************
# here saving a summary table of the results
# saves 1 file per workload and setup, and also a file with all summary statistics together

# the code here following the first example at: https://www.geeksforgeeks.org/python/how-to-save-a-python-dictionary-to-a-csv-file/
# iqr and percentiles calculated using example at: https://www.geeksforgeeks.org/numpy/interquartile-range-and-quartile-deviation-using-numpy-and-scipy/
# mins and maxs from: https://www.geeksforgeeks.org/python/python-min-function/
# mean from: https://numpy.org/doc/stable/reference/generated/numpy.mean.html
# standard deviation from: https://numpy.org/doc/stable/reference/generated/numpy.std.html

fieldnames = ["workload", "setup", "n", "median", "Q1", "Q3", "IQR", "min", "max", "mean", "SD"]

with open("../results/summary_all_workloads_sysbench_pilot.csv", "w", newline="") as csvfile:

    fieldnames = ["workload", "setup", "n", "median", "Q1", "Q3", "IQR", "min", "max", "mean", "SD"]

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    # calculate the statistics
    for workload in workloads:
        for setup in setups:
            values = np.array(data[workload][setup])
            n = len(values)
            q1 = np.percentile(values, 25)
            median = np.percentile(values, 50)
            q3 = np.percentile(values, 75)
            iqr = q3 - q1
            minimum = np.min(values)
            maximum = np.max(values)
            mean = np.mean(values)
            std = np.std(values)

            # save statistics in a dictionary that will be one row of the csv
            row = {
                "workload": workload,
                "setup": setup,
                "n": n,
                "median": median,
                "Q1": q1,
                "Q3": q3,
                "IQR": iqr,
                "min": minimum,
                "max": maximum,
                "mean": mean,
                "SD": std,
            }
            writer.writerow(row)


# *************************** plot of value vs rep number ***************************
# again, very different values for ext4 and btrfs, so we make one plot for each
# based on same code sources as earlier for plot labels etc.

reps = range(1, 31)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()  # means that we can loop over the panels, taken from: https://stackoverflow.com/questions/28070906/loop-over-2d-subplot-as-if-its-a-1-d

for ax, workload in zip(axes, workloads):
    d = data[workload]

    ax.plot(reps, d["ext4-default"], color="black", linestyle="-", label="ext4-default")
    ax.plot(reps, d["ext4-tuned"], color="black", linestyle="--", label="ext4-tuned")

    if "seq" in workload:
        ax.set_ylabel("Throughput (MiB/s)")
    else:
        ax.set_ylabel("IOPS")
    
    #fig.suptitle("Sysbench, ext4", fontsize=12)

    ax.set_xlabel("Rep")

    ax.grid(True, color="lightgrey")
    
    ax.legend()

    ax.set_title(titles[workload])

    plt.tight_layout() 

axes[0].set_ylim([534, 540])
axes[1].set_ylim([45250, 45500])
plt.savefig(f"../results/figures_sysbench_pilot/value_vs_rep_ext4_sysbench_pilot.png", dpi=300, bbox_inches="tight")


fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for ax, workload in zip(axes, workloads):

    d = data[workload]
    ax.plot(reps, d["btrfs-default"], color="black", linestyle="-", label="Btrfs-default")
    ax.plot(reps, d["btrfs-tuned"], color="black", linestyle="--", label="Btrfs-tuned")

    if "seq" in workload:
        ax.set_ylabel("Throughput (MiB/s)")
    else:
        ax.set_ylabel("IOPS")
    
    #fig.suptitle("Sysbench, BTRFS", fontsize=12)

    ax.set_xlabel("Rep")
    ax.grid(True, color="lightgrey")

    ax.set_title(titles[workload])

    ax.legend()

    plt.tight_layout() 

plt.savefig(f"../results/figures_sysbench_pilot/value_vs_rep_btrfs_sysbench_pilot.png", dpi=300, bbox_inches="tight")