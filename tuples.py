t = tuple('2345avbcd')
t1 = tuple('harsha')
print(t)
print(t[2])
print(t[-3])
print(t[1:])#excluding index 1
print(t[2:-1])#excluding 0 &1 as wll as -1
print(t[:])
print(t[:3])


#traversing tupless
for i in range(len(t)-1):
    print(t)

print('c' in t)
print(t.index('v'))

def searchtuple(t,element):
    for i in range(0,len(t)):
        if t[i] == element:
            return f"the '{element}' is found at {i}"
    return 'element is not found'

print(searchtuple(t ,'c'))

#concatination
print(t1 + t)
#multiplication
print(t*2)

print('a' in t)
print(t1.count('a'))
print(len(t1))
print(max(t))
print(min(t))
t2=()
print(t2)