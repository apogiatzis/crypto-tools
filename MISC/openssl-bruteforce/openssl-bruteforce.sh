#!/bin/bash

key=$1
echo -e "[+] Key set: $key"
for i in $(cat ciphers.txt);do openssl enc -d -$i -in ciphertext.txt -out results/$i.txt -a -k $key;done
