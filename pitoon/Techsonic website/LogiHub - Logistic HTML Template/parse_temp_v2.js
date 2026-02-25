const fs = require('fs');
// Use a buffer to read and try to handle different encodings if necessary
const buf = fs.readFileSync('e:\\Machine Project\\pitoon\\LogiHub - Logistic HTML Template\\products_temp.txt');
let content = buf.toString('utf16le'); // Try utf16le first

// Check if it looks like garbage, if so try utf8
if (content.includes('\uFFFD') || !content.includes('<html')) {
    content = buf.toString('utf8');
}

const blocks = content.split(/<div class="cs-blog-item/i);
blocks.forEach((block, i) => {
    if (i === 0) return;
    const imgMatch = block.match(/assets\/IU\s*\((\d+)\)\.png/);
    const titleMatch = block.match(/<h5>([^<]+)<\/h5>/);
    const linkMatch = block.match(/href="([^"]+\.html)"/);

    if (titleMatch) {
        let out = `Block ${i}: Title: ${titleMatch[1].trim()}`;
        if (imgMatch) out += ` | Image: assets/IU (${imgMatch[1]}).png`;
        if (linkMatch) out += ` | Link: ${linkMatch[1]}`;
        console.log(out);
    }
});
