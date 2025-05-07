const fs = require("fs")
let input = fs.readFileSync(0).toString().trim().split("-")

let first = Number(input[0])
let second = Number(input[1])

console.log(`${first}${second}`)