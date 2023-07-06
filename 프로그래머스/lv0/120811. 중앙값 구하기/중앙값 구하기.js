// function solution(array) {
//     // 배열 삽입 정렬
//     for ( let i = 1; i < array.length; i++ ) {
//         const checkValue = array[i];
//         let left = i - 1;
        
//         while ( left >= 0 && array[left] > checkValue ) {
//             array[left+1]  = array[left];
//             left--;
//         }
//         array[left+1] = checkValue;
//     }

//     // 배열 길이 / 2 (Math.floor 로 나머지 버림)
//     const center = Math.floor(array.length / 2)
//     return array[center];
// }

function solution(array) {
    // 배열 정렬 (sort 함수)
    const sortedArr = array.sort((a, b) => a - b);
    const center = Math.floor(sortedArr.length / 2)
    return sortedArr[center]
}