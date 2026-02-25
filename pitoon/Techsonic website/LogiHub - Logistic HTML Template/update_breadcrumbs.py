import os
import re

files = [
    "forcollege.html",
    "products.html",
    "Conveyor Lines.html",
    "iPhone Charging Rack.html",
    "Fumes extractors.html",
    "PCB separator.html",
    "DC Power Supply.html",
    "Digital Torque meter.html",
    "Microscope and Magnifier.html",
    "Automatic air shower and pass box.html",
    "ESD entry controlled Tripod.html",
    "ESD packages and accessories.html",
    "Rework station and soldering station.html",
    "AdvancedDigitalDrives.html",
    "CommunicationTrainers.html",
    "ControlSystemTrainers.html",
    "DigitalSignalProcessing.html",
    "EmbeddedTechnology.html",
    "InstrumentationTrainers.html",
    "InternetofThings.html",
    "MechanicalLabs.html",
    "Microprocessor&Controller.html",
    "PLCApplicationModules.html",
    "PowerElectronicsTrainers.html",
    "PowerSystemTrainers.html",
    "ProcessControlTrainers.html",
    "RFMicrowaveTrainers.html",
    "RoboticsLabs.html",
    "SmartGridProducts.html",
    "SpecialProducts.html",
    "VLSITechnology.html",
    "WirelessSensorNetwork.html",
    "DigitalTwinsIndustry4.0.html"
]

target_dir = r"e:\Machine Project\pitoon\LogiHub - Logistic HTML Template"
new_tag = '<div class="cs-braidcrumb-wrap img-scroll-object-zoom" data-src="assets/img/bannerproduct.png">'

# Regex to match the tag, capturing format flexibility if needed, 
# but specifically targeting the class and data-src attribute.
# We want to replace the whole opening tag.
tag_pattern = re.compile(r'<div class="cs-braidcrumb-wrap img-scroll-object-zoom"\s+data-src="[^"]+">')

for filename in files:
    file_path = os.path.join(target_dir, filename)
    if not os.path.exists(file_path):
        print(f"File not found: {filename}")
        continue
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if replacement is needed
        if tag_pattern.search(content):
            new_content = tag_pattern.sub(new_tag, content)
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated: {filename}")
            else:
                print(f"No change needed (content same): {filename}")
        else:
            print(f"Pattern not found in: {filename}")
            # Fallback for exact string match if regex fails (e.g. different spacing)
            # but let's just log it first.
            
    except Exception as e:
        print(f"Error processing {filename}: {e}")
