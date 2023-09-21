
# Given the names and grades for each student in a class of 
# students, store them in a nested list and print the name(s) 
# of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second
#  lowest grade, order their names alphabetically and 
#  print each name on a new line.

# Example
# records = [["chi",20],["beta",50],["alpha", 50]]
# The ordered list of scores is[20,50] , so the second lowest score is 50.
# There are two students with that score:["beta","alpha"] . Ordered alphabetically,
# the names are printed as:
# alpha
# beta

#  solution

#  we create two empty lists one to store the scores (stud_scores) and
 #  the other stores names and scores in a nested list (results) 

results = []
stud_scores = []
for i in range(int(input())):
    name = input()
    score = float(input())
    results.append([name,score])
    stud_scores.append(score)

stud_scores.sort() # Here we sort the scores in ascending order to find the min 
sec_min = 0   # a variable for the second lowest
minimum = stud_scores[0] # since its sorted the first value in the list is the minimum


for i in stud_scores:
    if i != minimum:
        sec_min = i
        break 
    #the for loops find the second lowest from the
    # stud_scores list. The  for loop will loop throgh 
    # the first value which is the minimum and it will
    # be equal to the variable in the for loof. afret that it will
    # execute the second value in the list since its not equal to
    # the minimum it will break and the the value assigned to the 
    # second lowest. Note that the list was sorted in ascending order  
    
results.sort() #sort the results in ascending order
for i in results:
    if i[1] == sec_min:

        print(i[0])
    #here the loop compares the sec lowest value with the 
    # scores of every student to print out the ones that meet the criteria

