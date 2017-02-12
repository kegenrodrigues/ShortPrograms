# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.

def hash_string(keyword,buckets):
    total=0
    for e in keyword:
        total=total+ord(e)
    bnum=total%buckets    
    return bnum

print hash_string('a',12)
#>>> 1
print hash_string('b',12)
#>>> 2
print hash_string('a',13)
#>>> 6
print hash_string('au',12)
#>>> 10

