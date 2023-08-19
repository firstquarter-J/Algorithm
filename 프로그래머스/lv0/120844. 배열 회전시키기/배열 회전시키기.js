// function solution(numbers, direction) {
//     direction === 'right' ? numbers.unshift(numbers.pop()) : numbers.push(numbers.shift());
    
//     return numbers;
// }


function solution(numbers, direction) {
    return direction === 'right' 
        ? [numbers[numbers.length - 1], ...numbers.slice(0, numbers.length - 1)]
        : [...numbers.slice(1), numbers[0]];
}
