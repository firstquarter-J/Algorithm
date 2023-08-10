// function solution(my_string) {
//     let answer = '';
//     const strArr = [...my_string];
    
//     for (let i in strArr) {
//         if (strArr[i] === strArr[i].toUpperCase()) {
//             answer += strArr[i].toLowerCase();        
//         } else {
//             answer += strArr[i].toUpperCase();
//         }
//     }
    
//     return answer;
// }

// function solution(my_string) {
//     let answer = '';
    
//     for (let i of my_string) answer += i === i.toUpperCase() ? i.toLowerCase() : i.toUpperCase();
    
//     return answer;
// }

function solution(my_string) {
    return [...my_string].map((v) => v === v.toUpperCase() ? v.toLowerCase() : v.toUpperCase()).join('');
}

