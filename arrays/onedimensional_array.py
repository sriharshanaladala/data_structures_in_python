import array
a= array.array('i',[1,2,3,4,5])

def search_array(array, value):
    for i in array:
        if i == value:
            return True
    else:
        return "the element doent exist"

print(search_array(a, 3))