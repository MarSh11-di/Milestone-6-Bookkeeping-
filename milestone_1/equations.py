user = input()
user_new = user.replace(" ","").replace("(", "").replace(")","").replace("^2", "").replace("x","").replace("=","+").split("+")
a = int(user_new[0])
b = int(user_new[1])
c = int(user_new[2])
disc = round((b**2 - (4*a*c))**0.5)
# тут краще б застосувати if тому що якщо disc вiд"емне то видае помилку, але в умовi написано, що не можна, тому без if
x_1 =  round(((-b) + disc)/(2*a))
x_2 =  round(((-b) - disc)/(2*a))
print(user_new)
print(a)
print(b)
print(c)
print(disc)
print(x_1)
print(x_2)