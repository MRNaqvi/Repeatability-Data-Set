# Data Analysis and Validation

This section outlines the process for analyzing and validating the NED-2 repeatability dataset.

## Repeatability Capability Data Analysis

Given a NED-2 repeatability dataset `D` consisting of `N` samples, our objective is to divide this dataset into `k` equal sets for analysis, where `k = 4`. Let `D_i` represent the `i^{th}` set. The division process is as follows:

### Data Ordering

Ensure all samples in `D` maintain their original order.

### Set Division

For each sample `n` in `D`, assign it to set `D_i`, where `i = n mod k` and `i` belongs to the set [0, k-1].

#### Standard Deviation Calculation for Each Set

The standard deviation (SD) for each set `D_i` is calculated using the formula:

SD(D_i) = sqrt((1/(N_i - 1)) * sum((x_j - x̄)^2 from j=1 to N_i))

where:

- `N_i` is the number of samples in set `D_i`,
- `x_j` is the `j^{th}` sample in set `D_i`,
- `x̄` is the mean of all samples in `D_i`.

#### Pooled Standard Deviation Calculation

The pooled standard deviation (`SD_pooled`) is calculated by combining the variances of all `k` sets, weighted by their degrees of freedom (`N_i - 1`), and then taking the square root. The formula is:
