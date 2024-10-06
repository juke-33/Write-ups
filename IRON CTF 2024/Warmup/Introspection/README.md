## Challenge

Introspection

Know your inner self and get started with Pwn.

nc pwn.1nf1n1ty.team 31698

## Solution

I noticed that on the inspection.c there is not check for the buffer input.

So i tried to put 1200 characters to overwrite it and it gave me the flag.


Flag: `ironCTF{W0w!_Y0u_Just_OverWrite_the_Nul1!}`