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
        
exersice_one()