// function solution(n, t) {
//     let answer = n;
    
//     for (let i = 1; i <= t; i++) {
//         answer = answer * 2
//     }
//     return answer;
// }

// function solution(n, t) {
//     while (t-- > 0) n *=  2
//     return n;
// }

// function solution(n, t) {
//     return n * Math.pow(2, t);
// }

function solution(n, t) {
    return n << t;
}