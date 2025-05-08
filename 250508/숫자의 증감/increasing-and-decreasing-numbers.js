const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");
let c = input[0];
let n = Number(input[1]);

// 출력
let result = "";
if (c === 'A') {
    for (let i = 1; i <= n; i++) {
        result += i + " ";
    }
}
else {
    for (let i = n; i >= 1; i--) {
        result += i + " ";
    }
}
console.log(result);
