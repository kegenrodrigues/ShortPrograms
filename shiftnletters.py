# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    num=ord(letter)
    new_num=num+n
    if new_num<97:
        ans=123-(97-new_num)
        return chr(ans)
    if new_num>122:
        ans=96+new_num-122
        return chr(ans)
    if new_num>=97 and new_num<=122:
        return chr(new_num)
print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i
print shift_n_letters('a', -10)
#>>q
