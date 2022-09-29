import os
import csv

csvpath = os.path.join('resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    votes = []
    candidates = []
    percent = []
    can1 = 0
    can2 = 0
    can3 = 0
    winner = []

    for row in csvreader:
        votes.append(row[0])
        ct = len(votes)
        if row[2] not in candidates:
            candidates.append(row[2])
        if row[2] == candidates[0]:
            can1 += 1
        elif row[2] == candidates[1]:
            can2 += 1
        elif row[2] == candidates[2]:
            can3 += 1
        
        if can1 > can2 and can3:
            winner= candidates[0]
        elif can2 > can1 and can3:
            winner = candidates[1]
        elif can3 > can2 and can1:
            winner = candidates[2]

    perc1 = round((can1/ct)*100, 3)
    perc2 = round((can2/ct)*100, 3)
    perc3 = round((can3/ct)*100, 3)



    tot = (f'Total Votes: {ct}')
    charles = (f'{candidates[0]}: {perc1}% ({can1})')
    diana = (f'{candidates[1]}: {perc2}% ({can2})')
    raymon = (f'{candidates[2]}: {perc3}% ({can3})')
    win = (f'Winner: {winner}')


    output = os.path.join('analysis', 'analysis.txt')

with open (output, 'w') as txtfile:
    txtfile.write('Election Results\n')
    txtfile.write('-------------------------\n')
    txtfile.write(f'{tot}\n')
    txtfile.write('-------------------------\n')
    txtfile.write(f'{charles}\n')
    txtfile.write(f'{diana}\n')
    txtfile.write(f'{raymon}\n')
    txtfile.write('-------------------------\n')
    txtfile.write(f'{win}\n')
    txtfile.write('-------------------------\n')






      
    






