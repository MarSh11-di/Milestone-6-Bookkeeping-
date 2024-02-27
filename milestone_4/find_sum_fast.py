def find_sum_fast(target: int, li: list[int]) -> tuple[int, int]:
   b_set =set()
   for i in li:
    x = target-i
    if x in list_target:
         b_set.add((max(i, x), min(i,x)))
   return b_set
a = 5
list_target =[0,1,2,4,5,10]
print("по ускоренной функции О(n)",find_sum_fast(a,list_target))