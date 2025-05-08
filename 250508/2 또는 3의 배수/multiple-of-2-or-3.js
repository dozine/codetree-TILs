// 변수 선언 및 입력
const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());
let result = "";

// 출력
for (let i = 1; i <= n; i++) {
    if (i % 2 === 0 || i % 3 === 0) {
        result += 1 + " ";
    }
    else {
        result += 0 + " ";
    }
}

console.log(result);
