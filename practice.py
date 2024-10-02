#Practicing array data structures

#Exersice one
def exersice_one():
    monthly_expenses = [2200,2350,2600,2130,2190]
    result1 = compare(monthly_expenses)
    print (result1)

    result2 = first_quarter(monthly_expenses)
    print(result2)

    result3 = spent_exact(monthly_expenses)
    print(result3)

    result4 = add_expense(monthly_expenses)
    print(result4)

    result5 = correction(monthly_expenses)
    print(result5)


#1
#Goal compare the extra money spent
def compare(expenses):
    extra = expenses[1] - expenses[0]
    return extra    

#2
#Here is the thing I can make it specific but lets try and make it generic
def first_quarter(expenses):
    total = 0
    for i in range(0,3):
        total += expenses[i]
    return total

#3
#If exact money spent is 2000
def spent_exact(expenses):
    for expense in expenses:
        if expense == 2000:
            return True
    return False

#4
def add_expense(expenses):
    added_expense = expenses.copy()
    added_expense.append(1980)
    return added_expense

#5
def correction(expenses):
    
    for i in range(len(expenses)):
        if i == 3:
            expenses[i]= expenses[i] - 200
            return expenses
        
#exersice_one()

def exersise_two():
    heros=['spider man','thor','hulk','iron man','captain america']

    print(length(heros))

    print(add_in_end(heros))

    print(fix_error(heros))

    print(replace_item(heros))

    print(alphabetical(heros))
    


def length(heros):
    #I think there is multiple ways to find length either just count them using for loop
    #or just do .len
    length = len(heros)
    return length

def add_in_end(heros):
    #If i were to want it not to affect og list then I would just do this
    #new_list = heros.copy()
    #new_list.append('black panther')
    heros.append('black panther')
    return heros

def fix_error(heros):
    #if i want to make more generic probably just give a parameter
    heros.remove('black panther')
    heros.insert(3,'black panther')
    return heros

#remember splicing!! i mean slicing
def replace_item(heros):
    heros[1:3] = ['doctor strange']
    return heros

#nice little hack return dir(heros) for a list of options
#sorted used for list 
#.sort() for numbers me assumes
def alphabetical(heros):
    heros = sorted(heros)
    return heros

#exersise_two()


#Excersise three
#Idk if it is asking me to also have max number odd
#is this efficient ? I think this is O(n)
def exersise_three():

    odd_array = []
    ans = int(input("Enter an odd max number: "))
    #if(ans % 2 == 1): Fix mistake this line is not needed because it is already checking
    #in next lines if it is even or not
    for num in range(1,ans):
        if(num % 2 == 1):
            odd_array.append(num)
    print(odd_array)
    

exersise_three()