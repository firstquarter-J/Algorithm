function solution(my_string) {
    let answer = '';
    const strArr = [...my_string];
    
    for (let i in strArr) {
        if (strArr[i] === strArr[i].toUpperCase()) {
            answer += strArr[i].toLowerCase();        
        } else {
            answer += strArr[i].toUpperCase();
        }
    }
    
    return answer;
}