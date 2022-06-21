#modules
import os
import csv



total_vote = []
voters = 0
candidates_list = []
candidates = 0
percentage_vote_candidate = 0
each_candidate_vote = 0
winner = 0
candidate1 = int(Diana DeGette)


# Path to collect data from the Resources folder
csvpath = os.path.join(os.path.expanduser('~'),'Desktop','python-challenge','Pypoll','Resources','election_data.csv')

# Read in the CSV file
with open(csvpath) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    #loop through the data after the deader row
    for rows in csvreader:
        total_vote.append(int(rows[0]))

        candidates_list.append(str(rows[2]))     

        

    voters = len(total_vote)
    candidates = len(candidates_list)
  
        

    print(f'Total Votes:  {str(voters)}')
    #print(f' {candidates}')