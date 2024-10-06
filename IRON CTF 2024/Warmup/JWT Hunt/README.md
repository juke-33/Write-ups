## Challenge

JWT Hunt

Scavenger hunts are a blast, so I've woven one into this challenge. Test your skills and see if you can uncover the treasure you seek!

https://jwt-hunt.1nf1n1ty.team/

## Solution

First of all we tried to register and when we opened the cookie we found the secretkeypart2.

After that we searched for robots.txt where we found secretkeypart1 and a path about another key part.

Since robots existed we tried the sitemap.xxml, where we found the secretkeypart3.

When we tried to access /secretkeypart4 we got a bad request.

So we tried to open the path on Burp Suite and use the HEAD method, which gave us the secretkeypart4.

We combined all the parts and put it on the cookie we got at first at jwt.io to verify signature and also changed the username to "admin".

We put this as a cookie and we got the flag


Flag: `ironCTF{W0w_U_R34lly_Kn0w_4_L07_Ab0ut_JWT_3xp10r4710n!}`