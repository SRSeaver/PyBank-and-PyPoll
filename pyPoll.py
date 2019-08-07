# Dependencies
import os
import csv

# Place to store data
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
most_votes = 0

# Input and output files
input_file = os.path.join("Resources", "election_data.csv")
output_file = os.path.join("Resources", "election_results.txt")

# Load the file
with open(input_file, "r", newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	header = next(csvreader)
	# print(header)
	
	# Loop through the data, count total votes and get candidates
	for row in csvreader:
		total_votes = total_votes + 1
		candidate = row[2]
		
		# Start counting votes for candidates
		if candidate not in candidate_options:
			candidate_options.append(candidate)
			candidate_votes[candidate] = 0
			
		candidate_votes[candidate] = candidate_votes[candidate] + 1

# Print results to terminal and save to file
with open(output_file, "w", newline="") as txt_file:

	# Election results 
	election_total = (
	f"\nElection Results\n"
	f"---------------------------\n"
	f"Total Votes: {total_votes}\n"
	f"---------------------------")
	
	# Print and save election results
	print(election_total)
	txt_file.write(election_total)
	
	# Find vote percentages
	for candidate in candidate_votes:
		votes = candidate_votes.get(candidate)
		candidate_percentage = float(votes) / float(total_votes) * 100
		
		vote_percentage = (
			f"{candidate}: {candidate_percentage:.3}% {votes}")
		
		# Print and save vote percentages
		print(vote_percentage)
		txt_file.write(vote_percentage)
		
		# Find the winner
		if votes > most_votes:
			most_votes = votes
			winning_candidate = candidate
			
	election_winner = (
		f"---------------------------\n"
		f"Winner: {winning_candidate}\n"
		f"---------------------------\n")
				
	# Print and save winner
	print(election_winner)
	txt_file.write(election_winner)
		
	
		
		
		
	

		
		