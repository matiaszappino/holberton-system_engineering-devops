#!/usr/bin/node

const fs = require('fs')
fs.readFile(`${process.argv.slice(2)}`, 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }
  console.log(data)
})
