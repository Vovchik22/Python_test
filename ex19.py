def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"you have {cheese_count} cheeses")
    print(f"you have {boxes_of_crackers } boxes of crackers")
    print("Get a blankett \n")

print ('we can just give the function numbers directly')
cheese_and_crackers(20,30)


amount_of_cheese = 10
amount_of_crackers = 50
print (f"""
OR, We can use variables:
chesee = {amount_of_cheese}
crackers = {amount_of_crackers}
""")

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("we can do the mat with them:  ")

cheese_and_crackers(2e5, 4**4)

x = int(input())
y = int(input())

print(cheese_and_crackers(x,y))
