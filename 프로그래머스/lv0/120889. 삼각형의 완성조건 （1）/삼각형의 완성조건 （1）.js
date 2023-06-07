function solution(sides) {
    var answer = 0;
    
    const sortedArr = sides.sort((a, b) => b - a)
    
    let max = sortedArr[0]
    let sum = sortedArr[1] + sortedArr[2]
    
    if (max < sum) {
        answer = 1
    } else {
        answer = 2    
    }
    
    return answer;
}