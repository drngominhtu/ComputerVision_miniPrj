#include <stdio.h>

#define M 5  // Kích thước ma trận đầu vào
#define N 5
#define K 3  // Kích thước kernel

void printMatrix(int matrix[M][N]) {
    for(int i = 0; i < M; i++) {
        for(int j = 0; j < N; j++) {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

// Hàm áp dụng sharpen kernel
void applySharpening(int input[M][N], int kernel[K][K], int output[M][N]) {
    int pad = K/2;
    
    // Áp dụng kernel
    for(int i = pad; i < M-pad; i++) {
        for(int j = pad; j < N-pad; j++) {
            int sum = 0;
            
            // Tính tích chập với sharpen kernel
            for(int k = -pad; k <= pad; k++) {
                for(int l = -pad; l <= pad; l++) {
                    sum += input[i+k][j+l] * kernel[k+pad][l+pad];
                }
            }
            
            // Giới hạn giá trị trong khoảng [0,255]
            if(sum > 255) sum = 255;
            if(sum < 0) sum = 0;
            
            output[i][j] = sum;
        }
    }
}

int main() {
    // Ma trận đầu vào (giả lập ảnh xám)
    int input[M][N] = {
        {100, 120, 130, 140, 150},
        {110, 130, 140, 150, 160},
        {120, 140, 150, 160, 170},
        {130, 150, 160, 170, 180},
        {140, 160, 170, 180, 190}
    };
    
    // Sharpen kernel
    int kernel[K][K] = {
        { 0, -1,  0},
        {-1,  5, -1},
        { 0, -1,  0}
    };
    
    // Ma trận kết quả
    int output[M][N] = {0};
    
    printf("Ma tran dau vao (anh xam):\n");
    printMatrix(input);
    
    printf("Sharpen kernel:\n");
    for(int i = 0; i < K; i++) {
        for(int j = 0; j < K; j++) {
            printf("%d\t", kernel[i][j]);
        }
        printf("\n");
    }
    printf("\n");
    
    applySharpening(input, kernel, output);
    
    printf("Ket qua sau khi lam sac net:\n");
    printMatrix(output);
    
    return 0;
}