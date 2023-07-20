import csv

# Initialize the vote counter as a dictionary
votes = {}

# Open the CSV file
with open('/Users/jeanjin/Desktop/DSBC/4/assignment/module3/python-challenge/pypoll/Resources/election_data.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        # Count the votes
        candidate = row[2]
        if candidate in votes:
            votes[candidate] += 1
        else:
            votes[candidate] = 1

# Calculate the total number of votes cast
total_votes = sum(votes.values())

# Calculate the winner
winner = max(votes, key=votes.get)

# Prepare the results
results = (
    'Election Results\n'
    '-------------------------\n'
    f'Total Votes: {total_votes}\n'
    '-------------------------\n'
)
for candidate, vote in votes.items():
    percentage = (vote / total_votes) * 100
    results += f'{candidate}: {percentage:.3f}% ({vote})\n'
results += (
    '-------------------------\n'
    f'Winner: {winner}\n'
    '-------------------------\n'
)

# Print the results
print(results)

# Write the results to a text file
with open('/Users/jeanjin/Desktop/DSBC/4/assignment/module3/python-challenge/pypoll/analysis/election_results.txt', 'w') as f:
    f.write(results)
