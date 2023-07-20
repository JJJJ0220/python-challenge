import csv

# Initialize variables
total_months = 0
net_total = 0
changes = []
last_month_profit = None
greatest_increase = None
greatest_increase_month = None
greatest_decrease = None
greatest_decrease_month = None

# Open the CSV file
with open('/Users/jeanjin/Desktop/DSBC/4/assignment/module3/python-challenge/pybank/Resources/budget_data.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        # Count the months
        total_months += 1

        # Calculate the net total amount
        current_month_profit = int(row[1])
        net_total += current_month_profit

        # Calculate the changes
        if last_month_profit is not None:
            change = current_month_profit - last_month_profit
            changes.append(change)

            # Find the greatest increase and decrease
            if greatest_increase is None or change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = row[0]

            if greatest_decrease is None or change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = row[0]

        last_month_profit = current_month_profit

# Calculate the average change
average_change = sum(changes) / len(changes) if changes else None

# Print the results
results = (
    'Financial Analysis\n'
    '----------------------------\n'
    f'Total Months: {total_months}\n'
    f'Total: ${net_total}\n'
)
if average_change is not None:
    results += f'Average Change: ${average_change:.2f}\n'
results += (
    f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n'
    f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n'
)

print(results)

# Write the results to a text file
with open('/Users/jeanjin/Desktop/DSBC/4/assignment/module3/python-challenge/pybank/analysis/financial_analysis.txt', 'w') as f:
    f.write(results)
