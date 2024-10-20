"The main Function"
def main():
    keepGoing = 'y'

    while keepGoing == 'y':
        totalBottles = getBottles()
        totalPayout = calcPayout(totalBottles)
        printInfo(totalBottles, totalPayout)
        keepGoing = input('Do you want to run the program again? (Enter y or n): ')

"this function will get the number of bottles returned"
def getBottles():
    totalBottles = 0
    todayBottles = 0
    counter = 1
    while counter <= 7:
        todayBottles = int(input('Enter number of bottles for today: '))
        totalBottles = totalBottles + todayBottles
        counter = counter + 1
    return totalBottles

"this function will calculate the payout"
def calcPayout(totalBottles):
    totalPayout = 0
    totalPayout = totalBottles * .10
    return totalPayout

"this function will display the information"
def printInfo(totalBottles, totalPayout):
    print(f'The total number of bottles collected is'), totalBottles
    print(f'The total paid out is ${totalPayout:.2f}'), totalPayout

main()
