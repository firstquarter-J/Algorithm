function solution(array) {
    let answer = [];
    let checkValue = array[0];
    
    for (let i = 0; i < array.length; i++) {
        if (checkValue < array[i]) checkValue = array[i];
    }
    answer.push(checkValue)
    
    for (let i = 0; i < array.length; i++) {
        if (array[i] === checkValue) answer.push(i)
    }
    
    
    
    return answer;
}