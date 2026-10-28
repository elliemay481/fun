from scipy.stats import mannwhitneyu

setups = ["ext4-default", "ext4-tuned", "btrfs-default", "btrfs-tuned"]
workloads = ["seqread", "randread", "seqwrite", "randwrite"]


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

# Function taken from: https://www.geeksforgeeks.org/machine-learning/how-to-find-a-p-value-from-a-t-score-in-python/
def interpret_p_value(p_value, alpha=0.05):
    if p_value < alpha:
        return "Reject the null hypothesis. There is a statistically significant difference."
    else:
        return "Fail to reject the null hypothesis. There is no statistically significant difference."


# Mann-Whitney test to get p value
# method taken from: https://mcpanalytics.ai/articles/mann-whitney-u-test-practical-guide-for-data-driven-decisions
# explains that man-whitney more appropriate for outliers


print("Checking hypothesis 1: ext4 vs btrfs")
print("*****************************************")

# ---------- seqread ----------
print("Results for workload:", "seqread")

a = dictionary_seqread["ext4-default"]
b = dictionary_seqread["btrfs-default"]
u, p = mannwhitneyu(a, b, alternative="two-sided")
result = interpret_p_value(p)
print("seqread", "ext4-default", "vs", "btrfs-default", "p-value:", p)
print(result)
print("------------------------------------------")

a = dictionary_seqread["ext4-tuned"]
b = dictionary_seqread["btrfs-tuned"]
u, p = mannwhitneyu(a, b, alternative="two-sided")
result = interpret_p_value(p)
print("seqread", "ext4-tuned", "vs", "btrfs-tuned", "p-value:", p)
print(result)
print("------------------------------------------")

# ---------- randread ----------
print("Results for workload:", "randread")

a = dictionary_randread["ext4-default"]
b = dictionary_randread["btrfs-default"]
u, p = mannwhitneyu(a, b, alternative="two-sided")
result = interpret_p_value(p)
print("randread", "ext4-default", "vs", "btrfs-default", "p-value:", p)
print(result)
print("------------------------------------------")

a = dictionary_randread["ext4-tuned"]
b = dictionary_randread["btrfs-tuned"]
u, p = mannwhitneyu(a, b, alternative="two-sided")
result = interpret_p_value(p)
print("randread", "ext4-tuned", "vs", "btrfs-tuned", "p-value:", p)
print(result)
print("------------------------------------------")

# ---------- seqwrite ----------
print("Results for workload:", "seqwrite")

a = dictionary_seqwrite["ext4-default"]
b = dictionary_seqwrite["btrfs-default"]
u, p = mannwhitneyu(a, b, alternative="two-sided")
result = interpret_p_value(p)
print("seqwrite", "ext4-default", "vs", "btrfs-default", "p-value:", p)
print(result)
print("------------------------------------------")

a = dictionary_seqwrite["ext4-tuned"]
b = dictionary_seqwrite["btrfs-tuned"]
u, p = mannwhitneyu(a, b, alternative="two-sided")
result = interpret_p_value(p)
print("seqwrite", "ext4-tuned", "vs", "btrfs-tuned", "p-value:", p)
print(result)
print("------------------------------------------")

# ---------- randwrite ----------
print("Results for workload:", "randwrite")

a = dictionary_randwrite["ext4-default"]
b = dictionary_randwrite["btrfs-default"]
u, p = mannwhitneyu(a, b, alternative="two-sided")
result = interpret_p_value(p)
print("randwrite", "ext4-default", "vs", "btrfs-default", "p-value:", p)
print(result)
print("------------------------------------------")

a = dictionary_randwrite["ext4-tuned"]
b = dictionary_randwrite["btrfs-tuned"]
u, p = mannwhitneyu(a, b, alternative="two-sided")
result = interpret_p_value(p)
print("randwrite", "ext4-tuned", "vs", "btrfs-tuned", "p-value:", p)
print(result)
print("------------------------------------------")


print(" ")
print(" -")

print("Checking hypothesis 2: default vs tuned")
print("*****************************************")

# ---------- seqread ----------
print("Results for workload:", "seqread")

a = dictionary_seqread["ext4-default"]
b = dictionary_seqread["ext4-tuned"]
u, p = mannwhitneyu(a, b, alternative="two-sided")
result = interpret_p_value(p)
print("seqread", "ext4-default", "vs", "ext4-tuned", "p-value:", p)
print(result)
print("------------------------------------------")

a = dictionary_seqread["btrfs-default"]
b = dictionary_seqread["btrfs-tuned"]
u, p = mannwhitneyu(a, b, alternative="two-sided")
result = interpret_p_value(p)
print("seqread", "btrfs-default", "vs", "btrfs-tuned", "p-value:", p)
print(result)
print("------------------------------------------")

# ---------- randread ----------
print("Results for workload:", "randread")

a = dictionary_randread["ext4-default"]
b = dictionary_randread["ext4-tuned"]
u, p = mannwhitneyu(a, b, alternative="two-sided")
result = interpret_p_value(p)
print("randread", "ext4-default", "vs", "ext4-tuned", "p-value:", p)
print(result)
print("------------------------------------------")

a = dictionary_randread["btrfs-default"]
b = dictionary_randread["btrfs-tuned"]
u, p = mannwhitneyu(a, b, alternative="two-sided")
result = interpret_p_value(p)
print("randread", "btrfs-default", "vs", "btrfs-tuned", "p-value:", p)
print(result)
print("------------------------------------------")

# ---------- seqwrite ----------
print("Results for workload:", "seqwrite")

a = dictionary_seqwrite["ext4-default"]
b = dictionary_seqwrite["ext4-tuned"]
u, p = mannwhitneyu(a, b, alternative="two-sided")
result = interpret_p_value(p)
print("seqwrite", "ext4-default", "vs", "ext4-tuned", "p-value:", p)
print(result)
print("------------------------------------------")

a = dictionary_seqwrite["btrfs-default"]
b = dictionary_seqwrite["btrfs-tuned"]
u, p = mannwhitneyu(a, b, alternative="two-sided")
result = interpret_p_value(p)
print("seqwrite", "btrfs-default", "vs", "btrfs-tuned", "p-value:", p)
print(result)
print("------------------------------------------")

# ---------- randwrite ----------
print("Results for workload:", "randwrite")

a = dictionary_randwrite["ext4-default"]
b = dictionary_randwrite["ext4-tuned"]
u, p = mannwhitneyu(a, b, alternative="two-sided")
result = interpret_p_value(p)
print("randwrite", "ext4-default", "vs", "ext4-tuned", "p-value:", p)
print(result)
print("------------------------------------------")

a = dictionary_randwrite["btrfs-default"]
b = dictionary_randwrite["btrfs-tuned"]
u, p = mannwhitneyu(a, b, alternative="two-sided")
result = interpret_p_value(p)
print("randwrite", "btrfs-default", "vs", "btrfs-tuned", "p-value:", p)
print(result)
print("------------------------------------------")


print(" ")
print(" -")

print("Checking the others")
print("*****************************************")

# ---------- seqread ----------
print("Results for workload:", "seqread")

a = dictionary_seqread["btrfs-default"]
b = dictionary_seqread["ext4-tuned"]
u, p = mannwhitneyu(a, b, alternative="two-sided")
result = interpret_p_value(p)
print("seqread", "btrfs-default", "vs", "ext4-tuned", "p-value:", p)
print(result)
print("------------------------------------------")

a = dictionary_seqread["ext4-default"]
b = dictionary_seqread["btrfs-tuned"]
u, p = mannwhitneyu(a, b, alternative="two-sided")
result = interpret_p_value(p)
print("seqread", "ext4-default", "vs", "btrfs-tuned", "p-value:", p)
print(result)
print("------------------------------------------")

# ---------- randread ----------
print("Results for workload:", "randread")

a = dictionary_randread["btrfs-default"]
b = dictionary_randread["ext4-tuned"]
u, p = mannwhitneyu(a, b, alternative="two-sided")
result = interpret_p_value(p)
print("randread", "btrfs-default", "vs", "ext4-tuned", "p-value:", p)
print(result)
print("------------------------------------------")

a = dictionary_randread["ext4-default"]
b = dictionary_randread["btrfs-tuned"]
u, p = mannwhitneyu(a, b, alternative="two-sided")
result = interpret_p_value(p)
print("randread", "ext4-default", "vs", "btrfs-tuned", "p-value:", p)
print(result)
print("------------------------------------------")

# ---------- seqwrite ----------
print("Results for workload:", "seqwrite")

a = dictionary_seqwrite["btrfs-default"]
b = dictionary_seqwrite["ext4-tuned"]
u, p = mannwhitneyu(a, b, alternative="two-sided")
result = interpret_p_value(p)
print("seqwrite", "btrfs-default", "vs", "ext4-tuned", "p-value:", p)
print(result)
print("------------------------------------------")

a = dictionary_seqwrite["ext4-default"]
b = dictionary_seqwrite["btrfs-tuned"]
u, p = mannwhitneyu(a, b, alternative="two-sided")
result = interpret_p_value(p)
print("seqwrite", "ext4-default", "vs", "btrfs-tuned", "p-value:", p)
print(result)
print("------------------------------------------")

# ---------- randwrite ----------
print("Results for workload:", "randwrite")

a = dictionary_randwrite["btrfs-default"]
b = dictionary_randwrite["ext4-tuned"]
u, p = mannwhitneyu(a, b, alternative="two-sided")
result = interpret_p_value(p)
print("randwrite", "btrfs-default", "vs", "ext4-tuned", "p-value:", p)
print(result)
print("------------------------------------------")

a = dictionary_randwrite["ext4-default"]
b = dictionary_randwrite["btrfs-tuned"]
u, p = mannwhitneyu(a, b, alternative="two-sided")
result = interpret_p_value(p)
print("randwrite", "ext4-default", "vs", "btrfs-tuned", "p-value:", p)
print(result)
print("------------------------------------------")