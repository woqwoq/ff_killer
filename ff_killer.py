import logical_calc_logics
expr = "( A n B ) / C"
expr = expr.split()
vars = []
exprs = []
allowedVars = [ "P", "Q", "R", "T", "A", "B", "C"]
output = []
calcs = []


#Changing set notation's "/" to be equal to "and not"
for i in range(len(expr)):
    if expr[i] == "/":
        expr[i] = "^"
        expr.insert(i+1, "~")
        break


#Getting Prime Proposition List
#for i in range(len(expr)):
#    if expr[i] in allowedVars:
[vars.append(expr[i]) if expr[i] not in vars and expr[i] in allowedVars else None for i in range(len(expr))]

#Creating a 2d array of size len(vars)^2
[exprs.append([[].append(0) for i in range(len(vars)+1)]) for i in range(pow(len(vars), 2))]

#Getting max number binary number for calculating combinations
numtoget = len(vars)**2-1
#Calculating Combinations
currnum = 0
for i in range(len(exprs)):
    p = 0
    for j in range(len(exprs[i])-1):
        c = j+1
        exprs[i][j] = format(currnum, '#010b')[10-len(vars)+p:10-len(vars)+c]
        p+=1
    currnum+=1

#Generating Expression with different combinations
for i in range(len(exprs)):
    temp = ' '.join(expr)
    for j in range(len(vars)):
            temp = temp.replace(vars[j], exprs[i][j])
    calcs.append(temp)


#Calculating combinations and writing down to the last row of each column
for i in range(len(exprs)):
    #exprs[i][len(exprs[i])-1] = eval(calcs[i]) #Optional selection of calculation engines
    exprs[i][len(exprs[i])-1] = logical_calc_logics.enlogicate(calcs[i]) #Preffered

#Printing out
for i in range(len(vars)):
    print(vars[i], "\t", end = " ")
print(' '.join(expr), end = " ")  
print("", end="\n")     
for row in range(len(exprs)):
    for column in range(len(exprs[row])):
        print(exprs[row][column], "\t", end=" ")
        if column == len(exprs[row])-1:
            print("", end="\n")
