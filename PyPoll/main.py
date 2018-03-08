
# coding: utf-8

#import dependencies
import pandas as pd

#read csv
pypoll = pd.read_csv("raw_data/election_data_1.csv")

#Total Votes
Total_Votes = pypoll["Voter ID"].count()

#List of candidates with percentage of votes and total number of votes
candidatevotes = pd.DataFrame(pypoll["Candidate"].value_counts())

candidatevotes = candidatevotes.reset_index()

candidatevotes = candidatevotes.rename(columns={"index": "Candidate", "Candidate": "Votes"})

candidatevotes.head()


#The winner of the election based on popular vote
topvotes = candidatevotes["Votes"].max()
Winner = candidatevotes["Candidate"].loc[candidatevotes["Votes"] == topvotes]

#Print out the results
print("Election Results")
print("--------------------")
print("Total Votes: " + str(Total_Votes))
print("--------------------")
print(candidatevotes)
print("--------------------")
print("Winner: " + str(Winner))
print("--------------------")

#Print results to external file
with open("PyPollResults.txt", "w") as text_file:
    text_file.write("Election Result\n")
    text_file.write("--------------------\n")
    text_file.write("Total Votes: " + str(Total_Votes) + "\n")
    text_file.write("--------------------\n")
    text_file.write(str(candidatevotes) + "\n")
    text_file.write("--------------------\n")
    text_file.write("Winner: " + str(Winner)+ "\n")
    text_file.write("--------------------\n")
