const fs = require("fs")
let input = fs.readFileSync(0).toString().trim().split("-")

let m = Number(input[0])
let d = Number(input[1])
let y = Number(input[2])

console.log(`${y}.${m}.${d}`)