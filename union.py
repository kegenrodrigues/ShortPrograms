# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no 
# repeated elements.

def union(l1,l2):
    j=0
    flag=0
    
    
    while j<len(l2):
        #0<3
        
        i=0
        while i<len(l1):
            #0<3
            
            if l2[j]==l1[i]:
            #2==1
                flag=0
                break
                #donotappend
            else:
                flag= 1
            i=i+1    
        
        if flag==1:
            
            l1.append(l2[j])       
            #1234
        j=j+1    
# To test, uncomment all lines 
# below except those beginning with >>>.


a = [1,2,3]
b = [2,4,6]

union(a,b)
print a
#>>> [1,2,3,4,6]
print b
#>>> [2,4,6]
