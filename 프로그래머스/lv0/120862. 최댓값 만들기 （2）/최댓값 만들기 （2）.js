// function solution(numbers) {
//     numbers.sort((a, b) => a - b);
    
//     minIndexMul = numbers[0] * numbers[1];
//     maxIndexMul = numbers[numbers.length - 1] * numbers[numbers.length - 2];
    
//     return minIndexMul > maxIndexMul ? minIndexMul : maxIndexMul;
// }

function solution(numbers) {
    let answer = [];
    
    for (let i = 0; i < numbers.length - 1; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            answer.push(numbers[i] * numbers[j]);
        }
    }

    return Math.max(...answer);
}
