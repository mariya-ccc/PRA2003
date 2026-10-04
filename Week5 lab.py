import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def calculate_momentum(px, py, pz):
    # Calculate the magnitude of the momentum vector
    momentum = math.sqrt(px**2 + py**2 + pz**2)
    return momentum


def analyse_file(file_path):

    molecule_ids = [
        211, -211, 321, -321,
        2212, -2212, 3122, -3122,
        3312, -3312, 3334, -3334
    ]

    # Store the momentum values for each molecule ID
    momenta = {}

    for molecule_id in molecule_ids:
        momenta[molecule_id] = []

    number_of_events = 0

    # Protection in case the file does not exist
    try:
        input_file = open(file_path, "r")

    except FileNotFoundError:
        print("Error: file not found:", file_path)
        return None

    with input_file:

        # Keep reading events until the file ends
        while True:

            header = input_file.readline().split()

            # Stop if there is no next header
            if len(header) == 0:
                break

            # The header tells us the event ID
            # and how many molecules follow
            event_id = int(header[0])
            number_of_molecules = int(header[1])

            # Count non-empty events
            if number_of_molecules > 0:
                number_of_events += 1

            # Read every molecule belonging to this event
            for i in range(number_of_molecules):

                molecule = input_file.readline().split()

                # Get the momentum components and molecule ID
                px = float(molecule[0])
                py = float(molecule[1])
                pz = float(molecule[2])
                molecule_id = int(molecule[3])

                # Only analyse the molecule IDs we need
                if molecule_id in momenta:

                    momentum = calculate_momentum(px, py, pz)

                    # Store this molecule's momentum
                    momenta[molecule_id].append(momentum)

    return momenta, number_of_events


def main():

    molecule_pairs = [
        (211, -211),
        (321, -321),
        (2212, -2212),
        (3122, -3122),
        (3312, -3312),
        (3334, -3334)
    ]
    # Momentum bins:
    # 0-0.1, 0.1-0.2, 0.2-0.3, ..., 49.9-50.0
    bins = np.arange(0, 50.1, 0.1)

    # Store the asymmetry results from each subsample
    all_differences = {}

    for pair in molecule_pairs:
        all_differences[pair] = []

    number_of_events_per_file = []

    # Analyse Set1 through Set10
    for i in range(1, 11):

        file_path = f"output-Set{i}.txt"

        print("Analysing", file_path)

        result = analyse_file(file_path)

        if result is None:
            return

        momenta, number_of_events = result

        number_of_events_per_file.append(number_of_events)

        # Calculate the asymmetry for every molecule pair
        for normal_id, variant_id in molecule_pairs:

            # Histogram for the normal molecule
            normal_counts, bin_edges = np.histogram(
                momenta[normal_id],
                bins=bins
            )

            # Histogram for the variant molecule
            variant_counts, bin_edges = np.histogram(
                momenta[variant_id],
                bins=bins
            )

            # Calculate the average number per event
            normal_average = normal_counts / number_of_events
            variant_average = variant_counts / number_of_events

            # Calculate the asymmetry in every momentum bin
            difference = normal_average - variant_average

            # Store the result for this subsample
            all_differences[(normal_id, variant_id)].append(
                difference
            )

    # Find the centre of each momentum bin
    bin_centres = (bins[:-1] + bins[1:]) / 2

    # Calculate the final results and make the six plots
    for normal_id, variant_id in molecule_pairs:

        differences = np.array(
            all_differences[(normal_id, variant_id)]
        )

        # Store the final mean asymmetry for each momentum bin
        mean_differences = []

        # Store the statistical uncertainty for each momentum bin
        uncertainties = []

        # Go through each momentum bin
        for bin_number in range(len(bin_centres)):

            weighted_sum = 0
            total_events = 0

            # Weighted mean using the 10 subsamples
            for i in range(10):

                weighted_sum += (
                    differences[i][bin_number]
                    * number_of_events_per_file[i]
                )

                total_events += number_of_events_per_file[i]

            mean_difference = weighted_sum / total_events

            # Statistical uncertainty from the spread
            # of the 10 subsample results
            uncertainty = stats.tstd(
                differences[:, bin_number]
            )

            mean_differences.append(mean_difference)
            uncertainties.append(uncertainty)

        # Make the plot
        plt.figure()

        plt.errorbar(
            bin_centres,
            mean_differences,
            yerr=uncertainties,
            fmt="o",
            capsize=3
        )

        plt.axhline(0)
        
        plt.xlabel("Momentum P (1e-20 kg m/s)")

        plt.ylabel("Asymmetry ΔN")

        plt.title(
            f"Asymmetry between {normal_id} and {variant_id}"
        )

        plt.show()


if __name__ == "__main__":
    main()