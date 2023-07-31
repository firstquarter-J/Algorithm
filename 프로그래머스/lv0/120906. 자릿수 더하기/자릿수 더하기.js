function solution(n) {
    
    let nArr = (n + '').split('');
    
    return nArr.reduce((acc, cur) => Number(acc) + Number(cur), 0);
}