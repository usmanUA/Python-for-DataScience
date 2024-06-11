# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: uahmed <uahmed@student.hive.fi>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 10:30:21 by uahmed            #+#    #+#              #
#    Updated: 2024/06/10 10:48:46 by uahmed           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
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
