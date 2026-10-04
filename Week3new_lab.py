
import math 

def main(): # Define the function that reads the file and prints the results 

    file_path = "output-Set1.txt"

    molecule_ids = [211, -211, 321, -321, 2212, -2212, 3122, -3122, 3312, -3312, 3334, -3334] # 12 molecule IDs needed in results 

    # Give each ID a starting count of zero
    molecule_counts = {}
    for molecule_id in molecule_ids:
        molecule_counts[molecule_id] = 0

    number_of_events = 0 

     # Protection in case the file does not exist
    try:
        input_file = open(file_path, "r")
    except FileNotFoundError:
        print("Error: file not found.")
        return
    
    with input_file:

        # Keep reading events until the file ends
        while True:  

            header = input_file.readline().split()

            # Stop if there is no next header
            if len(header) == 0: 
                    break


           # The header tells us the event ID and how many molecules follow

            event_id = int(header[0])
            number_of_molecules = int(header[1])

            # Add 1 to the event count if this event has molecules
            if number_of_molecules > 0:
                number_of_events += 1
            
            # Read every molecule belonging to this event
            for i in range(number_of_molecules):  

                molecule = input_file.readline().split()

                    # The fourth value is the molecule ID; convert it from text to an integer
                molecule_id = int(molecule[3]) 

                     # Count if it is an ID from our list
                if molecule_id in molecule_counts:
                    molecule_counts[molecule_id] += 1



    # Print the results after reading the whole file        
    print(f"{'ID':>6} {'Average':>14} {'Standard deviation':>20}")

    for molecule_id in molecule_ids:  
        # Find how many times this ID appeared
        total = molecule_counts[molecule_id]

        # Calculate the average per event that had molecules
        average = total / number_of_events

        # Calculate the standard deviation     
        standard_deviation = math.sqrt(average) 
    

        print(f"{molecule_id:>6} {average} ± {standard_deviation}")
              

if __name__ == "__main__":
    main()