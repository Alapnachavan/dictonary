import operator
d={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# print('original dictonary:',d)
sorted_d=sorted(d.items(),key=operator.itemgetter(1))
print('dictonary in acending order by value:',sorted_d)
sorted_d=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
print("dictionary in descemding enter by value:",sorted_d)
