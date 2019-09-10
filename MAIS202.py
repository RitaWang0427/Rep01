import csv
import numpy as np
import matplotlib
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import six
list1 = []
with open('loan_data.csv') as loanData:
    reader1 = csv.reader(loanData)
    for column in loanData:
        list1.append([column.split(',')[0], column.split(',')[1]])
list1 = list1[1:]
list2 = []
with open('home_ownership_data.csv') as hoData:
    reader2 = csv.reader(hoData)
    for row in hoData:
        list2.append([row.split(',')[0], row.split(',')[1].rstrip()])
list2 = list2[1:]
list3 = []
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i][0] == list2[j][0]:
            list3.append([list2[j][1], list1[i][1]])
listM = []
listO = []
listR = []
for z in range(len(list3)):
    if list3[z][0] == 'MORTGAGE':
        listM.append(list3[z][1])
    if list3[z][0] == 'OWN':
        listO.append(list3[z][1])
    if list3[z][0] == 'RENT':
        listR.append(list3[z][1])
Mortgage = 0
Rent = 0
Own = 0
for a in range(len(listM)):
    Mortgage = Mortgage+int(listM[a])
for b in range(len(listO)):
    Own = Own+int(listO[b])
for c in range(len(listR)):
    Rent = Rent+int(listR[c])
Mortgage = round(float(Mortgage)/len(listM),6)
Own = round(float(Own)/len(listO),6)
Rent = round(float(Rent)/len(listR),6)
Name = ['MORTGAGE', 'OWN', 'RENT']
Average = [Mortgage, Own, Rent]
All = [[0, 'MORTGAGE', Mortgage],[1,'OWN', Own], [2, 'RENT', Rent]]
All = np.array(All)
fig, plt = plt.subplots(1, 2, gridspec_kw={'width_ratios': [1,3]},figsize=(15,6))
plt[1].bar(Name, Average, align='center', width=0.62)
plt[1].set_title('Average loan amounts per home ownership')
plt[1].set_xlabel('Home ownership')
plt[1].set_ylabel('Average loan amount($)')
plt[0].axis('off')
plt[0].axis([0, 3, All.shape[0], -6])
table1 = plt[0].table(cellText=All, cellColours=[['#F0F0F0', '#F0F0F0', '#F0F0F0'], ['#FFFFFF', '#FFFFFF', '#FFFFFF'],
                                                 ['#F0F0F0', '#F0F0F0', '#F0F0F0']],
             colLabels=['', 'home_ownership', 'loan_amnt'], loc='bottom', colWidths=[0.05, 0.4, 0.4], bbox=[0.0, 0.0, 1.0, 0.3])
table1.auto_set_font_size(False)
table1.set_fontsize(12.5)
for k, cell in six.iteritems(table1._cells):
    cell.set_edgecolor('none')
    cell.set_text_props(fontproperties=FontProperties(family='Arial'))
    if k[0] == 0:
        table1._cells[k]._loc='right'
        cell.set_text_props(fontproperties=FontProperties(weight='bold', family='Arial'))
    if k[1] == 0:
        cell.set_text_props(fontproperties=FontProperties(weight='bold', family='Arial'))
plt[0].axhline(y=1, color='k')
fig.show()