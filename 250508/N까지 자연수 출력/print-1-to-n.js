// 변수 선언 및 입력
const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());

let i = 1;
let result = "";

while (i <= n) {
    result += i + " ";
    i++;
}

// 출력
console.log(result);