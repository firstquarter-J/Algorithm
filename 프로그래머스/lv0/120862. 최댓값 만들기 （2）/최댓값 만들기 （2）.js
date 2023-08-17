function solution(numbers) {
    numbers.sort((a, b) => a - b);
    
    minIndexMul = numbers[0] * numbers[1];
    maxIndexMul = numbers[numbers.length - 1] * numbers[numbers.length - 2];
    
    return minIndexMul > maxIndexMul ? minIndexMul : maxIndexMul;
}