from scipy import stats


def analyse_file(file_path):

    molecule_ids = [
        211, -211, 321, -321,
        2212, -2212, 3122, -3122,
        3312, -3312, 3334, -3334
    ]

    # Give each ID a starting count of zero
    molecule_counts = {}

    for molecule_id in molecule_ids:
        molecule_counts[molecule_id] = 0

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

            # Only count events that contain molecules
            if number_of_molecules > 0:
                number_of_events += 1

            # Read every molecule belonging to this event
            for i in range(number_of_molecules):

                molecule = input_file.readline().split()

                # The fourth value is the molecule ID
                molecule_id = int(molecule[3])

                # Count if it is an ID from our list
                if molecule_id in molecule_counts:
                    molecule_counts[molecule_id] += 1

    # Calculate the average for each molecule in this subsample
    averages = {}

    for molecule_id in molecule_ids:

        total = molecule_counts[molecule_id]

        average = total / number_of_events

        averages[molecule_id] = average

    # Return both the averages and the size of this subsample
    return averages, number_of_events


def main():

    molecule_ids = [
        211, -211, 321, -321,
        2212, -2212, 3122, -3122,
        3312, -3312, 3334, -3334
    ]

    # Store the averages from all 10 subsamples
    all_averages = {}

    for molecule_id in molecule_ids:
        all_averages[molecule_id] = []

    # Store the number of events in each subsample
    number_of_events_per_file = []

    # Analyse Set1 through Set10
    for i in range(1, 11):

        file_path = f"output-Set{i}.txt"

        print("Analysing", file_path)

        result = analyse_file(file_path)

        if result is None:
            return

        averages, number_of_events = result

        # Store the number of events in this subsample
        number_of_events_per_file.append(number_of_events)

        # Store the average from this subsample
        for molecule_id in molecule_ids:

            all_averages[molecule_id].append(
                averages[molecule_id]
            )


    # QUESTION 1

    print()
    print("QUESTION 1")
    print()
    print(f"{'ID':>6} {'Average':>14} {'Statistical uncertainty':>25}")

    for molecule_id in molecule_ids:

        # Get the 10 results for this molecule
        subsample_results = all_averages[molecule_id]

        # Calculate the weighted average
        weighted_sum = 0
        total_events = 0

        for i in range(10):

            weighted_sum += (
                subsample_results[i]
                * number_of_events_per_file[i]
            )

            total_events += number_of_events_per_file[i]

        average = weighted_sum / total_events

        # Standard deviation of the subsample results
        # gives the statistical uncertainty
        uncertainty = stats.tstd(subsample_results)

        print(
            f"{molecule_id:>6} "
            f"{average:>14} ± {uncertainty}"
        )


    # QUESTION 2

    # Is there any asymmetry between normal and variant molecules?

    molecule_pairs = [
        (211, -211),
        (321, -321),
        (2212, -2212),
        (3122, -3122),
        (3312, -3312),
        (3334, -3334)
    ]

    print()
    print("QUESTION 2")
    print()
    print("Asymmetry between normal and variant molecules")
    print()

    for normal_id, variant_id in molecule_pairs:

        # Store the difference from each subsample
        differences = []

        # Calculate the difference separately
        # for each of the 10 subsamples
        for i in range(10):

            difference = (
                all_averages[normal_id][i]
                - all_averages[variant_id][i]
            )

            differences.append(difference)

        # Calculate the weighted mean difference
        weighted_sum = 0
        total_events = 0

        for i in range(10):

            weighted_sum += (
                differences[i]
                * number_of_events_per_file[i]
            )

            total_events += number_of_events_per_file[i]

        average_difference = weighted_sum / total_events

        # The spread of the 10 subsample differences
        # gives the statistical uncertainty
        uncertainty_difference = stats.tstd(differences)

        # Compare the difference with its uncertainty
        significance = (
            abs(average_difference)
            / uncertainty_difference
        )

        print(
            normal_id, "vs", variant_id,
            ":", average_difference,
            "±", uncertainty_difference,
            "| significance =", significance
        )


if __name__ == "__main__":
    main()