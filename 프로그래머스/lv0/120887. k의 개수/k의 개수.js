function solution(i, j, k) {
    let sum = '';
    for (let x = i; x <= j; x++) {
        sum += String(x);
    }
    return sum.split(k).length - 1;
}