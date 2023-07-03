'''Problem-2:  With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]

    Output: (examples)
        1) input a = 1, then output : 1
        2) input a = 2, then output : 1, 3
        3) input a = 3, then output : 1, 3, 5
        4) input a = 4, then output : 1, 3, 5, 7
        .
        .
        5) input a = x, then output : 1, 3, 5, 7, .......'''


def generate_series(x):
    series = []
    for i in range(1, x+1):
        series.append(str(2*i - 1))
    series_string = ', '.join(series)
    return series_string

#Example
input_number = 4
output = generate_series(input_number)
print(output)
