// function solution(order) {
//     let answer = 0;
//     const orderArr = order.toString().split('');
    
//     for (let i of orderArr) {
//         if (i !== '0' && Number(i) % 3 === 0) answer += 1;
//     }
    
//     return answer;
// }

// function solution(order) {
//     console.log((order + '').split(/[369]/))
//     return (order + '')
//             .split(/[369]/)
//             .length - 1;
// }

// function solution(order) {
//     return [...order.toString().matchAll(/[3|6|9]/g)].length;
// }

function solution(order) {
    const threeSixNine = new Set([3, 6, 9]);
    
    return order
            .toString()
            .split('')
            .filter((x) => threeSixNine.has(Number(x)))
            .length;
}
