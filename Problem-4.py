'''Get the total count of number listed in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
    (examples)
    input: [1,2,8,9,12,46,76,82,15,20,30]
    Output:
        {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}'''


def count_multiples(numbers_list, multiples_list):
    result = {}
    for multiple in multiples_list:
        count = 0
        for number in numbers_list:
            if number % multiple == 0:
                count += 1
        result[multiple] = count
    return result

#example
input_numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
multiples = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = count_multiples(input_numbers, multiples)
print(output)
