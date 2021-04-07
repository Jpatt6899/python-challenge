
import csv
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

os.chdir(dir_path)

file = '../resources/py_poll.csv'

voter_ID = []
county = []
candidate = []
total_votes = 0
candidate_search = []
candidate_votes = {}
vote_split = []
cname = []

with open(file,encoding="utf-8") as pypoll:

   csvreader = csv.reader(pypoll, delimiter=',')

   header = next(csvreader)
   

   for row in csvreader:
       voter_ID.append(row[0])
       county.append(row[1])
       cname.append(row[2])

       
       total_votes = total_votes + 1

       candidate_name = (row[2])
       
       
       if candidate_name not in candidate_search:
      
        candidate_search.append(candidate_name)
        candidate_votes [candidate_name ] = 0
       candidate_votes [candidate_name] = candidate_votes[candidate_name] + 1
       
       vote_split = list(candidate_votes.values())
       all_candidates = list(candidate_votes.keys())
       
   
   name_1 = all_candidates[0]
   name_2 = all_candidates[1]
   name_3 = all_candidates[2]
   name_4 = all_candidates[3]
      
       
   khan_votes = vote_split[0]
   correy_votes = vote_split[1]
   li_votes = vote_split[2]
   otooley_votes = vote_split[3]

   khan_percentage = (khan_votes/total_votes)*100
   round_percent_khan = round(khan_percentage)
   correy_percentage = (correy_votes/total_votes)*100 
   round_percent_correy = round(correy_percentage)
   li_percentage = (li_votes/total_votes)*100
   round_percent_li = round(li_percentage)
   otooley_percentage = (otooley_votes/total_votes)*100
   round_percent_otooley = round(otooley_percentage)
   Winner = max(candidate_votes, key=candidate_votes.get)

   
print("Election Results")
print('-----------------------------------')
print(f"Total Votes:{total_votes}")
print(f"{name_1}: {round_percent_khan}%({khan_votes})")
print(f"{name_2}: {round_percent_correy}%({correy_votes})")
print(f"{name_3}: {round_percent_li}%({li_votes})")
print(f"{name_4}: {round_percent_otooley}%({otooley_votes})")
print("___________________________________")
print(f"Winner: {Winner}")





cleaned_py_poll = zip(voter_ID, county, cname)
output_file = os.path.join("jordan_pypoll.csv")

with open(output_file,"w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Voter ID", "County", "Candidate Name"])

    writer.writerows(cleaned_py_poll)









  
    

