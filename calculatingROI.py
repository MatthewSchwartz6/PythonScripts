moneySpent = float(raw_input("How much did you invest today in total? \n>>> "))
moneyGenerated = float(raw_input("How much money was generated overall today? \n>>>"))
moneyProfit = 0.0
moneyProfit = moneyGenerated - moneySpent
ventureROI = 0.0
if moneySpent == 0.0:
    moneyProfit = moneyGenerated
else:
    ventureROI = moneyProfit/moneySpent
pecentageROI = 0.0
percentageROI = ventureROI * 100.0
print "Your profit for the day is %d." %(moneyProfit)
print "Your return of investment for the day is %d pecent."%(percentageROI)
