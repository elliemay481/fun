import matplotlib.pyplot as plt
import numpy as np

import csv


setups = ["ext4-default", "ext4-tuned", "btrfs-default", "btrfs-tuned"]
workloads = ["seqread", "randread", "seqwrite", "randwrite"]

titles = {
    "seqread": "(a) Sequential read",
    "randread": "(b) Random read",
    "seqwrite": "(c) Sequential write",
    "randwrite": "(d) Random write",
}

dictionary_seqread = {
    "ext4-default": [
        535.59, 537.33, 539.21, 538.52, 537.89,
        537.46, 537.36, 539.02, 535.82, 537.38,
        538.58, 537.41, 536.77, 538.39, 537.31,
        538.92, 539.0, 537.18, 539.03, 537.85,
        536.67, 538.09, 537.45, 537.46, 536.52,
        537.6, 537.41, 538.04, 537.54, 539.41,
        538.07, 537.22,
    ],
    "ext4-tuned": [
        536.3, 537.14, 537.71, 536.99, 539.37,
        536.27, 537.44, 538.34, 538.59, 536.82,
        539.83, 535.68, 537.61, 537.52, 537.55,
        539.12, 538.99, 537.06, 537.06, 538.55,
        537.41, 537.24, 537.37, 537.07, 537.23,
        536.21, 537.36, 539.19, 540.01, 537.21,
        537.95, 535.4,
    ],
    "btrfs-default": [
        420.07, 415.35, 421.36, 417.54, 421.44,
        419.53, 417.38, 422.36, 418.57, 414.61,
        415.24, 416.88, 421.33, 420.47, 420.71,
        423.1, 421.69, 417.14, 420.88, 406.17,
        419.02, 419.21, 420.16, 426.53, 421.53,
        416.33, 418.8, 422.14, 421.15, 416.66,
        419.47, 415.61,
    ],
    "btrfs-tuned": [
        421.69, 421.01, 417.65, 418.07, 421.36,
        422.07, 413.86, 415.43, 423.75, 421.62,
        419.54, 420.58, 423.08, 425.22, 420.97,
        415.94, 418.26, 421.95, 417.66, 420.49,
        421.13, 419.73, 419.48, 416.65, 422.49,
        418.27, 414.93, 419.41, 418.56, 420.67,
        417.18, 414.88,
    ],
}

dictionary_randread = {
    "ext4-default": [
        45403.21, 45313.02, 45435.37, 45360.16, 45382.63,
        45387.34, 45437.82, 45411.57, 45391.0, 45364.11,
        45405.2, 45308.1, 45349.86, 45370.37, 45178.08,
        45353.67, 45417.77, 45301.08, 45392.55, 45351.32,
        45355.4, 45388.52, 45434.14, 45339.24, 45239.58,
        45378.43, 45190.99, 45372.77, 45475.4, 45351.02,
        45409.33, 45430.15,
    ],
    "ext4-tuned": [
        45316.15, 45480.2, 45371.25, 45290.89, 45322.19,
        45393.3, 45376.1, 45386.32, 45159.79, 45368.82,
        45309.78, 45309.63, 45322.72, 45382.82, 45277.82,
        45412.87, 45393.02, 45294.93, 45357.57, 45378.05,
        45345.4, 45339.71, 45424.31, 45340.77, 45382.73,
        45333.83, 45433.6, 45369.67, 45419.71, 45445.78,
        45390.28, 45358.56,
    ],
    "btrfs-default": [
        43066.65, 43359.5, 43063.46, 43294.21, 42827.84,
        43233.23, 43306.99, 43333.47, 43199.68, 43182.52,
        43047.36, 43085.46, 42900.21, 43235.52, 42740.15,
        42986.72, 43109.97, 42877.28, 43254.56, 42771.78,
        43353.41, 42934.2, 43171.88, 43235.23, 42968.34,
        42986.55, 43387.93, 43219.6, 43290.69, 43133.67,
        43077.35, 42690.09,
    ],
    "btrfs-tuned": [
        42985.06, 43185.31, 43209.85, 43153.42, 43087.62,
        43065.31, 43365.87, 42864.17, 43198.41, 43210.65,
        43349.15, 42947.3, 43090.75, 43284.85, 43134.21,
        43153.43, 43399.07, 42951.24, 43306.96, 43328.01,
        43320.87, 42809.43, 43147.94, 43122.64, 43153.36,
        43086.11, 43202.72, 42885.39, 43364.29, 43043.43,
        43317.5, 43112.39,
    ],
}

dictionary_seqwrite = {
    "ext4-default": [
        464.84, 462.51, 459.12, 448.06, 469.93,
        464.42, 461.45, 439.81, 469.11, 467.51,
        466.9, 446.83, 471.67, 467.33, 466.03,
        445.59, 471.66, 466.42, 470.88, 439.14,
        465.44, 467.96, 465.47, 442.28, 469.37,
        467.53, 468.27, 441.68, 467.79, 468.73,
        466.67, 448.21,
    ],
    "ext4-tuned": [
        413.58, 468.07, 471.42, 462.47, 426.72,
        467.91, 463.02, 467.03, 408.0, 467.17,
        465.17, 459.68, 431.48, 471.22, 466.34,
        458.86, 406.42, 464.3, 465.47, 458.62,
        420.28, 467.31, 467.14, 458.11, 397.05,
        473.3, 464.02, 460.6, 390.04, 468.4,
        459.87, 460.52,
    ],
    "btrfs-default": [
        444.24, 333.38, 502.27, 503.0, 481.04,
        321.97, 501.37, 504.47, 479.73, 388.85,
        502.32, 503.2, 487.38, 345.43, 501.79,
        476.82, 496.84, 363.14, 501.61, 504.17,
        430.51, 398.36, 503.44, 503.61, 445.21,
        344.73, 502.36, 503.37, 414.88, 338.82,
        472.67, 503.65,
    ],
    "btrfs-tuned": [
        502.72, 501.65, 389.44, 501.79, 503.71,
        475.5, 303.0, 502.79, 504.08, 502.76,
        388.26, 502.8, 503.46, 503.05, 308.57,
        502.54, 503.26, 500.95, 324.79, 502.26,
        504.4, 503.17, 315.62, 502.24, 504.96,
        502.72, 318.1, 502.02, 502.88, 503.95,
        315.03, 501.51,
    ],
}

dictionary_randwrite = {
    "ext4-default": [
        59894.88, 59568.4, 85429.38, 85187.48, 71452.81,
        56788.74, 86104.99, 85206.23, 68118.65, 57726.52,
        85669.26, 85866.36, 71972.81, 58295.82, 85228.37,
        85289.14, 70892.07, 58093.35, 85214.67, 86146.31,
        72828.33, 59188.85, 85716.34, 85599.62, 69384.09,
        58066.05, 85913.18, 85467.58, 73049.7, 58335.15,
        86016.59, 85499.75,
    ],
    "ext4-tuned": [
        85241.24, 76970.07, 57271.09, 83209.51, 85663.98,
        73543.99, 58582.44, 86259.35, 85710.34, 76725.95,
        57491.64, 85497.99, 85724.31, 77095.42, 58759.56,
        85184.71, 85390.92, 76575.58, 58128.39, 85435.46,
        85313.4, 78595.22, 58582.55, 85983.69, 85387.17,
        78490.52, 59217.04, 85176.2, 85314.3, 79174.19,
        59063.73, 86174.26,
    ],
    "btrfs-default": [
        43489.65, 39482.36, 42269.77, 39264.58, 41387.56,
        44310.13, 39730.1, 41741.85, 45585.76, 43458.92,
        43235.59, 39884.24, 40788.81, 40199.49, 38929.44,
        39676.05, 43757.24, 38376.31, 54492.77, 40406.04,
        41212.04, 40457.78, 36616.55, 39000.88, 44280.04,
        41796.15, 39515.7, 38529.49, 43169.59, 40188.45,
        43401.65, 39764.39,
    ],
    "btrfs-tuned": [
        38971.52, 42237.89, 43712.8, 39787.82, 39462.93,
        44230.28, 44970.68, 38546.88, 38575.35, 40672.62,
        41165.91, 38661.16, 37487.61, 40589.92, 43505.81,
        40535.37, 37322.6, 42729.72, 39151.98, 39441.9,
        41010.96, 39680.37, 44057.07, 39002.52, 41054.75,
        43250.52, 39652.5, 41894.56, 40604.14, 43491.11,
        44115.4, 41753.03,
    ],
}
# *************************** create boxplots ***************************

fig, ax = plt.subplots(1, 1, figsize=(6, 6))    # 1 boxplot for each workload

# matplotlib's boxplot function wants a list of lists
# so values is a list where each element of the list is all 30 values for a given setup
# this is how its done in: https://www.geeksforgeeks.org/data-visualization/box-plot-in-python-using-matplotlib/
values = [
    dictionary_seqread["ext4-default"],
    dictionary_seqread["ext4-tuned"],
    dictionary_seqread["btrfs-default"],
    dictionary_seqread["btrfs-tuned"],
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

ax.set_ylabel("Throughput (MiB/s)")

ax.grid(True, color="lightgrey")  # add gridlines so plot can be read easily, following https://www.geeksforgeeks.org/python/grids-in-matplotlib/


# from: https://matplotlib.org/3.1.1/gallery/subplots_axes_and_figures/figure_title.html
# and https://blog.finxter.com/5-best-ways-to-add-a-variable-to-python-plt-title/

plt.tight_layout() # otherwise text overlaps plots, from: https://pythonguides.com/matplotlib-tight-layout/

plt.savefig(f"../results/figures_sysbench_v2/boxplot_seqread_sysbench_v2_combined.png", dpi=300, bbox_inches = "tight")
# saving figures code from:
# https://pythonguides.com/matplotlib-save-graph-as-png/
# bbox_inches used because edges of plot were cut off without it
# found at: https://stackoverflow.com/questions/45239261/savefig-text-chopped-off


fig, ax = plt.subplots(1, 1, figsize=(6, 6))

values = [
    dictionary_randread["ext4-default"],
    dictionary_randread["ext4-tuned"],
    dictionary_randread["btrfs-default"],
    dictionary_randread["btrfs-tuned"],
]

ax.boxplot(
    values,
    widths=0.6,
    medianprops={"color": "black", "ls": "--"},
    )
ax.set(xticks=np.arange(1, 5))
ax.set_xticklabels([s.replace("-", "\n") for s in setups])

ax.set_ylabel("IOPS")

ax.grid(True, color="lightgrey")

plt.tight_layout()

plt.savefig(f"../results/figures_sysbench_v2/boxplot_randread_sysbench_v2_combined.png", dpi=300, bbox_inches = "tight")


fig, ax = plt.subplots(1, 1, figsize=(6, 6))

values = [
    dictionary_seqwrite["ext4-default"],
    dictionary_seqwrite["ext4-tuned"],
    dictionary_seqwrite["btrfs-default"],
    dictionary_seqwrite["btrfs-tuned"],
]

ax.boxplot(
    values,
    widths=0.6,
    medianprops={"color": "black", "ls": "--"},
    )
ax.set(xticks=np.arange(1, 5))
ax.set_xticklabels([s.replace("-", "\n") for s in setups])

ax.set_ylabel("Throughput (MiB/s)")

ax.grid(True, color="lightgrey")

plt.tight_layout()

plt.savefig(f"../results/figures_sysbench_v2/boxplot_seqwrite_sysbench_v2_combined.png", dpi=300, bbox_inches = "tight")


fig, ax = plt.subplots(1, 1, figsize=(6, 6))

values = [
    dictionary_randwrite["ext4-default"],
    dictionary_randwrite["ext4-tuned"],
    dictionary_randwrite["btrfs-default"],
    dictionary_randwrite["btrfs-tuned"],
]

ax.boxplot(
    values,
    widths=0.6,
    medianprops={"color": "black", "ls": "--"},
    )
ax.set(xticks=np.arange(1, 5))
ax.set_xticklabels([s.replace("-", "\n") for s in setups])

ax.set_ylabel("IOPS")

ax.grid(True, color="lightgrey")

plt.tight_layout()

plt.savefig(f"../results/figures_sysbench_v2/boxplot_randwrite_sysbench_v2_combined.png", dpi=300, bbox_inches = "tight")


# *************************** create boxplots v2 ***************************
# the Btrfs and ext4 boxplots were sometimes very far apart in some workloads, so the boxes looked squashed
# this is the same code as above, we just plot Btrfs and ext4 in separate panels here
# code for making plot with two panels taken from: https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html

fig = plt.figure(figsize=(10, 8))
subfigs = fig.subfigures(2, 2, wspace=0.25, hspace=0.07)  # gap between the 4 panels themselves

subfig = subfigs.flatten()[0]
ax1, ax2 = subfig.subplots(1, 2, gridspec_kw={"wspace": 0.02})
subfig.subplots_adjust(left=0.08, right=0.98, top=0.93, bottom=0.12)

values_ext4 = [dictionary_seqread["ext4-default"], dictionary_seqread["ext4-tuned"]]
values_btrfs = [dictionary_seqread["btrfs-default"], dictionary_seqread["btrfs-tuned"]]

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
subfig.suptitle(titles["seqread"], fontsize=12)
#ax2.set_title(workload + ", btrfs")

ax1.set_ylabel("Throughput (MiB/s)")

subfig = subfigs.flatten()[1]
ax1, ax2 = subfig.subplots(1, 2, gridspec_kw={"wspace": 0.02})
subfig.subplots_adjust(left=0.08, right=0.98, top=0.93, bottom=0.12)

values_ext4 = [dictionary_randread["ext4-default"], dictionary_randread["ext4-tuned"]]
values_btrfs = [dictionary_randread["btrfs-default"], dictionary_randread["btrfs-tuned"]]

ax1.boxplot(values_ext4, widths=0.6, medianprops={"color": "black", "ls": "--"})
ax2.boxplot(values_btrfs, widths=0.6, medianprops={"color": "black", "ls": "--"})

ax1.set_xticks([1, 2])
ax2.set_xticks([1, 2])
ax1.set_xticklabels(["ext4\ndefault", "ext4\ntuned"])
ax2.set_xticklabels(["btrfs\ndefault", "btrfs\ntuned"])
ax2.yaxis.tick_right()

ax1.grid(True, color="lightgrey")
ax2.grid(True, color="lightgrey")

subfig.suptitle(titles["randread"], fontsize=12)

ax1.set_ylabel("IOPS")

subfig = subfigs.flatten()[2]
ax1, ax2 = subfig.subplots(1, 2, gridspec_kw={"wspace": 0.02})
subfig.subplots_adjust(left=0.08, right=0.98, top=0.93, bottom=0.12)

values_ext4 = [dictionary_seqwrite["ext4-default"], dictionary_seqwrite["ext4-tuned"]]
values_btrfs = [dictionary_seqwrite["btrfs-default"], dictionary_seqwrite["btrfs-tuned"]]

ax1.boxplot(values_ext4, widths=0.6, medianprops={"color": "black", "ls": "--"})
ax2.boxplot(values_btrfs, widths=0.6, medianprops={"color": "black", "ls": "--"})

ax1.set_xticks([1, 2])
ax2.set_xticks([1, 2])
ax1.set_xticklabels(["ext4\ndefault", "ext4\ntuned"])
ax2.set_xticklabels(["btrfs\ndefault", "btrfs\ntuned"])
ax2.yaxis.tick_right()

ax1.grid(True, color="lightgrey")
ax2.grid(True, color="lightgrey")

subfig.suptitle(titles["seqwrite"], fontsize=12)

ax1.set_ylabel("Throughput (MiB/s)")

subfig = subfigs.flatten()[3]
ax1, ax2 = subfig.subplots(1, 2, gridspec_kw={"wspace": 0.02})
subfig.subplots_adjust(left=0.08, right=0.98, top=0.93, bottom=0.12)

values_ext4 = [dictionary_randwrite["ext4-default"], dictionary_randwrite["ext4-tuned"]]
values_btrfs = [dictionary_randwrite["btrfs-default"], dictionary_randwrite["btrfs-tuned"]]

ax1.boxplot(values_ext4, widths=0.6, medianprops={"color": "black", "ls": "--"})
ax2.boxplot(values_btrfs, widths=0.6, medianprops={"color": "black", "ls": "--"})

ax1.set_xticks([1, 2])
ax2.set_xticks([1, 2])
ax1.set_xticklabels(["ext4\ndefault", "ext4\ntuned"])
ax2.set_xticklabels(["btrfs\ndefault", "btrfs\ntuned"])
ax2.yaxis.tick_right()

ax1.grid(True, color="lightgrey")
ax2.grid(True, color="lightgrey")

subfig.suptitle(titles["randwrite"], fontsize=12)

ax1.set_ylabel("IOPS")

plt.tight_layout() 
        
plt.savefig(f"../results/figures_sysbench_v2/boxplots_sysbench_v2.png", dpi=300, bbox_inches = "tight")



# *************************** create csv files ***************************
# here saving a summary table of the results
# saves 1 file per workload and setup, and also a file with all summary statistics together

# the code here following the first example at: https://www.geeksforgeeks.org/python/how-to-save-a-python-dictionary-to-a-csv-file/
# iqr and percentiles calculated using example at: https://www.geeksforgeeks.org/numpy/interquartile-range-and-quartile-deviation-using-numpy-and-scipy/
# mins and maxs from: https://www.geeksforgeeks.org/python/python-min-function/
# mean from: https://numpy.org/doc/stable/reference/generated/numpy.mean.html
# standard deviation from: https://numpy.org/doc/stable/reference/generated/numpy.std.html

fieldnames = ["workload", "setup", "n", "median", "Q1", "Q3", "IQR", "min", "max", "mean", "SD"]

with open("../results/summary_all_workloads_sysbench_v2.csv", "w", newline="") as csvfile:

    fieldnames = ["workload", "setup", "n", "median", "Q1", "Q3", "IQR", "min", "max", "mean", "SD"]

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    # calculate the statistics
    values = np.array(dictionary_seqread["ext4-default"])
    n = len(values)
    q1 = np.percentile(values, 25)
    median = np.percentile(values, 50)
    q3 = np.percentile(values, 75)
    iqr = q3 - q1
    minimum = np.min(values)
    maximum = np.max(values)
    mean = np.mean(values)
    std = np.std(values, ddof=1)

    # save statistics in a dictionary that will be one row of the csv
    row = {
        "workload": "seqread",
        "setup": "ext4-default",
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

    values = np.array(dictionary_seqread["ext4-tuned"])
    n = len(values)
    q1 = np.percentile(values, 25)
    median = np.percentile(values, 50)
    q3 = np.percentile(values, 75)
    iqr = q3 - q1
    minimum = np.min(values)
    maximum = np.max(values)
    mean = np.mean(values)
    std = np.std(values, ddof=1)

    row = {
        "workload": "seqread",
        "setup": "ext4-tuned",
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

    values = np.array(dictionary_seqread["btrfs-default"])
    n = len(values)
    q1 = np.percentile(values, 25)
    median = np.percentile(values, 50)
    q3 = np.percentile(values, 75)
    iqr = q3 - q1
    minimum = np.min(values)
    maximum = np.max(values)
    mean = np.mean(values)
    std = np.std(values, ddof=1)

    row = {
        "workload": "seqread",
        "setup": "btrfs-default",
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

    values = np.array(dictionary_seqread["btrfs-tuned"])
    n = len(values)
    q1 = np.percentile(values, 25)
    median = np.percentile(values, 50)
    q3 = np.percentile(values, 75)
    iqr = q3 - q1
    minimum = np.min(values)
    maximum = np.max(values)
    mean = np.mean(values)
    std = np.std(values, ddof=1)

    row = {
        "workload": "seqread",
        "setup": "btrfs-tuned",
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

    values = np.array(dictionary_randread["ext4-default"])
    n = len(values)
    q1 = np.percentile(values, 25)
    median = np.percentile(values, 50)
    q3 = np.percentile(values, 75)
    iqr = q3 - q1
    minimum = np.min(values)
    maximum = np.max(values)
    mean = np.mean(values)
    std = np.std(values, ddof=1)

    row = {
        "workload": "randread",
        "setup": "ext4-default",
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

    values = np.array(dictionary_randread["ext4-tuned"])
    n = len(values)
    q1 = np.percentile(values, 25)
    median = np.percentile(values, 50)
    q3 = np.percentile(values, 75)
    iqr = q3 - q1
    minimum = np.min(values)
    maximum = np.max(values)
    mean = np.mean(values)
    std = np.std(values, ddof=1)

    row = {
        "workload": "randread",
        "setup": "ext4-tuned",
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

    values = np.array(dictionary_randread["btrfs-default"])
    n = len(values)
    q1 = np.percentile(values, 25)
    median = np.percentile(values, 50)
    q3 = np.percentile(values, 75)
    iqr = q3 - q1
    minimum = np.min(values)
    maximum = np.max(values)
    mean = np.mean(values)
    std = np.std(values, ddof=1)

    row = {
        "workload": "randread",
        "setup": "btrfs-default",
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

    values = np.array(dictionary_randread["btrfs-tuned"])
    n = len(values)
    q1 = np.percentile(values, 25)
    median = np.percentile(values, 50)
    q3 = np.percentile(values, 75)
    iqr = q3 - q1
    minimum = np.min(values)
    maximum = np.max(values)
    mean = np.mean(values)
    std = np.std(values, ddof=1)

    row = {
        "workload": "randread",
        "setup": "btrfs-tuned",
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

    values = np.array(dictionary_seqwrite["ext4-default"])
    n = len(values)
    q1 = np.percentile(values, 25)
    median = np.percentile(values, 50)
    q3 = np.percentile(values, 75)
    iqr = q3 - q1
    minimum = np.min(values)
    maximum = np.max(values)
    mean = np.mean(values)
    std = np.std(values, ddof=1)

    row = {
        "workload": "seqwrite",
        "setup": "ext4-default",
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

    values = np.array(dictionary_seqwrite["ext4-tuned"])
    n = len(values)
    q1 = np.percentile(values, 25)
    median = np.percentile(values, 50)
    q3 = np.percentile(values, 75)
    iqr = q3 - q1
    minimum = np.min(values)
    maximum = np.max(values)
    mean = np.mean(values)
    std = np.std(values, ddof=1)

    row = {
        "workload": "seqwrite",
        "setup": "ext4-tuned",
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

    values = np.array(dictionary_seqwrite["btrfs-default"])
    n = len(values)
    q1 = np.percentile(values, 25)
    median = np.percentile(values, 50)
    q3 = np.percentile(values, 75)
    iqr = q3 - q1
    minimum = np.min(values)
    maximum = np.max(values)
    mean = np.mean(values)
    std = np.std(values, ddof=1)

    row = {
        "workload": "seqwrite",
        "setup": "btrfs-default",
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

    values = np.array(dictionary_seqwrite["btrfs-tuned"])
    n = len(values)
    q1 = np.percentile(values, 25)
    median = np.percentile(values, 50)
    q3 = np.percentile(values, 75)
    iqr = q3 - q1
    minimum = np.min(values)
    maximum = np.max(values)
    mean = np.mean(values)
    std = np.std(values, ddof=1)

    row = {
        "workload": "seqwrite",
        "setup": "btrfs-tuned",
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

    values = np.array(dictionary_randwrite["ext4-default"])
    n = len(values)
    q1 = np.percentile(values, 25)
    median = np.percentile(values, 50)
    q3 = np.percentile(values, 75)
    iqr = q3 - q1
    minimum = np.min(values)
    maximum = np.max(values)
    mean = np.mean(values)
    std = np.std(values, ddof=1)

    row = {
        "workload": "randwrite",
        "setup": "ext4-default",
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

    values = np.array(dictionary_randwrite["ext4-tuned"])
    n = len(values)
    q1 = np.percentile(values, 25)
    median = np.percentile(values, 50)
    q3 = np.percentile(values, 75)
    iqr = q3 - q1
    minimum = np.min(values)
    maximum = np.max(values)
    mean = np.mean(values)
    std = np.std(values, ddof=1)

    row = {
        "workload": "randwrite",
        "setup": "ext4-tuned",
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

    values = np.array(dictionary_randwrite["btrfs-default"])
    n = len(values)
    q1 = np.percentile(values, 25)
    median = np.percentile(values, 50)
    q3 = np.percentile(values, 75)
    iqr = q3 - q1
    minimum = np.min(values)
    maximum = np.max(values)
    mean = np.mean(values)
    std = np.std(values, ddof=1)

    row = {
        "workload": "randwrite",
        "setup": "btrfs-default",
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

    values = np.array(dictionary_randwrite["btrfs-tuned"])
    n = len(values)
    q1 = np.percentile(values, 25)
    median = np.percentile(values, 50)
    q3 = np.percentile(values, 75)
    iqr = q3 - q1
    minimum = np.min(values)
    maximum = np.max(values)
    mean = np.mean(values)
    std = np.std(values, ddof=1)

    row = {
        "workload": "randwrite",
        "setup": "btrfs-tuned",
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

ax = axes[0]
d = dictionary_seqread

ax.plot(reps, d["ext4-default"], color="black", linestyle="-", label="ext4-default")
ax.plot(reps, d["ext4-tuned"], color="black", linestyle="--", label="ext4-tuned")

ax.set_ylabel("Throughput (MiB/s)")

ax.set_title("seqread")
ax.set_xlabel("Rep")
ax.grid(True, color="lightgrey")


ax.legend()

ax.set_title(titles["seqread"])

plt.tight_layout() 

ax = axes[1]
d = dictionary_randread

ax.plot(reps, d["ext4-default"], color="black", linestyle="-", label="ext4-default")
ax.plot(reps, d["ext4-tuned"], color="black", linestyle="--", label="ext4-tuned")

ax.set_ylabel("IOPS")

ax.set_title("randread")
ax.set_xlabel("Rep")
ax.grid(True, color="lightgrey")

ax.legend()

ax.set_title(titles["randread"])

plt.tight_layout() 

ax = axes[2]
d = dictionary_seqwrite

ax.plot(reps, d["ext4-default"], color="black", linestyle="-", label="ext4-default")
ax.plot(reps, d["ext4-tuned"], color="black", linestyle="--", label="ext4-tuned")

ax.set_ylabel("Throughput (MiB/s)")

ax.set_title("seqwrite")
ax.set_xlabel("Rep")
ax.grid(True, color="lightgrey")

ax.legend()

ax.set_title(titles["seqwrite"])

plt.tight_layout() 

ax = axes[3]
d = dictionary_randwrite

ax.plot(reps, d["ext4-default"], color="black", linestyle="-", label="ext4-default")
ax.plot(reps, d["ext4-tuned"], color="black", linestyle="--", label="ext4-tuned")

ax.set_ylabel("IOPS")

ax.set_title("randwrite")
ax.set_xlabel("Rep")
ax.grid(True, color="lightgrey")

ax.legend()

ax.set_title(titles["randwrite"])

plt.tight_layout() 

plt.savefig(f"../results/figures_sysbench_v2/value_vs_rep_ext4_sysbench_v2.png", dpi=300, bbox_inches="tight")


fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

ax = axes[0]

d = dictionary_seqread
ax.plot(reps, d["btrfs-default"], color="black", linestyle="-", label="Btrfs-default")
ax.plot(reps, d["btrfs-tuned"], color="black", linestyle="--", label="Btrfs-tuned")

ax.set_ylabel("Throughput (MiB/s)")


ax.set_xlabel("Rep")
ax.grid(True, color="lightgrey")

ax.set_title(titles["seqread"])

ax.legend()

plt.tight_layout() 

ax = axes[1]

d = dictionary_randread
ax.plot(reps, d["btrfs-default"], color="black", linestyle="-", label="Btrfs-default")
ax.plot(reps, d["btrfs-tuned"], color="black", linestyle="--", label="Btrfs-tuned")

ax.set_ylabel("IOPS")

ax.set_xlabel("Rep")
ax.grid(True, color="lightgrey")

ax.set_title(titles["randread"])

ax.legend()

plt.tight_layout() 

ax = axes[2]

d = dictionary_seqwrite
ax.plot(reps, d["btrfs-default"], color="black", linestyle="-", label="Btrfs-default")
ax.plot(reps, d["btrfs-tuned"], color="black", linestyle="--", label="Btrfs-tuned")

ax.set_ylabel("Throughput (MiB/s)")

ax.set_xlabel("Rep")
ax.grid(True, color="lightgrey")

ax.set_title(titles["seqwrite"])

ax.legend()

plt.tight_layout() 

ax = axes[3]

d = dictionary_randwrite
ax.plot(reps, d["btrfs-default"], color="black", linestyle="-", label="Btrfs-default")
ax.plot(reps, d["btrfs-tuned"], color="black", linestyle="--", label="Btrfs-tuned")

ax.set_ylabel("IOPS")

ax.set_xlabel("Rep")
ax.grid(True, color="lightgrey")

ax.set_title(titles["randwrite"])

ax.legend()

plt.tight_layout() 

plt.savefig(f"../results/figures_sysbench_v2/value_vs_rep_btrfs_sysbench_v2.png", dpi=300, bbox_inches="tight")