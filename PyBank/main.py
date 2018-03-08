# coding: utf-8

#import dependencies
import pandas as pd
import sys

#Read CSV
pybank = pd.read_csv("raw_data/budget_data_1.csv")


#Print Total number of months
pydate = pybank["Date"].count()


#Print Total Revenue
pyrev = pybank["Revenue"].sum()


#Print Average Revenue Change
pyavgrev = pybank["Revenue"].mean()


#The Greatest Increase in Revenue (date and amount) over the entire period
bankmax = pybank["Revenue"].max()


#The greatest decrease in revenue (date and amount) over the entire period
bankmin = pybank["Revenue"].min()

#Print the set values
print("Financial Analysis")
print("-------------------")
print("Total Months: " + str(pydate))
print("Total Revenue: " + str(pyrev))
print("Average Revenue Change: " + str(pyavgrev))
print("Greatest Increase in Revenue: " + str(bankmax))
print("Greatest Decrease in Revenue: " + str(bankmin))


#Export a file with the results
with open("PyBankResults.txt", "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("---------------------\n")
    text_file.write("Total Months: " + str(pydate) + "\n")
    text_file.write("Total Revenue         : $" + str(pyrev) + "\n")
    text_file.write("Average Revenue       : $" + str(pyavgrev) + "\n")
    text_file.write("Greatest Increase in Revenue: " + str(bankmax) + "\n")
    text_file.write("Greatest Decrease in Revenue: " + str(bankmin) + "\n")

