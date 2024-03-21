#import used to work with OS functionality
import os
#import used to optimise portable executable file functionality
import pefile
#import used to generate cryptographic hash of pe file section
import hashlib

#Function used to generate hash of .text section
def calculate_text_hash(pe):
    for section in pe.sections:
        if section.Name.decode().strip('\x00') == '.text':
            text_data = section.get_data()
            return hashlib.sha256(text_data).hexdigest()

#Directing the path to where portable executable files are stored.
path_to_files = "/home/b00132407/Desktop/Formbook/"

#Dictionary to store calculated .text hash values
text_hash_values = {}

#Loop through each file in directory 
for filename in os.listdir(path_to_files):
    file_path = os.path.join(path_to_files, filename)

    #Open and read file
    with open(file_path, "rb") as f:
        pe = pefile.PE(data=f.read())

    #Calculate .text hash value 
    text_hash = calculate_text_hash(pe)

    #Check if value already in dictionary
    if text_hash in text_hash_values:

        #If value already in append to list 
        text_hash_values[text_hash].append(filename)
    else:

        #Else add to dictionary
        text_hash_values[text_hash] = [filename]

#Open new file in write mode to add calculated values
with open("/home/b00132407/Desktop/textOutput/FormbookTextHashInformation.txt", "w") as f:

    #Iterate through dictionary to values
    for text_hash, filenames in text_hash_values.items():
        #List number of files related to specific rich hash value
        f.write(f"Number of files related with TextHash value: {text_hash} ({len(filenames)} files):\n")
        #List specific files containing rich hash value
        for index, filename in enumerate(filenames, start=1):
            f.write(f"{index}. {filename}\n")
        f.write("\n")
