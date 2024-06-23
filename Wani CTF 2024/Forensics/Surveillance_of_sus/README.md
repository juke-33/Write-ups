# Surveillance_of_sus

## A PC is showing suspicious activity, possibly controlled by a malicious individual.

## It seems a cache file from this PC has been retrieved. Please investigate it!

Found a python script that extracted the photos from the bin file.
```
python3 bmc-tools.py -s Cache_chal.bin -d files/
```

After checking and putting the photos in the correct order we found the flag.

![photo](./Photo1.png)

Flag: `FLAG{RDP_is_useful_yipeee}`