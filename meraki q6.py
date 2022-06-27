list1=["one","two","three","four","five"]
list2=[1,2,3,4,5]
dic={}
i=0
b=[]
while i<len(list1):
    c=list1[i],list2[i]
    b.append(c)
    i=i+1
    dic.update(b)
print(dic)
