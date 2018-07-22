#!/bin/bash

echo "[+] Host: $1"

openssl s_client -connect $1:443 | openssl x509 -pubkey -noout > cert.pem

