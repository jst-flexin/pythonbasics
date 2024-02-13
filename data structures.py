# list data structure


my_list = ["Toyota", "Mercedes", "Subaru", "Range Rover", "Nissan"]
my_list.append("Mazda")
print(my_list)

print(my_list[0])
print(my_list[0], "are manufactured in Japan")

di_list = ["23", "24", "25", "26", "27", "28", "29"]
di_list.insert(1, "Mercedes")
print(di_list)
print(type(di_list))

# tuple datastructure

my_tuple = ("Banana", "Pomegranates", "Apples", "Mangoes", "Oranges")
print(f"I love eating {my_tuple[1]}")
# my_tuple[2]="Bussin"

# set data structure
my_set = {"Philadelphia", "Bangladesh", "Delhi", "New Brunswick", "Oklahoma"}
print(my_set)

# dictionary data structures
my_dict = {"Name": "Flex", "Age": 19, "Gender": "Male"}
print(my_dict)
print(my_dict["Name"])
print(my_dict["Age"])
print(my_dict["Gender"],"EHEEEMMMM")
print(f"my name is {my_dict["Name"]} and my age is {my_dict["Age"]}")