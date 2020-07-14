#!/bin/bash
[[ $(ls -A ./input) ]] && rm ./input/*
cp ./inline/* ./input
prettier --write ./input/*
