# Data Analysis and Validation

This section outlines the process for analyzing and validating the NED-2 repeatability dataset.

This script is designed to evaluate the repeatability of a robotic system by executing a series of movements to a defined reference pose and measuring the deviation from this pose over multiple repetitions. The key steps include:

Defining a Reference Pose: Specifies a target position and orientation for the robot.
**Executing Movements:** The robot is instructed to move to the reference pose multiple times.
**Recording Final Poses:** After each movement, the final pose of the robot is recorded.
**Analyzing Deviations:** The script calculates the deviation of each final pose from the reference pose, then computes the average deviation across all repetitions.
This process helps in assessing the precision and reliability of the robot's positioning capabilities, critical aspects of robotic systems used in applications requiring high levels of accuracy.

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
