// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim();

let n = Number(input);

// 출력
if (n >= 80) {
    console.log("pass");
}
else {
    console.log(`${80 - n} more score`);
}
