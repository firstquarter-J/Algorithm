function solution(n, numlist) {
//     var answer = [];
    
//     for ( let i = 0; i < numlist; i ++ ) {
//         if (numlist[i] % n != 0) {
//             numlist.pop(i)
//         }
//     }
//     return numlist;
    
  let answer = numlist.filter((el) => el % n === 0);
    
  return answer;
}