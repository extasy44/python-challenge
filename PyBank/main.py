import os
import csv

budget_csv = os.path.join('.', 'resources', 'budget_data.csv')

# declare list varaibles to hold data
months = []
profit = []
total_profit = 0
monthly_change = []
greatest_increase = { 'month' : '', 'profit' : 0 }
greatest_decrease = { 'month' : '', 'profit' : 0 }

# open csv file
with open(budget_csv) as csv_file:
  csv_reader = csv.reader(csv_file, delimiter = ',')

  # set the header from the first row
  header = next(csv_reader)

  # add values to each list and calculate total profit
  for row in csv_reader:
    months.append(row[0]) 
    profit.append(int(row[1]))
    total_profit += int(row[1])

  # calculate monthly change and add it to list
  for x in range(len(profit)-1):
    change = profit[x+1] - profit[x]
    monthly_change.append(change)

    if ( change > greatest_increase['profit']):
      greatest_increase['profit'] = change
      greatest_increase['month'] = months[x + 1]
    
    if ( change < greatest_decrease['profit']):
      greatest_decrease['profit'] = change
      greatest_decrease['month'] = months[x + 1]


# Print values_staments

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}")
print(f"Greatest Increase in Profits: {greatest_increase['month']} (${greatest_increase['profit']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['month']} (${greatest_decrease['profit']})")

#output file
output_file = os.path.join(".",".","analysis.txt" )

with open(output_file,"w") as txtfile:

   txtfile.write(f"Financial Analysis")
   txtfile.write("\n")
   txtfile.write(f"---------------------------")
   txtfile.write("\n")
   txtfile.write(f"Total Months: {len(months)}")
   txtfile.write("\n")
   txtfile.write(f"Total: ${total_profit}")
   txtfile.write("\n")
   txtfile.write(f"Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}")
   txtfile.write("\n")
   txtfile.write(f"Greatest Increase in Profits: {greatest_increase['month']} (${greatest_increase['profit']})")
   txtfile.write("\n")
   txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease['month']} (${greatest_decrease['profit']})")
