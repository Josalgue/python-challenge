# Import file
import os
import csv

# Set file path
pypoll = os.path.join("..", "Resources", "election_data.csv")

# Assign variables
total_votes = 0
candidates = {}
candidates_percent = {}

# Enable csv reader
with open(pypoll, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    firstrow = next(csvreader)

# Calculate votes per candidate and percentage
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
    for key, value in candidates.items():
        candidates_percent[key] = round((value/total_votes)*100,2)

# Search for the winner
winner = ""
winner_count = 0
for key in candidates.keys():
    if candidates[key] > winner_count:
        winner = key
        winner_count = candidates[key]

# Print all values in terminal
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
for key, value in candidates.items():
    print(key + ": " + str(f"{(candidates_percent[key]):.3f}") + "% (" + str(value) + ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

# Print analysis in text document
poll = open("election_results.txt", "w")
poll.write("Election Results \n")
poll.write("------------------------- \n")
poll.write("Total Votes: " + str(total_votes) + "\n")
poll.write("------------------------- \n")
for key, value in candidates.items():
    poll.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")
poll.write("------------------------- \n")
poll.write("Winner: " + winner + "\n")
poll.write("------------------------- \n")