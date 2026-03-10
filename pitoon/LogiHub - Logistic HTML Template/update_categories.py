import codecs
import re

lines = [l.strip("\r\n").strip() for l in codecs.open('categories.txt', 'r', 'utf-8').readlines()]

main_categories = [
    "ELECTRONICS & INSTRUMENTATION ENGINEERING (E&I)",
    "ELECTRICAL & ELECTRONICS ENGINEERING (EEE)",
    "ELECTRONICS & COMMUNICATION ENGINEERING (ECE)",
    "MECHANICAL ENGINEERING",
    "MECHATRONIC ENGINEERING",
    "CIVIL ENGINEERING",
    "CHEMICAL ENGINEERING (New Department)",
    "PETROLEUM ENGINEERING",
    "AGRICULTURAL ENGINEERING (New Department)",
    "FOOD ENGINEERING (New Department)",
    "RENEWABLE ENERGY ENGINEERING (New Department)",
    "MEDICAL ELECTRONICS"
]

extra_categories = [
    "BIO MEDICAL ENGINEERING",
    "AEROSPACE ENGINEERING",
    "AERONAUTICAL ENGINEERING",
    "AUTOMOBILE ENGINEERING",
    "POLYMER ENGINEERING",
    "PRODUCTION ENGINEERING"
]

link_map = {
    "ELECTRONICS & INSTRUMENTATION ENGINEERING (E&I)": "EIEngineering.html",
    "ELECTRICAL & ELECTRONICS ENGINEERING (EEE)": "EEEEngineering.html",
    "ELECTRONICS & COMMUNICATION ENGINEERING (ECE)": "ECEEngineering.html",
    "MECHANICAL ENGINEERING": "MechanicalEngineering.html",
    "CIVIL ENGINEERING": "CivilEngineering.html",
    "MECHATRONIC ENGINEERING": "MechatronicEngineering.html",
    "CHEMICAL ENGINEERING (New Department)": "ChemicalEngineering.html",
    "PETROLEUM ENGINEERING": "PetroleumEngineering.html",
    "AGRICULTURAL ENGINEERING (New Department)": "AgriculturalEngineering.html",
    "FOOD ENGINEERING (New Department)": "FoodEngineering.html",
    "RENEWABLE ENERGY ENGINEERING (New Department)": "RenewableEnergyEngineering.html",
    "MEDICAL ELECTRONICS": "MedicalElectronics.html",
    "BIO MEDICAL ENGINEERING": "BioMedicalEngineering.html",
    "AEROSPACE ENGINEERING": "AerospaceEngineering.html",
    "AERONAUTICAL ENGINEERING": "AeronauticalEngineering.html",
    "AUTOMOBILE ENGINEERING": "AutomobileEngineering.html",
    "POLYMER ENGINEERING": "PolymerEngineering.html",
    "PRODUCTION ENGINEERING": "ProductionEngineering.html"
}

data = []
curr_cat = None
curr_lab = None

for line in lines:
    if not line:
        curr_lab = None
        continue
        
    if line in main_categories:
        curr_cat = {"name": line, "labs": []}
        data.append(curr_cat)
        curr_lab = None
        continue
        
    if curr_lab is None:
        curr_lab = {"name": line, "items": []}
        if curr_cat:
            curr_cat["labs"].append(curr_lab)
    else:
        curr_lab["items"].append(line)

for extra in extra_categories:
    data.append({"name": extra, "labs": []})

html = ['<ul class="cat-accordion-list">']
for cat in data:
    html.append('    <li>')
    html.append('        <button class="cat-parent-btn" onclick="toggleCat(this)">')
    link = link_map.get(cat["name"], "#")
    html.append(f'            <a class="cat-parent-link" href="{link}">{cat["name"]}</a>')
    html.append('            <i class="cat-toggle-icon">&#9656;</i>')
    html.append('        </button>')
    html.append('        <ul class="cat-sub-list">')
    
    for lab in cat["labs"]:
        html.append(f'            <li><strong>{lab["name"]}</strong></li>')
        for item in lab["items"]:
            html.append(f'            <li><a href="#">{item}</a></li>')
            
    html.append('        </ul>')
    html.append('    </li>')

html.append('</ul>')

html_str = '\n'.join(html)

with codecs.open("forcollege.html", "r", "utf-8") as f:
    content = f.read()

start_marker = '<ul class="cat-accordion-list">'
idx_start = content.find(start_marker)

# Finding the end of the ul element properly
import builtins
count = 0
found_end = -1
# naive approach to find closing ul matching the opening one since we know it's there
# we just look for `</ul>\n                                                </div>`
end_marker = '</ul>\n                                                </div>\n                                            </div>\n                                        </div>\n                                        <div class="cs-widget-item cs-widget-leftborder">'
idx_end = content.find(end_marker, idx_start)

if idx_end != -1:
    new_content = content[:idx_start] + html_str + content[idx_end + 5:]

    with codecs.open("forcollege.html", "w", "utf-8") as f:
        f.write(new_content)
    print("Updated successfully!")
else:
    print("Could not find end marker!")
    # Let's try alternative
    idx_end2 = content.find('</ul>', content.find('PRODUCTION ENGINEERING'))
    if idx_end2 != -1:
        new_content = content[:idx_start] + html_str + content[idx_end2 + 5:]
        with codecs.open("forcollege.html", "w", "utf-8") as f:
            f.write(new_content)
        print("Updated successfully using fallback!")

