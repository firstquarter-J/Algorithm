function solution(s) {
    let answer = [];
    
    for (let i in s) {
        if (s.indexOf(s[i]) === s.lastIndexOf(s[i])) {
            answer.push(s[i]);
        }
    }
    
    return answer.sort().join('');
}
