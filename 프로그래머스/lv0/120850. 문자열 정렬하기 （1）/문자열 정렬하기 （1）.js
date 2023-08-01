// function solution(my_string) {
//     var answer = [];
    
//     arr = [...my_string];
    
//     for (let i in arr) {
//         if (!isNaN(arr[i])) {
//             answer.push(Number(arr[i]))
//             }
//     }
        
//     return answer.sort();
// }

function solution(my_string) {
    return [...my_string].filter((v) => !isNaN(v)).map((v) => Number(v)).sort();
}