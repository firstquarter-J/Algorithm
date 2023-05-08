function solution(numbers) {
    var answer = 0;
    
    for ( let i = 0; i < numbers.length; i++ ) {
        let check = numbers[i] * numbers[i+1];
        if ( answer < check ) {
            answer = check;
        }
    }
    
    return answer;
}