#!/bin/bash
rm -rf *.py
rm -rf core
git clone https://github.com/Darksoul8/HunterSearch
git clone https://github.com/Darksoul8/HunterSearch/core
mv ./HunterSearch/* ./
rm -rf HunterSearch 
chmod +x *
