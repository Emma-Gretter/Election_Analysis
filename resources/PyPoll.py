# add our dependancies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

#Initialize a total vote counter
total_votes=0
#candidate options
candidate_options = []
#Declare dictionary
candidate_votes = {}
# Winning candidate and winnig count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0 

#Open the election results and read the file.
with open(file_to_load) as election_data:
  
    # read the file object with the reader function. 
    file_reader = csv.reader(election_data)
       # Print the header row
    headers = next(file_reader)
    # print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        
   # print the candidate name from each list 
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
         # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
        # 4. Print the candidate name and percentage of votes.
        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    winning_candidate_summary = (
            f'_______________________\n'
            f'Winner: {winning_candidate}\n'
            f'Winning Vote Count: {winning_count:,}\n'
            f'Winning Percentage: {winning_percentage:.1f}%\n'
            f'-----------------------\n')
    print(winning_candidate_summary)   






#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
# 4. The total number of votes each condidate won
# #5. The winner of the election based on popular vote 

