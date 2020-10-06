# Import file
import os
import csv

# Set file path
pybank_csv = os.path.join("..", "Resources", "budget_data.csv")

# Assign variables
total_months = 0
total_rev = 0
month_count = []
changes =[]
max_inc = 0
max_inc_month = 0
max_dec = 0
max_dec_month = 0

# Enable csv reader
with open(pybank_csv, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    row = next(csvreader)

# Calculate the total number of months and total revenue
    total_months = total_months + 1
    previous_profit = int(row[1])
    for row in csvreader:
        total_months = total_months + 1
        total_rev = total_rev + int(row[1])

# Calculate monthly change
        change = int(row[1]) - previous_profit
        changes.append(change)
        previous_profit = int(row[1])
        month_count.append(row[0])
        
# Calculate the max increase
        if int(row[1]) > max_inc:
            max_inc = int(row[1])
            max_inc_month = row[0]
            
# Calculate the max decrease
        if int(row[1]) < max_dec:
            max_dec = int(row[1])
            max_dec_month = row[0]  
      
# Calculate the average change
    average_change = sum(changes)/len(changes)
    high = max(changes)
    low = min(changes)

# Print all values in terminal
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months:" + str(total_months))
    print("Total Amount:" + str(total_rev))
    print(average_change)
    print(max_inc_month, max(changes))
    print(max_dec_month, min(changes))

# Print analysis in text document
    bank = open("analysis.txt","w+")
    bank.write("Financial Analysis") 
    bank.write('\n' +"-------------------------")
    bank.write('\n' +"Total Months: " + str(total_months)) 
    bank.write('\n' +"Total: $" + str(total_rev)) 
    bank.write('\n' +"Average Change: $" + str(f"{average_change:.2f}")) 
    bank.write('\n' +"Greatest Increase in Profits: " + str(max_inc_month))
    bank.write(" $" +str(high))
    bank.write('\n' +"Greatest Decrease in Profits: " + str(max_dec_month))
    bank.write(" $" + str(low))   