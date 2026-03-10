import codecs
import re

with codecs.open('forcollege.html', 'r', 'utf-8') as f:
    content = f.read()

to_append = '''
    <li class="cs-text_b_line"><a href="BioMedicalEngineering.html"><span>BIO MEDICAL ENGINEERING</span></a></li>
    <li class="cs-text_b_line"><a href="AerospaceEngineering.html"><span>AEROSPACE ENGINEERING</span></a></li>
    <li class="cs-text_b_line"><a href="AeronauticalEngineering.html"><span>AERONAUTICAL ENGINEERING</span></a></li>
    <li class="cs-text_b_line"><a href="AutomobileEngineering.html"><span>AUTOMOBILE ENGINEERING</span></a></li>
    <li class="cs-text_b_line"><a href="PolymerEngineering.html"><span>POLYMER ENGINEERING</span></a></li>
    <li class="cs-text_b_line"><a href="ProductionEngineering.html"><span>PRODUCTION ENGINEERING</span></a></li>
</ul>'''

new_content = re.sub(r'(<ul class="cat-accordion-list">.*?)(</ul>)', lambda m: m.group(1) + to_append, content, count=1, flags=re.DOTALL)

with codecs.open('forcollege.html', 'w', 'utf-8') as f:
    f.write(new_content)
print('Restored missing categories!')
