const fs = require('fs');
const content = fs.readFileSync('e:\\Machine Project\\pitoon\\LogiHub - Logistic HTML Template\\products_temp.txt', 'utf16le'); // Try utf16le since tool warned about it

const blocks = content.split('<div class="cs-blog-item');
blocks.forEach((block, i) => {
    if (i === 0) return;
    const imgMatch = block.match(/assets\/IU\s*\((\d+)\)\.png/);
    const titleMatch = block.match(/<h5>([^<]+)<\/h5>/);
    const linkMatch = block.match(/href="([^"]+\.html)"/);

    if (titleMatch) {
        console.log(`Title: ${titleMatch[1].trim()}`);
        if (imgMatch) console.log(`  Image: assets/IU (${imgMatch[1]}).png`);
        if (linkMatch) console.log(`  Link: ${linkMatch[1]}`);
    }
});
