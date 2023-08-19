function solution(age) {
    let answer = '';
    const ageArr = String(age).split('');
    
    for (let i = 0; i < ageArr.length; i++) {
        if (ageArr[i] === '0') answer += 'a'
        if (ageArr[i] === '1') answer += 'b'
        if (ageArr[i] === '2') answer += 'c'
        if (ageArr[i] === '3') answer += 'd'
        if (ageArr[i] === '4') answer += 'e'
        if (ageArr[i] === '5') answer += 'f'
        if (ageArr[i] === '6') answer += 'g'
        if (ageArr[i] === '7') answer += 'h'
        if (ageArr[i] === '8') answer += 'i'
        if (ageArr[i] === '9') answer += 'j'
    }
    
    return answer;
}