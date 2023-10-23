#!/usr/bin/env bash

echo "Bash script to compile & run java implementation"

cd java/src
javac Main.java && java Main

echo "Move file to top level location"
mv voltron-pve-filter.txt ../..
