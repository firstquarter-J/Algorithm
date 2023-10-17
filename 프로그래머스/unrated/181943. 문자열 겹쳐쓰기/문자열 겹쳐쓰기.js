// function solution(my_string, overwrite_string, s) {
//     const str = [...my_string];
//     str.splice(s, overwrite_string.length, overwrite_string);
//     return str.join('');
// }

function solution(my_string, overwrite_string, s) {
    return my_string.slice(0, s) + overwrite_string + my_string.slice(s + overwrite_string.length);
}