import csv
file_to_load = "election_data.csv"
file_to_output = "election_analysis.txt"
votes = 0
total_candidates = 0
winner_votes = 0 
candidates_1 = []
candidate_votes = {}
greatest_votes = ["",0]
with open(file_to_load) as election_data :
    reader = csv.reader(election_data)
    headers = next(reader)
    
    
    for row in reader:
        
        Candidate = row[2]
    
    
        votes = votes + 1
        
        
        
        if row[2] not in candidates_1:
            candidates_1.append(Candidate)
            candidate_votes[Candidate] = 0
            
            
        
        candidate_votes[Candidate] = candidate_votes[Candidate] + 1
            
candidate_votes   
print()
print()
print()
print("Elections Results")
print("-----------------")
print("Total Votes: " + str(votes))
print("-----------------")
Stock_votes = candidate_votes["Charles Casper Stockham"]
DeGette_votes = candidate_votes["Diana DeGette"]
Doane_votes = candidate_votes["Raymon Anthony Doane"]

Stock_percent = (Stock_votes/votes)*100
Stock_percent_round = round(Stock_percent,2)
Stock_percent_round

DeGette_percent = (DeGette_votes/votes)*100
DeGette_percent_round = round(DeGette_percent,2)
DeGette_percent_round

Doane_percent = (Doane_votes/votes)*100
Doane_percent_round = round(Doane_percent,2)
Doane_percent_round

print(f'Percentage Vote for Stockham is {Stock_percent_round}% \n')
print(f'Percentage Vote for DeGette is %') 
candidate_votes
with open(file_to_output, "w") as textbox:
    summary = (f'Elections Results \n'
              f'------------------- \n'
              f'Total Votes:  +str(votes) \n'
              f'Charles Casper Stockham: {Stock_percent_round}% ({Stock_votes})\n'
              f'Diana DeGette: {DeGette_percent_round}% ({DeGette_votes})\n'
              f'Raymond Anthony Doane: {Doane_percent_round}% ({Doane_votes}) \n'
              f' --------------------\n'
              f'Winner: Diana DeGette')
    textbox.write(summary)
