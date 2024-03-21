#import used to work with OS functionality
import os
#import used to optimise portable executable file functionality
import pefile
#import used to generate cryptographic hash of pe file section
import hashlib

#Function used to generate hash of .rsrc section
def calculate_rsrc_hash(pe):
    for section in pe.sections:
        if section.Name.decode().strip('\x00') == '.rsrc':
            rsrc_data = section.get_data()
            return hashlib.sha256(rsrc_data).hexdigest()

#Directing the path to where portable executable files are stored.
path_to_files = "/home/b00132407/Desktop/Conti/"

#Dictionary to store calculated .data hash values
rsrc_hash_values = {}

#Loop through each file in directory 
for filename in os.listdir(path_to_files):
    file_path = os.path.join(path_to_files, filename)

    #Open and read file
    with open(file_path, "rb") as f:
        pe = pefile.PE(data=f.read())

    #Calculate .rsrc hash value 
    rsrc_hash = calculate_rsrc_hash(pe)

    #Check if value already in dictionary
    if rsrc_hash in rsrc_hash_values:

        #If value already in append to list 
        rsrc_hash_values[rsrc_hash].append(filename)
    else:
        #Else add to dictionary
        rsrc_hash_values[rsrc_hash] = [filename]

#Open new file in write mode to add calculated values
with open("/home/b00132407/Desktop/rsrcOutput/ContiRsrcHashInformation.txt", "w") as f:
    for rsrc_hash, filenames in rsrc_hash_values.items():
        #List number of files related to specific rich hash value
        f.write(f"Number of files related with RsrcHash value: {rsrc_hash} ({len(filenames)} files):\n")
        #List specific files containing rich hash value
        for index, filename in enumerate(filenames, start=1):
            f.write(f"{index}. {filename}\n")
        f.write("\n")
