def find_sum_index(target: int, li: list[int]) -> tuple[int, int]:
    b_set =set()
    for i in range(len(li)):
      for j in range(i+1,len(li)):
        if li[i]+li[j] == target:
          b_set.add((i,j))
    return b_set
a = 5
list_target =[0,1,2,4,5,10]
print("по iндексам О(n2)",find_sum_index(a,list_target))