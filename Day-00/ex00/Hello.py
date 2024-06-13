ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"
ft_tuple = ("Hello","Finland!")
set_list = list(ft_set)
set_list[1] = "Helsinki!"
ft_set = set(set_list)
ft_dict["Hello"] = "Hive Helsinki!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
