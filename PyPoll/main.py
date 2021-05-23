import os
import csv

election_csv = os.path.join('.', 'resources', 'election_data.csv')

# reader and open data source file from path
with open(election_csv) as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')

  # set dict to hold a number of votes for each candidate
  total_votes = 0
  votes = {}

  # Read the header
  header= next(csv_reader)

  # Count vote for each candidate using dict
  for row in csv_reader:
    total_votes += 1 # set total number of votes cast
    if row[2] in votes: # Set The total number of votes each candidate won
      votes[row[2]] += 1 
    else :
      votes[row[2]] = 1

# Calculate the percentage of votes for each candidate won
percent_khan = round(votes['Khan'] / total_votes * 100, 3)
percent_correy = round(votes['Correy'] / total_votes * 100, 3)
percent_li = round(votes['Li'] / total_votes * 100, 3)
percent_otooley = round(votes["O'Tooley"] / total_votes * 100, 3)
otooley_vote = votes["O'Tooley"]

max_key = max(votes, key=votes.get)

# Print values_staments
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Khan: {percent_khan:.3f}% ({votes['Khan']})")
print(f"Correy: {percent_correy:.3f}% ({votes['Correy']})")
print(f"Li: {percent_li:.3f}% ({votes['Li']})")
print(f"O'Tooley: {percent_otooley:.3f}% ({ otooley_vote })")
print(f"---------------------------")
print(f"Winner: {max_key}")
print(f"---------------------------")

#output file
output_file = os.path.join(".",".","analysis.txt" )

with open(output_file,"w") as txtfile:
  txtfile.write(f"Election Results")
  txtfile.write("\n")
  txtfile.write(f"---------------------------")
  txtfile.write("\n")
  txtfile.write(f"Total Votes: {total_votes}")
  txtfile.write("\n")
  txtfile.write(f"---------------------------")
  txtfile.write("\n")
  txtfile.write(f"Khan: {percent_khan:.3f}% ({votes['Khan']})")
  txtfile.write("\n")
  txtfile.write(f"Correy: {percent_correy:.3f}% ({votes['Correy']})")
  txtfile.write("\n")
  txtfile.write(f"Li: {percent_li:.3f}% ({votes['Li']})")
  txtfile.write("\n")
  txtfile.write(f"O'Tooley: {percent_otooley:.3f}% ({ otooley_vote })")
  txtfile.write("\n")
  txtfile.write(f"---------------------------")
  txtfile.write("\n")
  txtfile.write(f"Winner: {max_key}")
  txtfile.write("\n")
  txtfile.write(f"---------------------------")




