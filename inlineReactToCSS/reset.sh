#!/bin/bash
[[ $(ls -A ./input) ]] && rm ./input/*
rm -f ./inline_conversion
cp ./inline/* ./input
prettier --write ./input/*
