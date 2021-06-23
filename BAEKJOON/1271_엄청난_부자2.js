let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split(" ");

const n = Number(input[0])
const m = Number(input[1])

aver = n / m

console.log(aver)