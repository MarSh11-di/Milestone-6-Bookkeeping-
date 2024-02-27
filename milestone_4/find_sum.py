def find_sum_num(target: int, li: list[int]) -> tuple[int, int]:
    b_set =set()
    for i in li:
      for j in li[i:]:
        if i+j == target:
          b_set.add((i,j))
    return b_set
a = 5
list_target =[0,1,2,4,5,10]
print("по числам О(n2)",find_sum_num(a,list_target))
