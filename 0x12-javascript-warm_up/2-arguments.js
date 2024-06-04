#!/usr/bin/node
// prints a message depending of the number of arguments passed

const args = process.argv;
const argsLen = args.length;
if (argsLen < 3) {
  console.log('No argument');
} else if (argsLen === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
