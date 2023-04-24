function solution(numbers, num1, num2) {
    var answer = [];
    
    // for ( let i = num1; i <= num2; i ++ ) {
    //     answer.push[numbers.pop(i)]
    // }
    
    answer = numbers.slice(num1, num2 + 1)
    
    return answer;
}