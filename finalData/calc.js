var fs = require("fs");
var spreads = JSON.parse(fs.readFileSync("./spreads.json", "utf8"));
var votes = JSON.parse(fs.readFileSync("./votes.json", "utf8"));


console.log("Votes: "+votes.length);

var calcVotes = spreads.reduce(function(a, spread) {
  return a + spread.fact + spread.fiction;
}, 0);

//console.log("Calculated Votes: "+calcVotes);

var percentages = spreads.map(function(a) {
  var total = a.fact + a.fiction;
  return {
    spreadId : a.spreadId,
    fact : a.fact,
    fiction : a.fiction,
    factPerc : parseInt(Math.round(a.fact / total * 100)),
    fictionPerc:  parseInt(Math.round(a.fiction / total * 100))
  }
});

console.log("Percentages: ", percentages)
var sorted = percentages.sort(function(a, b) {
  return (b.fact + b.fiction) - (a.fact + a.fiction);
});
console.log("Most Voted: ", sorted.slice(0,1));
var sorted = percentages.sort(function(a, b) {
  return (b.fictionPerc) - (a.fictionPerc);
});
console.log("Most Fiction: ", sorted[0]);
console.log("Most Fact: ", sorted[sorted.length - 1]);
