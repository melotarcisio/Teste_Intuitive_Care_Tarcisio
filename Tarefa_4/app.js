const express = require('express')
const app = express();
var http = require('http')
const fs = require('fs')
var parse = require('csv-parse');
const levenshtein = require('js-levenshtein');

global.rela_torio = [ ]

fs.readFile('Relatorio_cadop.csv','UTF8', function (err, fileData){
  parse(fileData,{columns: false,delimiter: ';', trim: true}, function(err, rows) {
    rela_torio = rows
  })
})

app.use(express.urlencoded({ extended: false }))
app.use(express.json())

app.get('/', function(req,res){
    res.sendFile(__dirname + "/index.html")
})

app.get('/search', function(req,res){
    par_ = req.headers.src
    result = src(par_)
    console.log('get')
    //res.sendFile(__dirname + "/text.json")
    res.send("Texto: " + par_ + rela_torio[2])
})
var src = function(par){
  i = 0
  for (var j = 0; j < rela_torio.length; j++) {
    n = levenshtein(par,rela_torio[j])
    if (n >= ref)
      result[i] = rela_torio[j]
      i++
  }
  return par
}



app.listen(8080, function(req,res){console.log('Servidor Rodando na url http://localhost:8080')})
