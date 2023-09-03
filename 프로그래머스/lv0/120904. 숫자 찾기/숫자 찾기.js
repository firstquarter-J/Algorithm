function solution(num, k) {
    let answer = -1;
    const numArr = num.toString().split('');
    
    for (let i = 0; i < numArr.length; i++) {
        if (numArr[i] === String(k)) {
            answer = i + 1;
            break;
        }
    }
    return answer;
}