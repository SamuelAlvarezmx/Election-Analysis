#Add our dependencies.
import csv
import os

#Assign a variable to load a file froma a path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path

file_to_save = os.path.join("Analysis", "election_analysis.txt")

#1 Initialize a total vote countes
total_votes = 0

#Declare a new list to encounter the candidates

candidate_options = []

#Declare a dictionary in which we will have the votes for each candidate

candidate_votes = {}

#Winning candidate and Winning Count tracker

winning_candidate = ""

winning_count = 0

winning_percentage = 0

#open the elections_results.csv and read the file

with open(file_to_load) as election_data:

#we need to use the reader function to read the csv
    file_reader = csv.reader(election_data)

#Read the header row
    
    headers = next(file_reader)

#print each row in the csv file
    for row in file_reader:

        #add the total vote count

        total_votes += 1

        #Find the candidates that ran in the election

        candidate_name = row[2]

        #Add it to the list of candidates
        if candidate_name not in candidate_options:
            #add candidate name to candidates list
            candidate_options.append(candidate_name)
            #Begin tracking that candidates vote count

            candidate_votes[candidate_name] = 0
            
            #add a vote to the candidate count

        candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes)/float(total_votes)*100

    if (votes> winning_count) and (vote_percentage > winning_percentage):
        #if true then set winning_count = votes and winning_percentage = votes_percentage
        winning_count = votes

        winning_percentage = vote_percentage
        #and, set the winning_candidate equal to the candidates name

        winning_candidate = candidate_name

    print(f"{candidate_name}: received {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"---------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning vote count: {winning_count:,}\n"
    f"Winning percentage: {winning_percentage: .1f}%\n"
    f"----------------------------"
)
print(winning_candidate_summary)

