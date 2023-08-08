// function solution(cipher, code) {
//     let answer = '';
    
//     for (let i = code - 1; i < cipher.length; i += code) {
//             answer += cipher[i];
//     }

//     return answer;
// }

function solution(cipher, code) {
    return [...cipher].filter((_, index) => (index + 1) % code === 0).join('');
}