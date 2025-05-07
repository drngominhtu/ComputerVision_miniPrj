#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

// Hàm tích chập
void convolution(int* input, int inputSize, int* kernel, int kernelSize, int* output) {
    int outputSize = inputSize - kernelSize + 1;
    
    for (int i = 0; i < outputSize; i++) {
        output[i] = 0;
        for (int j = 0; j < kernelSize; j++) {
            output[i] += input[i + j] * kernel[j];  
        }
    }
}

int main() {
    
    int input[] = {1, 2, 3, 9, 5, 3, 2, 2, 4, 1, 4, 5,1, 4, 0, 5};
    int kernel[] = {1, 0, -2};

    int inputSize = sizeof(input) / sizeof(input[0]);
    int kernelSize = sizeof(kernel) / sizeof(kernel[0]);
    int outputSize = inputSize - kernelSize + 1;
    int* output = new int[outputSize];

    // Gọi hàm tích chập
    convolution(input, inputSize, kernel, kernelSize, output);

    printf("Output: ");
    for (int i = 0; i < outputSize; i++) {
        printf("%d ", output[i]);
    }
    printf("\n");

    delete[] output;
    return 0;
}
