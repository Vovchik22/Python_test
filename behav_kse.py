# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 13:50:43 2018

@author: User
"""

from builtins import input
import random
from datetime import datetime

def make_filename(base = 'output', extension = 'csv'):
    return base + datetime.now().strftime('_%Y%m%d_%H%M%S') + '.' + extension

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

mail = input("Please, enter your e-mail. ")
gender = input("Please, enter your gender. m - for males, f - for females, o - for others ")
age = input("Please, enter your age. ")
w = [1000.0]
ret = [0.0]
risk = []
risk_loving = []
i = 0

print ("You have 1000 UAH")

while i != 1:
    print ("Experts say that bond will rise up in its price in the next period. Do you want to buy it on at least some of your money? If yes, please, enter y, if no - enter n.")
    Play = input()
    print (Play)
    if Play != "y" and Play != "n":
        print ("Please, enter either y or n.")
    else:
        i = 1

if Play == "y":
    i = 0
    while i != 1:
        print ("How much money do you want to spend to buy bonds? Choose value between 0 and 1000.")
        s = 0
        while s != 1:
            bet = input()
            if is_number(bet) == False:
                print ("Choose value between 0 and 1000.")
            else:
                s = 1
        bet = float(bet)
        if bet < 0 or bet > 1000:
            print ("Choose value between 0 and 1000.")
        else:
            i = 1
else:
    bet = 0

a = random.uniform(1, 1.5)
dollars = 1000-bet
bonds = bet*a
risk.append(bet)
risk_loving.append(bet)
wealth=bonds+dollars
print ("Bond's price have changed by " + str((a-1)*100) + "%")
print ("Now you have " + str(wealth) +" UAH:" + str(bonds) + " UAH in bonds and" + str(dollars) + " UAH in hryvnias.")

for j in range(9):
    w.append(wealth)
    ret.append((a-1)*100)
    i = 0
    while i != 1:
        print ("No forecasts are given now. Do you want to buy bonds or sell? If buy, please, enter b, if sell - enter s, if none - enter n.")
        Play = input()
        if Play != "b" and Play != "n" and Play != "s":
            print ("Please, enter either b, s or n.")
        else:
            i = 1
    if Play == "b":
        i = 0
        while i != 1:
            print ("How much money do you want to spend to buy bonds? Choose value between 0 and " + str(dollars) + ".")
            s = 0
            while s != 1:
                bet = input()
                if is_number(bet) == False:
                    print ("Choose value between 0 and " + str(dollars)+".")
                else:
                    s = 1
            bet = float(bet)
            if bet < 0 or bet > dollars:
                print ("Choose value between 0 and " + str(dollars) + ".")
            else:
                i = 1
    elif Play == "s":
         i = 0
         while i != 1:
            print ("How much money do you want to get from selling bonds? Choose value between 0 and " + str(bonds) + ".")
            s = 0
            while s != 1:
                bet = input()
                if is_number(bet) == False:
                    print ("Choose value between 0 and " + str(bonds) + ".")
                else:
                    s = 1
            bet = float(bet)
            if bet < 0 or bet > bonds:
                print ("Choose value between 0 and " + str(bonds) + ".")
            else:
                bet = -bet
                i = 1
    else:
        bet = 0
    a = random.uniform(0.5, 1.5)
    dollars = dollars-bet
    bonds = bonds+bet
    risk_loving.append(bonds/wealth)
    bonds = bonds*a
    wealth = bonds+dollars
    risk.append(bet)
    print ("Bond's price have changed by " + str((a-1)*100) + "%")
    print ("Now you have " + str(wealth) +" UAH: " + str(bonds) + " UAH in bonds and " + str(dollars) + " UAH in hryvnias.")

import csv
varlist = [w, ret, risk, risk_loving]
maxlen = max(len(w), len(ret), len(risk), len(risk_loving))
def list_get(src, index, default = None):
    return src[index] if len(src) > index else default
    # if index >= len(src):
    #     return None
    # else:
    #     return src.get(index)

with open(make_filename(), "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerow([mail])
    writer.writerow([gender])
    writer.writerow([age])
    # for val in varlist:
    #     writer.writerow([val])
    for i in range(maxlen):
        _row = [list_get(w, i), list_get(ret, i), list_get(risk, i), list_get(risk_loving, i)]
        writer.writerow(_row)
output.close()
