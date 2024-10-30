'''
Script: Theater Seating
Action: The script is designed to sell tickets to a theater and keep track of the total sold and for the prices set, while keeping within the programmed number of seats 
Author: Chris Anacker
Date: 10/30/2024
'''

# Section names
SECTION_A = "A"
SECTION_B = "B"
SECTION_C = "C"

# Ticket prices for each section
PRICE_A = 20
PRICE_B = 15
PRICE_C = 10

# Number of seats for each section
SEATS_A = 300
SEATS_B = 500
SEATS_C = 200

def displayWelcome():
    '''
    Action: Displays a welcome message showing the ticket prices and number of seats available for each section
    
    Input: None
    Output: Prints the ticket prices and seat availability for each section
    Return: None
    '''
    print("Welcome to the Theater Ticketing System!")
    print(f"Section {SECTION_A}: ${PRICE_A} per seat, {SEATS_A} seats available.")
    print(f"Section {SECTION_B}: ${PRICE_B} per seat, {SEATS_B} seats available.")
    print(f"Section {SECTION_C}: ${PRICE_C} per seat, {SEATS_C} seats available.")
    print()

def getInteger(msg, section):
    '''
    Action: Prompts the user to input a value and ensures it is an integer.
    
    Input: a. msg: The message prompt for the user
           b. section: The name of the section (A, B, C)
    Output: Prompts the user and prints an error message if the input is not a valid integer
    Return: The integer value entered by the user
    '''
    # make sure the value input is of type integer otherwise an exception is thrown
    myInteger = input(msg + " " + section + ": ")
    try:
        return int(myInteger)
    except ValueError:
        print(f'{myInteger} is not a valid integer. Please try again.')
        return getInteger(msg, section)

def getTicketsSold(section_name, max_seats):
    '''
    Action: Prompts the user to enter the number of tickets sold for a specific section 
            using the getInteger function for input validation.
    
    Input: a. Section name: Name of the section (A, B, C)
           b. Maxseats: The maximum number of seats available in the section
    Output: Prompts the user for input and prints an error message if the input is invalid
    Return: The number of tickets sold
    '''
    while True:
        sold = getInteger("Enter the number of tickets sold for Section", section_name)
        if 0 <= sold <= max_seats:
            return sold
        else:
            print(f"Invalid input: Please enter a number between 0 and {max_seats}.")

def calculateIncome(tickets_sold, ticket_price):
    '''
    Action: Calculates the income generated for a specific section
    
    Input: a. Tickets sold: The number of tickets sold for the section
           b. Ticket price: The price per ticket for the section
    Output: None
    Return: The total income generated for the section.
    '''
    return tickets_sold * ticket_price

def displaySubtotal(section_name, tickets_sold, income):
    '''
    Action: Displays the subtotal for a specific section
    
    Input: a. Section Name: Name of the section
           b. Tickets sold: The number of tickets sold in the section
           c. Income: The total income generated from the section
    Output: Prints the subtotal for the section.
    Return: None
    '''
    print(f"Section {section_name}: {tickets_sold} tickets sold, Income: ${income}")

def main():
    '''
    Action: Controls the flow of the program by gathering input, calculating income,
            and displaying subtotals and total income
    
    Input: User input for the number of tickets sold for each section
    Output: Displays welcome message, subtotals after each section, and final total income
    Return: None
    '''
    displayWelcome()

    # Collect tickets sold for each section
    sold_A = getTicketsSold(SECTION_A, SEATS_A)
    sold_B = getTicketsSold(SECTION_B, SEATS_B)
    sold_C = getTicketsSold(SECTION_C, SEATS_C)

    # Calculate income for each section
    income_A = calculateIncome(sold_A, PRICE_A)
    income_B = calculateIncome(sold_B, PRICE_B)
    income_C = calculateIncome(sold_C, PRICE_C)

    # Display subtotals for each section
    print("\nSubtotals:")
    displaySubtotal(SECTION_A, sold_A, income_A)
    displaySubtotal(SECTION_B, sold_B, income_B)
    displaySubtotal(SECTION_C, sold_C, income_C)

    # Calculate and display total income
    total_income = income_A + income_B + income_C
    print("\nTotal income from all sections: $", total_income)

# Run the program
if __name__ == "__main__":
    main()
