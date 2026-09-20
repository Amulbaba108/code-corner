const [a, b] = require("fs").readFileSync(0, "utf8").split("\n")[0].split(",");
const key = (s) => [...s.toLowerCase().replace(/\s/g, "")].sort().join("");
console.log(key(a) === key(b) ? "true" : "false");
