// function solution(rsp) {
//     let answer = '';
//     const rspArr = [...rsp];
    
//     for (let i in rspArr) {
//         if (rspArr[i] === '2') answer += '0'
//         if (rspArr[i] === '0') answer += '5'
//         if (rspArr[i] === '5') answer += '2'
//     }
    
//     return answer;
// }

function solution(rsp) {
    const rspObject = {
        2: 0,
        0: 5,
        5: 2
    }
    
    return [...rsp].map(v => rspObject[v]).join('')
}