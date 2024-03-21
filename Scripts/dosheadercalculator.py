#import used to work with OS functionality
import os
#import used to optimise portable executable file functionality
import pefile
#import used to generate cryptographic hash of pe file section
import hashlib

#Function used to generate hash of DOS Header
def calculate_dos_header_hash(pe):

    #Assuming DOS Header is always first 64 bytes. Hash the first 64 bytes
    dos_header_data = pe.__data__[:64] 
    return hashlib.sha256(dos_header_data).hexdigest()

#Directing the path to where portable executable files are stored.
path_to_files = "/home/b00132407/Desktop/WannaCry/"

#Dictionary to store calculated DOS Header hash values
dos_header_hash_values = {}

#Loop through each file in directory 
for filename in os.listdir(path_to_files):
    file_path = os.path.join(path_to_files, filename)

    #Open and read file
    with open(file_path, "rb") as f:
        pe = pefile.PE(data=f.read())

    #Calculate DOS Header hash value 
    dos_header_hash = calculate_dos_header_hash(pe)

    #Check if value already in dictionary
    if dos_header_hash in dos_header_hash_values:

        #If value already in append to list 
        dos_header_hash_values[dos_header_hash].append(filename)
    else:
        #Else add to dictionary
        dos_header_hash_values[dos_header_hash] = [filename]

#Open new file in write mode to add calculated values
with open("/home/b00132407/Desktop/DOSHashOutput/WannaCryDOSHeaderHashInformation.txt", "w") as f:
    for dos_header_hash, filenames in dos_header_hash_values.items():
        #List number of files related to specific rich hash value
        f.write(f"Number of files related with DOS Header Hash value: {dos_header_hash} ({len(filenames)} files):\n")
        #List specific files containing rich hash value
        for index, filename in enumerate(filenames, start=1):
            f.write(f"{index}. {filename}\n")
        f.write("\n")
