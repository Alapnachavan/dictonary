test_list=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
# b={}
# c=[]
# i=0
# while i<len(a):
#     b.update(a[i])
#     i+=1
# for i in b.values():
#     if 1 not in c :
#         c.append(i)
# print(c)
# # print(a)

# test_list = [{'gfg' : 1, 'is' : 2}, {'best' : 1, 'for' : 3}, {'CS' : 2}]
# print("The original list : " +  str(test_list))
a = list(set(val for dic in test_list for val in dic.values()))
print("The unique values in list are : " + str(a))
