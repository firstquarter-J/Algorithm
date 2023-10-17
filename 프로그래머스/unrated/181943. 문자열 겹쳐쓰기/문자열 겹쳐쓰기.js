function solution(my_string, overwrite_string, s) {
    const str = [...my_string];
    str.splice(s, overwrite_string.length, overwrite_string);
    return str.join('');
}