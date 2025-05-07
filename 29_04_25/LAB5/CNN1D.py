def conv1d(input, kernel):
    input_len = len(input)
    kernel_len = len(kernel)
    output_len = input_len - kernel_len + 1
    output = []

    for i in range(output_len):
        acc = 0
        for j in range(kernel_len):
            acc += input[i + j] * kernel[j]  
        output.append(acc)
    return output


input_signal = [1, 5, 1, 7, 8, 2, 1, 4, 5, 2]
kernel = [2, 4, -1]

output = conv1d(input_signal, kernel)
print("1D convolution Output:", output)
