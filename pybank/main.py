from itertools import count
import os
import csv
from statistics import mean
csvpath = os.path.join('resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    month = []
    tot = []
    change = []
    maxval = 0
    minval = 0
    maxdate = []
    mindate = []
    for row in csvreader:
        month.append(row[0])
        tot.append(int(row[1]))
        tot_amt = sum(tot)

    for i in range(len(month)-1):
        tot_change = tot[i+1]-tot[i]
        change.append(tot_change)
        avg = float(round(mean(change), 2))
    
    maxval = max(change)
    minval = min(change)

    maxdate = change.index(maxval) + 1
    date1 = month[maxdate]
    mindate = change.index(minval) + 1
    date2 = month[mindate]


 




