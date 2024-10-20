"""
    script: Lab6.py
    action: Calculates the number of hot dog packages and hot dog bun
            packages needed based on the number of people inputed. The output
            will be the number of hot dog packages and hot dog bun packages
            needed with the number of leftovers for each.
    author: Chris Anacker
    date: 10/20/2024
"""
import math

def main():
    """
    Action: This governs the calcultion process

    Input: None
    Output: None
    Return: None
    """
    # Named constants for the package sizes
    DOGS = 10  # Hot dogs in a package
    BUNS = 8   # Hot dog buns in a package

    # Get the total number of hot dogs needed
    total = get_total_hot_dogs()

    # Calculate leftover hot dogs
    dogs_left = (DOGS - total % DOGS) % DOGS

    # Calculate minimum packages of hot dogs
    min_dogs = math.ceil(total / DOGS)

    # Calculate leftover hot dog buns
    buns_left = (BUNS - total % BUNS) % BUNS

    # Calculate minimum packages of hot dog buns
    min_buns = math.ceil(total / BUNS)

    # Display the results
    show_results(dogs_left, min_dogs, buns_left, min_buns)

def get_total_hot_dogs():
    """
    Action: This prompts the user to input the variables that will be calculated.

    Input: a. Number of people attending
           b. Number of hotdogs per person 
    Output: None
    Return: Number of hotdogs required
    """
    people = int(input("Enter the number of people attending the cookout: "))
    hot_dogs = int(input("Enter the number of hot dogs for each person: "))
    
    total = people * hot_dogs  # Calculate total hot dogs needed
    return total

def show_results(dogs_left, min_dogs, buns_left, min_buns):
    """
    Action: Displays the results of how many packages of each are required
            and displays any leftovers.

    Input: a. dogs_left
           b. min_dogs
           c. buns_left
           d. min_buns
    Output: Prints the packages of each needed and what is left over.
    Return: None
    """
    print(f"Minimum packages of hot dogs needed: {min_dogs}")
    print(f"Minimum packages of hot dog buns needed: {min_buns}")
    print(f"Hot dogs left over: {dogs_left}")
    print(f"Hot dog buns left over: {buns_left}")

# Call the main function to execute the program
if __name__ == "__main__":
    main()
