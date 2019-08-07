# Dependencies
import os
import csv

# Path for reading csv and exporting csv file
csvpath = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("Resources", "financial_analysis.txt")

# Places to store data
months = 0
net_profits = 0
net_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999]

# Open the csv, skip header and get data from the first row
with open(csvpath, "r") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	header = next(csvreader)
	first_row = next(csvreader)
	months = months + 1
	net_profits = int(first_row[1])
	prev_month = net_profits

# Loop through the csv
	for row in csvreader:
		months = months + 1
		net_profits = net_profits + int(row[1])
		monthly_change = int(row[1]) - prev_month
		net_changes.append(monthly_change)
		prev_month = int(row[1])
		
		# Find greatest increase and decrease in monthly change
		if monthly_change > greatest_increase[1]:
			greatest_increase[0] = row[0]
			greatest_increase[1] = monthly_change
			
		if monthly_change < greatest_decrease[1]:
			greatest_decrease[0] = row[0]
			greatest_decrease[1] = monthly_change
			
# Calculate the average change over months
average_change = round(sum(net_changes) / len(net_changes), 2)

# Create output and print to terminal
output = (
	f"\nFinancial Analysis\n"
	f"---------------------------\n"
	f"Total Months: {months}\n"
	f"Total: ${net_profits}\n"
	f"Average Change: ${average_change}\n"
	f"Greatest Increase: {greatest_increase[0]} (${greatest_increase[1]})\n"
	f"Greatest Decrease: {greatest_decrease[0]} (${greatest_decrease[1]})"
)
	
print(output)

# Create text file and export
with open(output_path, "w", newline='') as txt_file:
	txt_file.write(output)
	

