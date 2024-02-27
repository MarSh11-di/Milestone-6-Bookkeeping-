open = "("
closed =")"
def is_balanced (symbol:str):
  full_symbol=[]
  for i in symbol:
    if i == open:
      full_symbol.append(open)
    if i == closed:
      full_symbol.append(closed)
  if full_symbol.count(open)==full_symbol.count(closed):
      return True
  else:
      return False
a = is_balanced ("()()")
b = is_balanced ("())")
c = is_balanced ("(()")
d = is_balanced ("()())( ")
print(a,b,c,d)