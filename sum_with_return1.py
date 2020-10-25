# 위치인자
def get_sum(a, b):
    result = a+b
    return result

#키워드인자
def get_sum_1(a=1, b=2):
    result = a+b
    return result

# 가변인자
def get_sum_2(b, d, a=1, c=3):
    result_1 = a + b
    result_2 = c - d
    return result_1, result_2

n1= get_sum(10, 20)
print("10과 20의 합은 " , n1)

n2= get_sum(100, 200)
print("100과 200의 합은 " ,n2)


n3= get_sum_1(8,5)
print("1과 2의 합은 " ,n3)

n4 = get_sum_2(5,6)
print(n4)