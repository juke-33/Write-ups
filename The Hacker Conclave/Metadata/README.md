# Metadata

## In this challenge, the flag has been hidden inside one of the images on the website. Will you be able to find it?

## http://ctf.thehackerconclave.es:20002/

While reloading the site you bet different photos in the range of 1-20.

Searched every single file till i find the flag in the 9th image.
```
exiftool 9.jpg
```

Flag: `conclave{5d1a323fbc88063c71cd1f6866f7d85d}`