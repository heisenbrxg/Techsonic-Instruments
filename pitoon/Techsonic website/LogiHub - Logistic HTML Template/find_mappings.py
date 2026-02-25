import re

with open(r'e:\Machine Project\pitoon\LogiHub - Logistic HTML Template\products.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Find all <a> tags with href and <img> tags with src
# This might be tricky because of corruption, but let's try.

images = re.findall(r'assets/IU\s*\(\d+\)\.png', content)
links = re.findall(r'href="([^"]+\.html)"', content)
titles = re.findall(r'<span>([^<]+)</span>', content)

print("Images found:", len(images))
print("Links found:", len(links))

# Let's try to find blocks
blocks = re.split(r'<div class="cs-blog-item', content)
for i, block in enumerate(blocks[1:]):
    print(f"--- Block {i} ---")
    img = re.search(r'assets/IU\s*\(\d+\)\.png', block)
    link = re.search(r'href="([^"]+\.html)"', block)
    title = re.search(r'<h5>([^<]+)</h5>', block)
    if img: print("Image:", img.group(0))
    if link: print("Link:", link.group(1))
    if title: print("Title:", title.group(1))
