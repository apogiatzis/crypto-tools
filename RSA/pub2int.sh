#!/bin/bash
echo "[-] Public Key File: $1"
openssl rsa -pubin -inform PEM -text -noout < $1  > pub2int.dat

echo '[+] Modulus'
modulus=$(awk '/Modulus:/{flag=1;next}/Exponent/{flag=0}flag' < pub2int.dat | tr -d ":    \n")
echo $modulus
echo -e "\n"

echo "[+] Exponent"
exponent=$(awk '/Exponent:/,0' < pub2int.dat | awk '{gsub("Exponent", "");print}' | tr -d ":    \n")
echo $exponent
echo -e "\n"

rm pub2int.dat
