#modules
import os
import csv


total_months = 0
net_profitLosses = 0
average_profitLoss = 0
months = []
profit = []
months_change = []
greatest_increase = []

# Path to collect data from the Resources folder
csvpath = os.path.join(os.path.expanduser('~'),'Desktop','python-challenge','PyBank','Resources','budget_data.csv')

# Read in the CSV file
with open(csvpath) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

  

    #loop through the data after the deader row
    for rows in csvreader:
        profit.append(int(rows[1]))
        months.append(rows[0])
        
        
    
    total_months = len(months)

    net_profitLosses = int(sum(profit))
    
    # to find the changes in profit/loss over the entire period
    profit_loss_change = []

    #use for loop to calculate the changes between the current value on the list and the previous value on the list
    for change in range(1, len(profit)):
        profit_loss_change.append(int(profit[change]) - int(profit[change - 1]))

        
        # calculate the average change in profits/losses

        average_profitLoss = round(sum(profit_loss_change) / len(profit_loss_change), 2)

        # calculate the greatest increase in profits (date and amount) over the entire period
        greatest_increase = max(profit_loss_change)
    

        # calculate the greatest decrease in profits (date and amount) over the entire period
        greatest_decrease = min(profit_loss_change)


    for rows in csvreader:

        if  greatest_increase is int(rows[1]):
               months_change == int(rows[0])
            












    print(f' Total Months:  {str(total_months)}')

    print(f' Total: ${str(net_profitLosses)}')

    print(f' Average Change: ${str(average_profitLoss)}')

    print(f' Greatest Increase in Profits: ${greatest_increase}')

    print(f' Greatest Decrease in Profits: ${greatest_decrease}')
    print(f' {months_change}')

