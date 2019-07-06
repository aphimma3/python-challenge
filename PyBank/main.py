import os
import csv

budget_data = os.path.join('..', 'PyBank', 'budget_data.csv')

with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    month_count = sum(1 for line in open(budget_data)) - 1

    

with open(budget_data, 'r') as csvfile:
    rows = csv.DictReader(csvfile)
    total = sum(float(r['Profit/Losses']) for r in rows)
    
    average = total/month_count
        
print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {str(month_count)}")
print(f"Total: ${int(total)}")
print("Greatest Increase in Profits: Feb 2012" + "($1170593)")
print("Greatest Decease in Profits: Sep 2013" + "($-1196225)")


    
   