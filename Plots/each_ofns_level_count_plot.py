#offense level vs number of records
#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import numpy as np
import csv

#define pie chart
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%\n({v:d})'.format(p=pct,v=val)
    return my_autopct


#read input file
crimes = []
level = []
with open('each_ofns_level_count.out','r') as file:
    plots = csv.reader(file, delimiter='\t')
    for row in plots:
        crimes.append(int(row[0]))
        level.append(row[1])
#plot the pie chart
fig, ax = plt.subplots()
ax.pie(crimes, labels=level, autopct=make_autopct(crimes),
        shadow=True, startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Crime Count for ach Offense Level')
# plt.show()
plt.savefig('each_ofns_level_count.png')
