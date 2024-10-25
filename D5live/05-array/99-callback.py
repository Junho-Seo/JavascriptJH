# python에서의 map 함수 예시

numbers = [1, 2, 3]


def square(num):
    return num**2

# numbers 리스트의 요소를 순회하며 square 함수를 적용
new_numbers = list(map(square, numbers))
print(new_numbers)  # [1, 4, 9]
