// 변수 선언, 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");
let c = input[0];
let b = Number(input[1]);
let a = Number(input[2]);

// 출력
console.log(c)
console.log(b.toFixed(2));
console.log(a.toFixed(2));
