function solution(rsp) {
    let answer = '';
    const rspArr = [...rsp];
    
    for (let i in rspArr) {
        if (rspArr[i] === '2') answer += '0'
        if (rspArr[i] === '0') answer += '5'
        if (rspArr[i] === '5') answer += '2'
    }
    
    return answer;
}