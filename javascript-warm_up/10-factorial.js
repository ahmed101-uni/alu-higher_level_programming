#!/usr/bin/node
const arg = +process.argv[2];

if (isNaN(arg)) {
  console.log(1);
} else {
  console.log(fact(arg));
}

function fact (n) {
  if (n === 1) return n;

  return n * fact(n - 1);
}
