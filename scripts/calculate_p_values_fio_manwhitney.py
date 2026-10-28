from scipy.stats import mannwhitneyu

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