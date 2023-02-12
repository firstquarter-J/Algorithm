function solution(numbers) {
    const answer = numbers.reduce(function add(sum, currentValue){
        return sum + currentValue
    }) / numbers.length
    return answer;
}