const fs = require("fs");
let a = fs.readFileSync(0).toString().trim();
a = Number(a);

// 출력
if (a >= 113) {
    console.log(1);
}
else {
    console.log(0);
}
