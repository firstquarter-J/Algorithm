function solution(numbers) {
    const answer = numbers.reduce((sum, currentValue) => sum + currentValue, 0) / numbers.length
    return answer;
}