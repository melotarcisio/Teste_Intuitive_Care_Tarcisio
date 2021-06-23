#!/bin/bash
sudo apt update &&
sudo apt install npm -y && 
cd Tarefa_4_incomplete &&
npm init -y && 
npm install nodejs && 
npm install express && 
npm install levenshtein &&
npm install body-parser && 
npm install csv-parse && 
cd .. &&
sudo apt install python3-pip -y &&
pip3 install pandas &&
pip3 install tabula-py && 
pip3 install bs4 && 
pip3 install requests;
