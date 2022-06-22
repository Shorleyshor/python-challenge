#modules
import os
import csv



total_vote = []
voters = 0


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
        total_vote.append(int(rows[0]))

        #candidates_list.append(str(rows[2]))     

    
        voters = len(total_vote)
        #candidates = (candidates_list)
    
    
        candidate_name = rows[2]  

        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_vote[candidate_name] = 0

        candidate_vote[candidate_name] += 1


        percentage_vote_candidate = ((candidate_vote[candidate_name]) / (voters)) * 100


    



print(f'Total Votes:  {str(voters)}')
  
print(f' {candidate_vote}, {percentage_vote_candidate}')