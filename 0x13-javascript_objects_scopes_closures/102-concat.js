#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  process.exit(1);
}

const concatfiles = fs.readFileSync(process.argv[2], 'utf8') + fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], concatfiles);
