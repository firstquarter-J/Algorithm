// function solution(dot) {
//     let answer = 0;
    
//     if ( dot[0] > 0 && dot[1] > 0 ) {
//         answer = 1;
//     }
//     if ( dot[0] < 0 && dot[1] > 0 ) {
//         answer = 2;
//     }
//     if ( dot[0] < 0 && dot[1] < 0 ) {
//         answer = 3;
//     }
//     if ( dot[0] > 0 && dot[1] < 0 ) {
//         answer = 4;
//     }
    
//     return answer;
// }

function solution(dot) {
    return dot[0] > 0 ? dot[1] > 0 ? 1 : 4 : dot[1] < 0 ? 3 : 2;
}