function solution(my_string) {
    var answer = [];
    
    arr = [...my_string];
    
    for (let i in arr) {
        if (!isNaN(arr[i])) {
            answer.push(Number(arr[i]))
            }
    }
    
    answer = insertionSort(answer);
        
    return answer;
}

function insertionSort (array) {
    for (let i = 1; i < array.length; i++) {
        let cur = array[i];
        let left = i - 1;

        while (left >= 0 && array[left] > cur) {
            array[left + 1] = array[left];
            left--;
        }

        array[left + 1] = cur;
        console.log(`${i}회전: ${array}`);
        }
    
    return array;
}

// function solution(my_string) {
//     return [...my_string].filter((v) => !isNaN(v)).map((v) => Number(v)).sort();
// }