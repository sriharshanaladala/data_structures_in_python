my_dict = dict()
print(my_dict)
my_d = dict(onew="uno", two="dos", three='tres')
print(my_d)

mydict = {"name": "edy", 'age': 26, 'contact': 658712}
mydict["age"] = 30
print(mydict)
mydict['address'] = "hyderabad"
print(mydict)


def traversedict(dict):
    for key in mydict:
        print(key, dict[key])


traversedict(mydict)


# searching for a value in dict

def searchdict(dict, value):
    for key in mydict:
        if dict[key] == value:
            return key, value
    return "the value doesnot exits"


print(searchdict(mydict, 30))

# delete an element from dictionary

del mydict['age']
print(mydict)
mydict['age'] = 24
print(mydict)
myDict = {}.fromkeys([1, 2, 3], 5)
print(myDict)
print(mydict.get("city"))
print(mydict.items())
print(mydict.keys())
print(mydict.popitem())
print(mydict)
print(mydict.setdefault("sex", 'male'))
print(mydict)
newdict = {"a":1,'b':2}
print(mydict.update(newdict))
print(mydict)
new_dict={3:"three", 5: "five", 9: 'nine', 2:'two', 1:'one', 4:'four'}
print(len(new_dict))
print("ten" not in new_dict)

print(all(new_dict))

