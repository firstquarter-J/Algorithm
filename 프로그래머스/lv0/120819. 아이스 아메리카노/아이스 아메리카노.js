function solution(money) {
    var answer = [];
    
    const count = Math.floor(money / 5500)
    const remainder = (money % 5500)
    
    answer.push(count)
    answer.push(remainder)
    
    return answer;
}