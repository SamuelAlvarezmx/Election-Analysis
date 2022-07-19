#Add our dependencies.
import csv
import os

#Assign a variable to load a file froma a path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path

file_to_save = os.path.join("Analysis", "election_analysis.txt")

with open(file_to_load) as election_data:

#we need to use the reader function to read the csv
    file_reader = csv.reader(election_data)

#Print each row in the CSV file
    
    headers = next(file_reader)

    print(headers)
    