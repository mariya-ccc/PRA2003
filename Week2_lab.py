import math # import math module to use the sqrt function


def calculate_momentum(px, py, pz): 
   momentum = math.sqrt(px**2 + py**2 + pz**2)  # Calculate the magnitude of the momentum vector
   return momentum

def main(): # Define the function that reads the file and prints the results 
    file_path = "output-Set0.txt" # Define the path to the input data

    with open(file_path, "r") as input_file:
        
        header = input_file.readline().split() # Read and split the event header  
        event_id = int(header[0])  # Convert the first header value into an integer: the event ID
        number_of_molecules = int(header[1]) # Get the number of molecules in the event

        
        for i in range(number_of_molecules): # Repeat the following steps once for each molecule
            molecule = input_file.readline().split()   # Read the next row and store its four text values in a list

              # Convert the momentum components from text to numbers

            px = float(molecule[0]) 
            py = float(molecule[1]) 
            pz = float(molecule[2]) 
            molecule_id = int(molecule[3]) # Convert the molecule ID to an integer


            
            momentum = calculate_momentum(px, py, pz) # Call the function to calculate this molecule's momentum magnitude
            print(f"ID: {molecule_id} Total Momentum: {momentum}")


if __name__ == "__main__": # Check if the python file is being run directly 
    main()

