#!/bin/bash
set -ex

mkdir -p testfiles
chmod 777 testfiles

ACCESS=(700 500 100 000)
for A in ${ACCESS[*]}
do
    FILE="useraccess$A"
    echo "$USER $A" > testfiles/$FILE
    chmod $A testfiles/$FILE
    FILE="rootaccess$A"
    echo "root $A" > testfiles/$FILE
    chmod $A testfiles/$FILE
    sudo chown root:wheel testfiles/$FILE
done
