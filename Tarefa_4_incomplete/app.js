const express = require('express')
const app = express();
var http = require('http')
const fs = require('fs')
var parse = require('csv-parse');
const levenshtein = require('levenshtein');
const { RSA_X931_PADDING } = require('constants');

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
app.get('/style.css', function(req,res){
  res.sendFile(__dirname + "/style.css")
})
app.get('/script.vue', function(req,res){
  res.sendFile(__dirname + "/script.vue")
})

app.get('/search', function(req,res){
    par_ = req.headers.src
    result = src(par_)
    console.log('get')
    res.send(result)
})
var src = function(par){
  m1 = 99999
  m2 = 99999
  m3 = 99999
  r1 = ''
  r2 = ''
  r3 = ''
  for (var j = 0; j < rela_torio.length; j++) {
    n = levenshtein(par,rela_torio[j][2])
    console.log(n)
    if(n<m1){
      r1=rela_torio[j]
      m1 = n
    }
    else if(n<m2){
      r2=rela_torio[j]
      m2 = n
    }
    else if(n<m3){
      r3=rela_torio[j]
      m3 = n
    }  
  }
  console.log(r1)
  result = {
      'r1':{ 
        'Registro ANS':r1[0],
        'CNPJ':r1[1],
        'Razão Social':r1[2]
      },
      'r2':{ 
        'Registro ANS':r2[0],
        'CNPJ':r2[1],
        'Razão Social':r2[2]
      },
      'r3':{ 
        'Registro ANS':r3[0],
        'CNPJ':r3[1],
        'Razão Social':r3[2]}
    }
  return JSON.stringify(result)
}



app.listen(8088, function(req,res){console.log('Servidor Rodando na url http://localhost:8088')})
