def get_triangle(rows:int):
  piramid =[]
  for i in range(rows):
    row = [1] * (i+1)
    for j in range(i+1):
        if j != 0 and j != i:
            row[j] = piramid[i-1][j-1] + piramid[i-1][j]
    piramid.append(row)
    if i%2==1 and rows%2==0:
        print(" ", end="")
    elif i%2==0 and rows%2==1:
        print(" ", end="")
    print(*[" "]*((rows-i)//2)+row)
  return piramid
P = get_triangle(5)