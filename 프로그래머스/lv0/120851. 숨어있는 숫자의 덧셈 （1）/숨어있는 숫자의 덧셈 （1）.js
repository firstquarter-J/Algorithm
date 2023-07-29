function solution(my_string) {
    let answer = 0;
    const array = [...my_string];
    
    for (let i in array) {
        if (!isNaN(array[i])) {
            answer += parseInt(array[i])
        }
    }
    
    return answer;
}