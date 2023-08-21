function solution(order) {
    let answer = 0;
    const orderArr = order.toString().split('');
    
    for (let i of orderArr) {
        if (i !== '0' && Number(i) % 3 === 0) answer += 1;
    }
    
    return answer;
}