## Challenge

wont-somebody-think-of-the-children

If Loab is back, we might need the council to help us out. The problem is that Anna sent Maya looking for them but she still hasn't come back. This is her last known location... Maybe you can help find her.

I'd go, but I really don't want to be around those spooky ghost orphans.

## Solution

We opened the svg file on the browser and found a picture.

Noticed it was 28MB, so we thought of extracting the files of the svg.

This script extracted all the images from it and the ![photo](./extracted_image_5.png) had the flag.

```python
import re
import base64

with open('yeoldeorphanarium.svg', 'r') as file:
    svg_content = file.read()

image_data_list = re.findall(r'data:image/(.*?);base64,(.*?)"', svg_content)

for index, (img_type, b64_data) in enumerate(image_data_list):
    img_data = base64.b64decode(b64_data)
    file_extension = img_type.split(";")[0]
    filename = f"extracted_image_{index + 1}.{file_extension}"
    with open(filename, 'wb') as img_file:
        img_file.write(img_data)
    print(f"Saved {filename}")

print("Extraction complete!")
```


Flag: `NICC{H3ck_th3m_kids_what_@bout_the_council?}`