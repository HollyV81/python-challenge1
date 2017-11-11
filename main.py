

import csv

poll_csv='election_data_2.csv'

total_votes=0
candidtates={}
vote_coutnt={}


with open(poll_csv,"r") as poll:
    csvreader=csv.DictReader(poll)

    for row in csvreader:
    	total_votes +=1
    	if row ['Candidate'] not in candidates:
    		candidates.append(row['Candidate'])
    		vote_coutnt(row{'Candidate'})=1
    	elif row ['Candidate']	in candidates:
    		vote_coutnt(row{'Candidate'}) += 1

    		



