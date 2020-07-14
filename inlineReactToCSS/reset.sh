#!/bin/bash
rm ./input/*
cp ./inline/* ./input
prettier --write ./input/*
