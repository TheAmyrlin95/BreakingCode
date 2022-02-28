#!/usr/bin/bash

echo Hello $USER to bash. We are going to list the characters from Encanto.

mkdir Encanto
#LowerCase
touch Abuela Bruno Lusia Camilo Dolores Mirabel

cd Encanto

mkdir GenerationOne GenerationTwo GenerationThree

mv Abuela GenerationOne
#Removed to
mv Bruno GenerationTwo

mv Mirabel GenerationThree

cat Encanto
