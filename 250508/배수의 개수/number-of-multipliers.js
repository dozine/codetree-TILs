const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");
let cntA = 0, cntB=0

for (let i=0; i<10; i++){
    let x=Number(input[i])
    if (x%3 === 0){
        cntA++;
    }
    if (x%5===0){
        cntB++;
    }
}

console.log(cntA,cntB)