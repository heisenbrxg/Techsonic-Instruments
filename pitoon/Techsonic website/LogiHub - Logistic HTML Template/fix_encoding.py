import glob
import codecs

# Find all HTML files
html_files = glob.glob('*.html')

for filename in html_files:
    try:
        # Read the file with UTF-8 encoding
        with codecs.open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Replace various dash encodings
        original_content = content
        content = content.replace('Chennai â€" 603', 'Chennai - 603')
        content = content.replace('Chennai – 603', 'Chennai - 603')  # en-dash
        content = content.replace('Chennai — 603', 'Chennai - 603')  # em-dash
        
        # Only write if changes were made
        if content != original_content:
            with codecs.open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed: {filename}")
        else:
            print(f"No changes: {filename}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")
