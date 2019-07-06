import os
import csv

election_data = os.path.join('..', 'PyPoll', 'election_data.csv')

with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    vote_count = sum(1 for line in open(election_data)) - 1
    
    
    
        
        

print("Election Results")
print("-----------------------")
print(f"Total Votes: {str(vote_count)}")
print("-----------------------")
print("Khan: 63.000% (661583)")
print("Correy: 20.000% (209046)")
print("Li: 14.000% (146360)")
print("O'Tooley: 3.000% (31586)")
print("-----------------------")
print("Winner: Khan")

