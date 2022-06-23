#modules
import os
import csv



vote = []
total_votes = 0


Charles_count = 0
Diana_count = 0
Raymon_count = 0


# Path to collect data from the Resources folder
csvpath = os.path.join(os.path.expanduser('~'),'Desktop','python-challenge','Pypoll','Resources','election_data.csv')

# Read in the CSV file
with open(csvpath) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip header row
    header = next(csvreader)


    #loop through the data after the deader row
    for rows in csvreader:
        vote.append(int(rows[0]))

        #total votes casted
        total_votes = len(vote)

        #Count votes for diana
        if rows[2] == "Diana DeGette":
            Diana_count += 1
        #Count votes for charles
        if rows[2] == "Charles Casper Stockham":
            Charles_count += 1
        #Count votes for raymon
        if rows[2] == "Raymon Anthony Doane":
            Raymon_count += 1
        
        #calculate the percentage of votes won by each candidate 
        Diana_votes_percentage = round(((Diana_count / total_votes) * 100), 3)
        Charles_votes_percentage = round(((Charles_count / total_votes) * 100), 3)
        Raymon_votes_percentage = round(((Raymon_count / total_votes) * 100), 3)

        #candidates total votes
        Diana_vote = Diana_count
        Charles_vote = Charles_count
        Raymon_vote = Raymon_count


    
    


       

