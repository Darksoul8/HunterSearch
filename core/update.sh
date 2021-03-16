#!/bin/bash
rm -rf *.py
rm -rf core
git clone https://github.com/Darksoul8/HunterSearch
mv ./HunterSearch/* ./
rm -rf HunterSearch 
chmod +x *
