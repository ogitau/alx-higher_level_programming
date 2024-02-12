#!/usr/bin/node

const count = parseInt(process.argv[2]);
const char = 'X';

if (typeof count === 'number' && isNaN(count) === false) {
  for (let i = 0; i < count; i++) {
    console.log(char.repeat(count));
  }
} else {
  console.log('Missing size');
}
