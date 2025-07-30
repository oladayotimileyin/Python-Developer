## functional programing - separate concerns each part with one thing its good at

# they also separate data and functions - separte attribute

##map ##filter ##zip # reduce

my_list = [1,2,3]
your_list = [10, 20, 30]

def multiply_by2(items):
    return items*2

print(list(map(multiply_by2, my_list)))

# Filter
def check_odd(items):
    return items % 2 !=0

print(list(filter(check_odd, my_list)))

##zip
#matches two or more list and join the together and zip
print(list(zip(my_list, your_list)))