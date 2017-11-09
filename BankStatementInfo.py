#Basic information about your monthly bank statement.
#All credits have to be with plus ("+") signs.
#All purchases have to be with minus ("-") signs.
#Your bank statement has to be in two columns: purchases/credits and balance at the time

from sys import argv
import re
import pprint


script, fromfile = argv

f = open(fromfile)
a = f.read()

money = re.compile(r'(\-?\d?\d?\d\.\d\d)')
m = money.findall(str(a))
b = m[1:len(m):2]
b = [float(i) for i in b]
print "Account balance for the month: \n" , pprint.pprint(b)
print "Average account balance of account is: ", round(sum(b)/len(b))
print "Times account balance changed: ", len(b)
print "Thats %r times per day!" % ((30.0)/len(b))
print "----------------------------------------"
amountSpent = re.compile(r'(\-\d?\d?\d\.\d\d)')
allSpent = amountSpent.findall(str(a))
justSpent = allSpent[0:len(allSpent)]
justSpent = [float(i) for i in justSpent]
print "All purchases for this month: \n ", pprint.pprint(justSpent)
print "Average purchase amount : ", round(sum(justSpent)/len(justSpent))
print "Number of purchases: ", len(justSpent)
print "Total spent for the month: ", sum(justSpent)
print "----------------------------------------"
amountpayed = re.compile(r'\+\d?\d?\d\.\d\d')
x = amountpayed.findall(str(a))
x = [float(i) for i in x]
print "Payment for this month : \n" , pprint.pprint(x)
print "Amount payed in total: ", sum(x)
print "----------------------------------------"
print "So you made %r and you spent %r. \nAre you a good budgeter?" % (sum(x),round(sum(justSpent)))
print "Your net cash for the month is: " ,sum(x) + round(sum(justSpent))
print "-------------------end------------------"
