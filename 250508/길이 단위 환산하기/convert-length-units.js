const fs = require("fs");
let ft = 30.48
let n = fs.readFileSync(0).toString();
n = Number(n);
let result = ft*n
console.log(result.toFixed(1))
