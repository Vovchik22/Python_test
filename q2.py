'''
def cheese_crackers(cheese_count, boxes_of_crackers):
    print(f"you have {cheese_count} cheeses")
    print(f"you have {boxes_of_crackers} boxes_of_crackers")
    print("thats enough for party")
    print("Get a blanked")

print("we can just give the function numbers directly: ")
cheese_crackers (20, 30)

print("Or, we can just use variables")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_crackers (amount_of_cheese, amount_of_crackers)

print("we can even do math inside too: ")
cheese_crackers (10+50, 5+6)

print("and we can combine the two, variables and math")
cheese_crackers (amount_of_cheese + 10, amount_of_crackers + 20)

'''
def function(arg1, arg2, arg3):
    print(f"Lets calculate some figures in different ways: {arg1}, {arg2} and {arg3} ")
    print(f"so first number is {arg1}")
    print(f"Second number will be {arg2}")
    print(f"And finaly third - {arg3}")
    print("\n")

print("First figures set direct in function")
function (10, 15, 20)




fig1 = 4
fig2 = 3
fig3 = 8

print(f"with variables : add {fig1} to {fig2}, substract {fig2} from {fig3} and dived {fig1} on {fig3}")

function (fig1 + fig2, fig2 - fig3 ,fig1 / fig3)

print("Divide all args on each other in a raw with another numbers")
function (1 + fig1, 2 + fig2, 3 + fig3)
