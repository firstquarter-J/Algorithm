const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    solution(Number(input[0]));
});

function solution(input) {
    // let star = '';
    // for (let i = 0; i < input; i++) {
    //     for ( let j = 0; j <= i; j++) {
    //         star += '*';
    //     }
    //     star += '\n';
    // }
    // console.log(star);
    for (let i = 1; i <= input; i++) {
        console.log('*'.repeat(i));
    }
}
