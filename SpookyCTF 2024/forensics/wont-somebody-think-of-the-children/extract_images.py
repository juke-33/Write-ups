# Extract all the images
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