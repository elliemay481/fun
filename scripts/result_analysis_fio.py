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
        538.26953125, 537.9365234375, 538.6435546875, 538.4775390625, 538.734375,
        538.9599609375, 538.5849609375, 538.677734375, 538.8193359375, 539.009765625,
        539.1337890625, 538.859375, 538.84375, 539.19140625, 538.91796875,
        539.216796875, 538.8681640625, 538.984375, 539.05078125, 538.701171875,
        539.1171875, 538.7607421875, 538.751953125, 539.0263671875, 538.353515625,
        539.029296875, 538.884765625, 538.642578125, 538.7685546875, 538.5693359375,
    ],
    "ext4-tuned": [
        538.734375, 538.7861328125, 538.68359375, 538.8193359375, 539.1669921875,
        539.1279296875, 539.2763671875, 539.1591796875, 539.216796875, 539.1337890625,
        538.92578125, 539.00390625, 539.1357421875, 538.744140625, 539.125,
        539.2666015625, 538.6923828125, 538.708984375, 538.8349609375, 538.775390625,
        538.5234375, 538.4521484375, 538.6943359375, 538.66796875, 538.6943359375,
        538.46875, 538.228515625, 538.634765625, 538.3779296875, 538.5380859375,
    ],
    "btrfs-default": [
        384.6171875, 388.9912109375, 390.400390625, 391.45703125, 393.470703125,
        392.810546875, 393.9931640625, 393.556640625, 394.0341796875, 393.857421875,
        390.3037109375, 394.1201171875, 394.0009765625, 392.1875, 393.34375,
        391.91015625, 394.18359375, 391.2412109375, 397.6064453125, 394.5166015625,
        394.86328125, 392.919921875, 399.732421875, 395.0830078125, 393.6533203125,
        390.93359375, 394.59375, 394.0966796875, 392.7138671875, 393.7265625,
    ],
    "btrfs-tuned": [
        388.4541015625, 384.64453125, 393.5400390625, 394.943359375, 393.34375,
        393.7705078125, 392.75390625, 389.02734375, 394.0166015625, 393.70703125,
        392.77734375, 394.2373046875, 395.033203125, 392.9931640625, 391.537109375,
        395.2236328125, 394.1435546875, 393.20703125, 391.1875, 395.853515625,
        392.52734375, 391.5234375, 393.1904296875, 393.876953125, 391.9208984375,
        393.6767578125, 394.0869140625, 392.8974609375, 393.5869140625, 392.0869140625,
    ],
}

dictionary_randread = {
    "ext4-default": [
        97392.360127, 96867.702205, 97574.890418, 96612.006467, 97405.059916,
        96975.667072, 96942.950951, 96876.168731, 97501.508308, 97011.549808,
        96698.455026, 96945.234246, 97253.629106, 97365.9939, 96685.988567,
        96862.052299, 97056.465726, 96948.650856, 97484.758587, 97140.347661,
        96969.700505, 97430.276162, 96881.285312, 96722.171297, 97443.39261,
        97160.497325, 97184.896918, 97187.496875, 96790.803487, 96826.069566,
    ],
    "ext4-tuned": [
        96847.935868, 96737.754371, 97051.199147, 97268.295528, 97542.307628,
        96864.785587, 97327.627873, 97043.332611, 96812.38646, 96966.500558,
        96737.521041, 96779.287012, 97235.412743, 97468.17553, 97190.19683,
        97147.897535, 97195.246746, 97239.02935, 97074.99875, 97113.798103,
        97030.949484, 97059.599007, 97114.431426, 96825.21958, 97305.21158,
        97232.42946, 96817.503042, 97041.049316, 96918.718021, 96944.234263,
    ],
    "btrfs-default": [
        101295.628406, 100108.014866, 101968.333861, 100221.57964, 97736.221063,
        98442.142631, 100818.936351, 98754.404093, 100368.760521, 98108.998183,
        98637.889369, 97572.640456, 98287.695205, 98980.133664, 99166.513891,
        101407.843203, 101455.9924, 99942.100965, 99653.62244, 98290.711821,
        98239.762671, 100034.482759, 97801.869969, 99755.9874, 99061.165647,
        99574.990417, 98877.552041, 97990.58349, 99917.134714, 101633.722771,
    ],
    "btrfs-tuned": [
        97986.0169, 98688.138531, 97017.716371, 97397.060049, 97987.800203,
        101720.137998, 99927.467876, 98089.031849, 98620.57299, 99528.157864,
        99710.671489, 98849.502508, 97313.561441, 100378.077032, 98233.046116,
        100125.931234, 99032.066132, 97613.18978, 99480.025333, 101438.559357,
        97567.090548, 97354.860752, 99095.765071, 98110.131498, 98891.368477,
        98434.259429, 97815.636406, 97768.870519, 99316.961384, 98378.82702,
    ],
}

dictionary_seqwrite = {
    "ext4-default": [
        504.08203125, 500.9140625, 500.423828125, 501.462890625, 500.6318359375,
        500.7646484375, 500.97265625, 501.9951171875, 501.62109375, 500.5732421875,
        502.0537109375, 501.330078125, 500.9560546875, 502.2109375, 501.09765625,
        500.3076171875, 501.4384765625, 501.9619140625, 501.0888671875, 502.1279296875,
        502.0283203125, 501.6376953125, 501.5126953125, 501.2880859375, 501.7294921875,
        501.6953125, 501.7958984375, 501.1884765625, 501.62890625, 501.9033203125,
    ],
    "ext4-tuned": [
        504.173828125, 503.775390625, 503.7001953125, 504.19921875, 503.69140625,
        503.275390625, 504.365234375, 503.7333984375, 503.458984375, 504.115234375,
        504.0078125, 503.1259765625, 503.4833984375, 502.91796875, 503.4169921875,
        502.818359375, 503.8583984375, 503.94921875, 503.2919921875, 503.75,
        503.849609375, 503.458984375, 503.69140625, 503.234375, 503.591796875,
        503.68359375, 502.9677734375, 503.333984375, 502.8017578125, 502.5439453125,
    ],
    "btrfs-default": [
        412.0810546875, 413.7607421875, 425.3642578125, 416.017578125, 415.89453125,
        420.509765625, 400.8125, 397.4931640625, 421.0, 386.8271484375,
        418.80078125, 397.7099609375, 424.466796875, 401.986328125, 409.1181640625,
        387.7333984375, 402.2529296875, 418.19140625, 409.681640625, 410.8017578125,
        412.865234375, 415.4013671875, 402.1962890625, 404.3193359375, 386.2373046875,
        410.544921875, 416.07421875, 416.2275390625, 420.30078125, 395.0537109375,
    ],
    "btrfs-tuned": [
        418.9912109375, 414.2177734375, 408.0849609375, 402.359375, 407.28515625,
        402.76953125, 401.2431640625, 413.6279296875, 411.4443359375, 418.00390625,
        416.3203125, 389.37109375, 416.7109375, 400.9189453125, 417.310546875,
        396.3701171875, 384.578125, 399.486328125, 416.451171875, 403.3291015625,
        382.42578125, 409.078125, 397.1298828125, 388.537109375, 415.8037109375,
        410.9111328125, 400.5458984375, 406.9287109375, 411.734375, 402.90234375,
    ],
}

dictionary_randwrite = {
    "ext4-default": [
        86048.730897, 85458.20903, 85396.110065, 84960.967968, 85408.476525,
        85622.962568, 84592.340128, 84993.016783, 85747.162642, 85135.481075,
        86269.695505, 85374.560424, 83604.306595, 85054.046397, 85362.39396,
        85719.030715, 86284.228596, 85714.121431, 84026.765328, 85437.909368,
        85623.356277, 84498.266724, 85779.12771, 84320.061332, 85929.134514,
        84643.872602, 84845.61924, 85014.499758, 85798.22003, 86088.781854,
    ],
    "ext4-tuned": [
        85960.433993, 84575.407077, 85445.042583, 86714.038099, 85084.194387,
        85896.351727, 86588.123531, 86315.128081, 86072.082132, 85540.40766,
        86423.542941, 85524.99125, 85964.700588, 85915.351411, 86624.372927,
        85554.674089, 86463.692272, 85186.384468, 86387.510208, 86379.960334,
        86456.40906, 85729.121181, 86435.092748, 85831.508425, 86385.043583,
        85735.071082, 86666.238896, 86621.622973, 86065.81557, 86306.928218,
    ],
    "btrfs-default": [
        52866.402227, 51900.834986, 50938.468718, 48816.086399, 49594.956751,
        49890.468492, 49899.985, 48752.424919, 49346.927551, 50734.38776,
        48705.088249, 49354.894085, 50404.39326, 48375.627073, 49496.158397,
        48983.717209, 49640.139331, 45223.19256, 49222.496292, 48820.552991,
        49610.323161, 44756.704055, 48231.112815, 49320.006, 50587.690205,
        49127.081215, 48322.177964, 49339.527675, 48598.273362, 53752.037466,
    ],
    "btrfs-tuned": [
        57535.507742, 50481.541974, 49562.040633, 48647.055882, 48978.150364,
        50170.980484, 52959.450676, 48969.350511, 49110.479651, 49232.929451,
        49677.955367, 49069.232179, 48771.187147, 51448.075865, 48307.644873,
        48946.41756, 48891.25725, 50812.119798, 48430.442826, 49563.464551,
        50281.073964, 49749.337511, 48778.18703, 50287.57854, 49328.61119,
        48743.9876, 49955.78407, 49426.709555, 50737.054382, 49854.552424,
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

#fig.suptitle("Fio, " + str(workload), fontsize=12)
# from: https://matplotlib.org/3.1.1/gallery/subplots_axes_and_figures/figure_title.html
# and https://blog.finxter.com/5-best-ways-to-add-a-variable-to-python-plt-title/

plt.tight_layout() # otherwise text overlaps plots, from: https://pythonguides.com/matplotlib-tight-layout/

plt.savefig(f"../results/figures_fio/boxplot_seqread_fio_combined.png", dpi=300, bbox_inches = "tight")
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

plt.savefig(f"../results/figures_fio/boxplot_randread_fio_combined.png", dpi=300, bbox_inches = "tight")


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

plt.savefig(f"../results/figures_fio/boxplot_seqwrite_fio_combined.png", dpi=300, bbox_inches = "tight")


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

plt.savefig(f"../results/figures_fio/boxplot_randwrite_fio_combined.png", dpi=300, bbox_inches = "tight")


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
        
plt.savefig(f"../results/figures_fio/boxplots_fio.png", dpi=300, bbox_inches = "tight")



# *************************** create csv files ***************************
# here saving a summary table of the results
# saves 1 file per workload and setup, and also a file with all summary statistics together

# the code here following the first example at: https://www.geeksforgeeks.org/python/how-to-save-a-python-dictionary-to-a-csv-file/
# iqr and percentiles calculated using example at: https://www.geeksforgeeks.org/numpy/interquartile-range-and-quartile-deviation-using-numpy-and-scipy/
# mins and maxs from: https://www.geeksforgeeks.org/python/python-min-function/
# mean from: https://numpy.org/doc/stable/reference/generated/numpy.mean.html
# standard deviation from: https://numpy.org/doc/stable/reference/generated/numpy.std.html

fieldnames = ["workload", "setup", "n", "median", "Q1", "Q3", "IQR", "min", "max", "mean", "SD"]

with open("../results/summary_all_workloads_fio.csv", "w", newline="") as csvfile:

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

#fig.suptitle("Fio, ext4", fontsize=12)

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

plt.savefig(f"../results/figures_fio/value_vs_rep_ext4_fio.png", dpi=300, bbox_inches="tight")


fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

ax = axes[0]

d = dictionary_seqread
ax.plot(reps, d["btrfs-default"], color="black", linestyle="-", label="Btrfs-default")
ax.plot(reps, d["btrfs-tuned"], color="black", linestyle="--", label="Btrfs-tuned")

ax.set_ylabel("Throughput (MiB/s)")

#fig.suptitle("Fio, BTRFS", fontsize=12)

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

plt.savefig(f"../results/figures_fio/value_vs_rep_btrfs_fio.png", dpi=300, bbox_inches="tight")