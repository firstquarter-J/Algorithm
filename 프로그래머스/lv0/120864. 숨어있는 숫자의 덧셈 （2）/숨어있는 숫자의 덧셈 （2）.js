function solution(my_string) {
    return my_string.match(/\d+/g) ? my_string.match(/\d+/g).reduce((a, c) => a + Number(c), 0) : 0
}