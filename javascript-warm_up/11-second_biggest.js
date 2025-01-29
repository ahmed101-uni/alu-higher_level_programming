#!/usr/bin/node
const args = process.argv.slice(2);

if ([0, 1].includes(args.length)) {
  console.log(0);
} else {
  args.sort((a, b) => b - a);
  console.log(+args[1]);
}
