const text = require("fs").readFileSync(0, "utf8").split("\n")[0];
const letters = text.toLowerCase().replace(/[^a-z0-9]/g, "");
console.log(letters === [...letters].reverse().join("") ? "true" : "false");
