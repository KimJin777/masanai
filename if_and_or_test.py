in_number1 = int(input("숫자를 넣으세요"))
in_number2 = int(input("숫자를 넣으세요"))

if (in_number1 % 2 == 0) and (in_number2 % 2 == 0):
    print("두 수 모두 짝수입니다.")
    print(in_number1, in_number2)

elif (in_number1 % 2 == 0) or (in_number2 % 2 == 0):
    print("두 수 중 하나는 짝수입니다.")

else:
    print("두 수 모두 홀수입니다.")