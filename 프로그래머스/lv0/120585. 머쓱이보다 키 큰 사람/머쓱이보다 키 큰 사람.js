function solution(array, height) {
    let answer = array.filter((arr) => arr > height).length;
    return answer;
}