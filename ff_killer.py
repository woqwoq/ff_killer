import logical_calc_logics
import config_parser


allowedVars = config_parser.get_allowed_vars()


#Changing set notation's "/" to be equal to "and not"
def replace_and_not(expr: str) -> str:
    for i in range(len(expr)):
        if expr[i] == "/":
            expr[i] = "^"
            expr.insert(i+1, "~")

    return expr


#Getting Prime Proposition List
def count_prime_propositions(expr: str) -> list:
    prime_propositions = []
    for digit in expr:
        if digit in allowedVars and digit not in prime_propositions:
            prime_propositions.append(digit)

    return prime_propositions

#Creating a 2d array of size 2^len(prime_propositions)
def create_2d_array(size: int) -> list:
    arr = []
    for i in range(pow(2, size)):
        arr.append([])
        for j in range(size+1):
            arr[i].append(0)

    return arr

#Calculating Combinations
def generate_binary_combinations(exprs: list, prime_propositions: list) -> list:
    currnum = 0
    for i in range(len(exprs)):
        p = 0
        for j in range(len(exprs[i])-1):
            c = j+1
            exprs[i][j] = format(currnum, '#010b')[10-len(prime_propositions)+p:10-len(prime_propositions)+c]
            p+=1
        currnum+=1

    return exprs

#Generating Expression with different combinations
def generate_expressions_from_combinations(expr: list, prime_propositions: list, exprs: list) -> list:
    calcs = []
    temp = ""
    for i in range(len(exprs)):
        temp = ' '.join(expr)
        for j in range(len(prime_propositions)):
                temp = temp.replace(prime_propositions[j], exprs[i][j])
        calcs.append(temp)

    return calcs

#Calculating combinations and writing down to the last row of each column
def calculate_expression(exprs: list, calcs: list) -> list:
    for i in range(len(exprs)):
        #exprs[i][len(exprs[i])-1] = eval(calcs[i]) #Optional selection of calculation engines
        exprs[i][len(exprs[i])-1] = logical_calc_logics.enlogicate(calcs[i]) #Preffered

    return exprs

#Printing out
def display_table(expr: list, prime_propositions: list, exprs: list):
    for i in range(len(prime_propositions)):
        print(prime_propositions[i], "\t", end = " ")
    print(' '.join(expr), end = " ")  
    print("", end="\n")     
    for row in range(len(exprs)):
        for column in range(len(exprs[row])):
            print(exprs[row][column], "\t", end=" ")
            if column == len(exprs[row])-1:
                print("", end="\n")

#Evaluating and displaying the truth table:
def evaluate_truth_table(expr: str):
    expr = expr.split()
    prime_propositions = []
    exprs = []
    calcs = []


    #Changing set's notation's '/' to ~^ as they are equivalent
    expr = replace_and_not(expr)

    #Getting a list of all prime propositions in the expression
    prime_propositions = count_prime_propositions(expr)

    #Creating an empty 2d array
    exprs = create_2d_array(len(prime_propositions))

    #Filling the 2d array with combinations such as 0 0 0, 0 0 1
    exprs = generate_binary_combinations(exprs, prime_propositions)

    #Interchanging the combinations from 2d array into the expression as follows: 0 0 1 -> 0 n 0 v 1
    calcs = generate_expressions_from_combinations(expr, prime_propositions, exprs)

    #Evaluating the final result
    exprs = calculate_expression(exprs, calcs)

    #Printing out
    display_table(expr, prime_propositions, exprs)




