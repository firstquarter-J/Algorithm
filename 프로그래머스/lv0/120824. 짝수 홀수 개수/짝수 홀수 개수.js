function solution(num_list) {
    // const answer = [];
    let evenNumber = 0;
    let oddNumber = 0;
    
    for ( let i = 0; i < num_list.length; i++ ) {
        num_list[i] % 2 === 0 ? evenNumber += 1 : oddNumber += 1
    }
    // answer.push(evenNumber, oddNumber)
    // return answer;
    return [evenNumber, oddNumber]
}