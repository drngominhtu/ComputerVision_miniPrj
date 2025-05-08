#include <iostream>
#include <vector>
#include <stdio.h>

#define M 5  // Số hàng của ma trận đầu vào 
#define N 5  // Số cột của ma trận đầu vào
#define K 3  // Kích thước kernel (3x3)

void printMatrix(int matrix[M][N]) {
    for(int i = 0; i < M; i++) {
        for(int j = 0; j < N; j++) {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

void convolution2D(int input[M][N], int kernel[K][K], int output[M][N]) {
    // Tính padding
    int pad = K/2;
    
    // Thực hiện tích chập
    for(int i = pad; i < M-pad; i++) {
        for(int j = pad; j < N-pad; j++) {  
            int sum = 0;
            
            for(int k = -pad; k <= pad; k++) {
                for(int l = -pad; l <= pad; l++) {
                    sum += input[i+k][j+l] * kernel[k+pad][l+pad];
                }
            }
            output[i][j] = sum;
        }
    }
}

int main() {
    int input[M][N] = {
        {1, 2, 3, 4, 5},
        {6, 7, 8, 9, 10},
        {11, 12, 13, 14, 15},
        {16, 17, 18, 19, 20},
        {21, 22, 23, 24, 25}
    };
    
    // Kernel 3x3 
    int kernel[K][K] = {
        {1, 0, -1},
        {1, 0, -1},
        {1, 0, -1}
    };
    
    // Ma trận kết quả
    int output[M][N] = {0};
    
    printf("Ma tran dau vao:\n");
    printMatrix(input);
    
    printf("Kernel:\n");
    for(int i = 0; i < K; i++) {
        for(int j = 0; j < K; j++) {
            printf("%d\t", kernel[i][j]);
        }
        printf("\n");
    }
    printf("\n");
    
    convolution2D(input, kernel, output);
    
    printf("Ket qua tich chap:\n");
    printMatrix(output);
    
    return 0;
}
