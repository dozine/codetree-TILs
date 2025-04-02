const fs=require("fs");
let a = Number(fs.readFileSync(0).toString());

let result = a+2
console.log(result)