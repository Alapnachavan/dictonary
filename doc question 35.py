# write a python program to convert a list into a nested dictionar
# num_list=[1,2,3,4]
# sample output:
# {1:{2 : {3: {4: {}}}}}




# num_list=[1,2,3,4]
# new_dict=current={}
# for name in num_list:
#     current[name]={}
#     current=current[name]
# print(new_dict)



class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        result=''
        
        a=list(a)
        b=list(b)
        while a or b or carry:
            if a:
                carry+=int(a.pop())
            if b:
                carry+=int(b.pop())
                
        result+=str(carry%2)
        carry//=2
        return result[::-1]
        