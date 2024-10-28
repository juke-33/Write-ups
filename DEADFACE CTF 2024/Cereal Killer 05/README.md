## Challenge

Cereal Killer 05 [200]

This year, America's politicians are weighing in on the IMPORTANT issues...! As in, which spooky cereal is best?

President Donald Trump also has a favorite monster cereal, but it is secured by a password. As a test of your hacking mettle, oh great Turbo Tactical nerd, we need you to hack the program and gain access to the flag. Good luck!

## Solution

When we downloaded the zip we found it had a jar file.

We put it in a simple java decompiler and got the java file of it.

In the java code we noticed that we have to put a phrase.

This phrase will do some operations with the encryptedURL and if the result starts with https it will continue with the decryption code.

We found the word was "Br00t" and after we tried it we got the flag.

![photo](./Photo1.png)


Flag: `flag{Fr00t-Br00t-is-the-only-cereal-for-Prez-Trump!}`