// function solution(hp) {
//     fiveCount = Math.floor(hp / 5);
//     threeCount = Math.floor((hp - fiveCount * 5) / 3);
//     oneCount = hp - (fiveCount * 5) - (threeCount * 3);

//     return fiveCount + threeCount + oneCount;
// }

function solution(hp) {
    fiveCount = ~~(hp / 5);
    threeCount = ~~((hp - fiveCount * 5) / 3);
    oneCount = hp - (fiveCount * 5) - (threeCount * 3);

    return fiveCount + threeCount + oneCount;
}