#modules
import os
import csv



vote = []
total_votes = 0


percentage_vote_candidate = {}
each_candidate_vote = 0
winner = 0
candidate_name = []
candidate_vote = {}
candidates = []


# Path to collect data from the Resources folder
csvpath = os.path.join(os.path.expanduser('~'),'Desktop','python-challenge','Pypoll','Resources','election_data.csv')

# Read in the CSV file
with open(csvpath) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)


    #loop through the data after the deader row
    for rows in csvreader:
        vote.append(int(rows[0]))

        #total votes casted
        total_votes = len(vote)

            

    
    


       



print(f'Total Votes:  {str(total_votes)}')
  
