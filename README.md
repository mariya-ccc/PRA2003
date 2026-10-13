# PRA2003


# Introduction

This project focuses on analysing simulated molecular emissions in a combustion reaction using Python.
The aim is to investigate how frequently different molecular species occur, whether there is an asymmetry between normal molecules and their corresponding variants, and whether this asymmetry changes as a function of momentum. The analysis was performed using 10 output files containing approximately 5 million simulated events in total.



# Installation 

- Python version 3.14 used
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

Table 1.0 



# Methodology and Results 


QUESTION 1:  What are the average counts of each molecular species and their statistical uncertainties?


For each of the 10 subsamples, the total number of times each molecular species occurred was counted. The average count was then calculated by dividing the total count of each molecular species by the number of non-empty events in that subsample.

This gave 10 average counts for each molecular species, one from each subsample. The weighted mean of these 10 averages to obtain the final average count. A weighted mean was used because the subsamples did not all contain the same number of events, so subsamples with more events contributed more to the final average.

The statistical uncertainty was determined from the sample standard deviation of the 10 subsample averages, using stats.tstd() from SciPy.


| Molecule ID | Average count per non-empty event | Statistical uncertainty |
|---|---:|---:|
| 211 | 19.949508 | 0.032746 |
| -211 | 19.917211 | 0.031873 |
| 321 | 2.509148 | 0.004774 |
| -321 | 2.503457 | 0.005504 |
| 2212 | 1.208034 | 0.001896 |
| -2212 | 1.184161 | 0.002412 |
| 3122 | 0.276599 | 0.001074 |
| -3122 | 0.271696 | 0.000985 |
| 3312 | 0.039441 | 0.000284 |
| -3312 | 0.039000 | 0.000402 |
| 3334 | 0.001187 | 0.000042 |
| -3334 | 0.001152 | 0.000051 |









  
