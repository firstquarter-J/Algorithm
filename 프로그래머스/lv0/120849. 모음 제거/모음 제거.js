// function solution(my_string) {
//     return my_string.replace(/[aeiou]/g, '');
// }

// function solution(my_string) {
//     let answer = '';
//     const check = ['a', 'e', 'i', 'o', 'u'];
    
//     for (let i in my_string) {
//         if (!check.includes(my_string[i])) answer += my_string[i];
//     }
    
//     return answer;
// }

function solution(my_string) {
    return [...my_string]
        .filter((v) => !['a', 'e', 'i', 'o', 'u'].includes(v))
        .join('');

}