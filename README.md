# Election-Analysis
## Overview of Election Audit
The following analysis was performed to find the number of total votes made in a recent local congressional election, getting the next information to complete this election audit:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Voter turnout for each county
7. Calculate the percentage of votes from each county out of the total count
8. Calculate the county with the highest turnout.


## Election-Audit Results
The analysis of the election data show that
* There were 369,711 votes cast in this congressional election.
* The breakdown on the percentage of votes for each county in the precinct is the following:

County Votes:
  - Jefferson: 10.5% (38,855 votes)
  - Denver: 82.8% (306,055 votes)
  - Arapahoe: 6.7% (24,801 votes)

* **Denver** was the county with the largest number of votes.
* Below is a breakdown on how was the votes cast given to each one of the candidates:
--Charles Casper Stockham--: 23.0% (85,213)
--Diana DeGette--: 73.8% (272,892)
--Raymon Anthony Doane--: 3.1% (11,606)
* Finally, after reviewing all the votes we can declare the winner of the election to be:

Winner: **Diana DeGette**

Winning Vote Count: **272,892**

Winning Percentage: **73.8%**

## Election-Audit Summary 

For this election audit it was made a particular script in Python in order to perform the analysis for this work. However this script can be considered useful for future elections and in the next few lines it will be explained why.
1. The data gathered in the analysis was sotered in an csv file, which we coded in order to read the file in our script as shown in the image below. The file_to_load and file_to_save are variables that we can modify and the whole code wouldn´t be affected because we are precisely using variables, we can change the value of the variable as much as we want to and our code is going to continue working as long as we are sure the values given fit the parameters.

<img width="494" alt="example_1" src="https://user-images.githubusercontent.com/104656920/180315025-ed1169d2-da73-4be9-b6b5-d44096c0b0dc.png">

2. It can be used not only for local elections but for many other elections. It needs only to be updated with the variables that we are performing this script, maybe rather than counties we are talking states or disctricts. The code will always perform the search of candidates and vote count for each candidate. Therefore we are talking a very powerful script that can be maleable to the needs of the client. 

<img width="579" alt="row_count_example" src="https://user-images.githubusercontent.com/104656920/180316486-8ec10b67-d68c-43ca-995c-14c2581e402b.png">
