# PRA2003


# Introduction

This project focuses on analysing simulated molecular emissions in a combustion reaction using Python.
The aim is to investigate how frequently different molecular species occur, whether there is an asymmetry between normal molecules and their corresponding variants, and whether this asymmetry changes as a function of momentum. The analysis was performed using 10 output files containing approximately 5 million simulated events in total.



# Installation 

- Python version 3.14
- Libraries needed:
         - math
         - Numpy
         - SciPy
         - Matplotlib


# Research questions

Q1. What are the average counts of each molecular species and their statistical uncertainties?

-> How frequently does each molecule appear across simulations 

Q2. Is there any asymmetry between the normal and variant molecules?

-> Compare production counts of each normal molecule 

Q3. Is there any asymmetry as a function of their momentum?

-> Whether or not the measured differences changes as the molecule`s momentum changes 

# Dataset

The dataset contains simulated molecular emissions from a combustion reaction.
It consists of 10 output files, each containing approximately 500,000 simulated events, giving approximately 5 million events in total.
Each event contains a header specifying the event ID and the number of molecules produced.

Each molecule is represented by four values:
- px: Momentum component along the x-axis.
- py: Momentum component along the y-axis.
- pz: Momentum component along the z-axis.
- molecule_id: Integer identifying the molecular species.



The following 12 molecules were analysed: 

Molecule IDs:


| Molecule ID | Molecule type |
|------------:|---------------|
| 211 | Carbon monoxide |
| -211 | Carbon-13 monoxide |
| 321 | Nitric oxide |
| -321 | Ionised NO |
| 2212 | Water |
| -2212 | Heavy water (D₂O) |
| 3122 | Methane (CH₄) |
| -3122 | Methyl ion (CH₃⁻) |
| 3312 | Ethylene (C₂H₄) |
| -3312 | Ionised ethylene (C₂H₃⁻) |
| 3334 | Ozone (O₃) |
| -3334 | Superoxide anion (O₂⁻) |

## Table 1.0 



# Methodology and Results 


QUESTION 1:  What are the average counts of each molecular species and their statistical uncertainties?


For each of the 10 subsamples, the total number of times each molecular species occurred was counted. The average count was then calculated by dividing the total count of each molecular species by the number of non-empty events in that subsample.

This gave 10 average counts for each molecular species, one from each subsample. The weighted mean of these 10 averages to obtain the final average count. A weighted mean was used because the subsamples did not all contain the same number of events, so subsamples with more events contributed more to the final average. 


The statistical uncertainty was determined from the sample standard deviation of the 10 subsample averages, using stats.tstd() from SciPy. This represents the spread of the results between the different subsamples. See Table 2.0. 


Average counts and statistical uncertainties of molecular species:

| Molecule ID | Average count ± Statistical uncertainty |
|---|---:|
| 211 | 19.9495079355902 ± 0.032746188172178115 |
| -211 | 19.917211221411552 ± 0.0318733428247216 |
| 321 | 2.5091478051179377 ± 0.004773688071794738 |
| -321 | 2.5034568047201455 ± 0.0055036861832087145 |
| 2212 | 1.208034096197201 ± 0.00189633025524925 |
| -2212 | 1.1841609547697451 ± 0.0024121635255373386 |
| 3122 | 0.2765985136833252 ± 0.0010743980330262981 |
| -3122 | 0.27169595103327354 ± 0.0009853787552934238 |
| 3312 | 0.03944115982852291 ± 0.00028367599331215285 |
| -3312 | 0.039000492205163585 ± 0.00040248313321916235 |
| 3334 | 0.0011870957794868897 ± 4.16761469955214e-05 |
| -3334 | 0.001151582516474148 ± 5.079386816876298e-05 |

### Table 2.0



QUESTION 2 : Is there any asymmetry between the normal and the
variant molecule?


A comparison of each normal molecule with its corresponding variant was made. For each of the 10 subsamples, the difference between the average counts of each molecular pair was calculated.

The difference was calculated as the average count of the normal molecule minus the average count of its variant.

The weighted mean of these 10 differences was then calculated. This gives the final measured asymmetry between the normal and variant molecule.

A positive diffierence means that, on average, the normal molecule occurred more often than its variant. The standard deviation of the 10 differences was used as the statistical uncertainty.

How do we know if the asymmetry is meaningful? :

I compared the difference with its uncertainty using:

significance = |D| / σ_D


The absolute value is used because significance measures the magnitude of the difference relative to zero, regardless of whether the difference is positive or negative. A difference of zero corresponds to no measured asymmetry.

The measured asymmetries, statistical uncertainties, and significances for the six molecular pairs are presented below (Table 3.0)


Asymmetry between normal and variant molecules

| Molecule pair | Average difference | Uncertainty | Significance |
|---|---:|---:|---:|
| 211 vs -211 | 0.03229671417864928 | 0.0045187006346247265 | 7.1473453964120575σ |
| 321 vs -321 | 0.005691000397791801 | 0.003293674238156648 | 1.7278577012451757σ |
| 2212 vs -2212 | 0.023873141427455603 | 0.002372770396324402 | 10.06129436899452σ |
| 3122 vs -3122 | 0.0049025626500516645 | 0.0005831593400970446 | 8.406900675269679σ |
| 3312 vs -3312 | 0.00044066762335932374 | 0.00048793089398757654 | 0.9031353185243151σ |
| 3334 vs -3334 | 3.551326301274172e-05 | 6.854374209958842e-05 | 0.518110945287228σ |

### Table 3.0


QUESTION 3: Is there any asymmetry as a function of their momentum?


To investigate whether the asymmetry between normal and variant molecules depends on momentum, the momentum of each molecular species was analysed across the 10 subsamples.

First, the magnitude of the momentum of each molecule was calculated using its three momentum components:

First, the magnitude of the momentum of each molecule was calculated using its three momentum components:

$$
P = \sqrt{p_x^2 + p_y^2 + p_z^2}
$$

where $p_x$, $p_y$, and $p_z$ are the momentum components in the x, y, and z directions.

The momentum values were then divided into 20 bins, ranging from 0 to 20, with a bin width of 1.


For each subsample, the number of normal and variant molecules in each momentum bin were counted. The difference in each momentum bin was calculated by subtracting the number of variant molecules from the number of normal molecules in that bin. This gave 10 differences for each momentum bin, one from each subsample.

The statistical uncertainty was estimated using the sample standard deviation of these 10 differences. This represents the spread of the measured differences between the subsamples.

Finally, the mean difference against momentum for each of the six molecular pairs, including error bars representing their statistical uncertainties was plotted. This gave 6 resulting graphs, one for each molecular pair (See all png files in repository). 



**211 vs −211:** Significant asymmetry, as the differences are mostly positive and particularly large at lower momentum values, with several error bars not overlapping zero.

**321 vs −321:** Insignificant asymmetry, as most error bars overlap zero and the differences show no clear trend.

**2212 vs −2212:** Significant asymmetry, as the differences are consistently positive and generally decrease with increasing momentum.

**3122 vs −3122:** Significant asymmetry, particularly at lower momentum values, where several error bars do not overlap zero.

**3312 vs −3312:** Insignificant asymmetry, as the differences are small compared with their uncertainties and most error bars overlap zero.

**3334 vs −3334:** Insignificant asymmetry, as the differences fluctuate around zero and all error bars overlap zero.












  
