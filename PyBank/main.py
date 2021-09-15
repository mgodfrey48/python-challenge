# import module for file paths
import os

# import module to read csv files
import csv

# create file path
file_path = os.path.join("Resources", "budget_data.csv")

# read the csv file
with open(file_path, 'r') as csvfile:
    
    # create the csv reader
    csvreader = csv.reader(csvfile, delimiter=',')

    # remove/store the header
    csv_header = next(csvreader)
    
    # define variables for calculations
    month_count = 0
    net_profit = 0
    previous_change = 0
    total_changes = 0
    average_change = 0
    greatest_increase = 0
    best_month = ''
    greatest_decrease = 0
    worst_month = ''

    # loop through the csv file an make calculations over the entire dataset/year
    for row in csvreader:
       
        # add to the month count
        month_count += 1
        
        # set the current month and change variables
        current_change = int(row[1])
        current_month = str(row[0])
        
        # add to the net profit/loss
        net_profit += current_change
    
        # calculate different between current month's change and the preivous month's change
        # append it to the list of changes
        monthly_change = current_change - previous_change
        total_changes += monthly_change

        previous_change = current_change

        # greatest increase in profits
        if current_change > greatest_increase:
            greatest_increase = current_change
            best_month = current_month
        
        # greatest decrease in profits
        if current_change < greatest_decrease:
            greatest_decrease = current_change
            worst_month = current_month

    # calculate the average change
    average_change = round(total_changes/month_count, 2)

    # print the summary table
    print(f'Total Months: {month_count}')
    print(f'Total: ${net_profit}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {best_month} (${greatest_increase})')
    print(f'Greates Decrease in Profits: {worst_month} (${greatest_decrease})')




