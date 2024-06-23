# Bad_Worker

## We created a web application that works offline.

## https://web-bad-worker-lz56g6.wanictf.org

Opened the website on Burp Suite and clicked the Fetch button.

On the requests i got this:
```
GET /DUMMY.txt
```

Changed it to:
```
GET /FLAG.txt
```

I got the flag in the response.

Flag: `FLAG{pr0gr3ssiv3_w3b_4pp_1s_us3fu1}`