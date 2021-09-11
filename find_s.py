#-------------------------------------------------------------------------
# AUTHOR: Michael Melkonian
# FILENAME: Assignment 1 Problem 7
# SPECIFICATION: Output Hypothesis of Find-S algo
# FOR: CS 4200- Assignment #1
# TIME SPENT: 1.5 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
import csv

num_attributes = 4
db = []
print("\n The Given Training Data Set \n")

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes #representing the most specific possible hypothesis
print(hypothesis)

#find the first positive training data in db and assign it to the vector hypothesis
##--> add your Python code here
for row in db:    #traverse through database
      if row[4] == "Yes":     #only look for first positive outcome row
            hypothesis = row #set hypothesis to new row
            break
            

#find the maximally specific hypothesis according to your training data in db and assign it to the vector hypothesis (special characters allowed: "0" and "?")
##--> add your Python code here

for row in db: #travresing through database (csv file)
      for i in range(len(row)): #traversing through each row within the csv file
            if row[4] == "Yes":    #if the result is positive, Yes, then we can look into row
                  if hypothesis[i] != row[i]:   #make comparison with db row vs hypothesis row
                        hypothesis[i] = "?"     #make adjustments to hypothesis row to make more accurate
                        
                  else:
                        continue


print("\n The Maximally Specific Hypothesis for the given training examples found by Find-S algorithm:\n")
print(hypothesis)