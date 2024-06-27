# Enumerate me

## In this challenge, the flag has been hidden inside one of the website files.

## The files to enumerate is one of the listed into test.txt wordlist in Discovery directory of this repo

## Will you be able to find it?

## https://github.com/danielmiessler/SecLists

## http://ctf.thehackerconclave.es:20001/

In the Discovery directory i found a tests.txt file.
```
dirb http://ctf.thehackerconclave.es:20001/ tests.txt
```

It found this page http://ctf.thehackerconclave.es:20001/prueba1 that had the flag in base64 format.

Flag: `conclave{7f52fcea1237b66122bd091b75642371}`