// function solution(i, j, k) {
//     let sum = '';
//     for (let x = i; x <= j; x++) {
//         sum += String(x);
//     }
//     return sum.split(k).length - 1;
// }

function solution(i, j, k) {
    let sum = '';
    for (i; i<= j; i++) {
        sum += String(i);
    }
    
    return sum.split(k).length - 1;
}
