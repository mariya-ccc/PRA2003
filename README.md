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








  
