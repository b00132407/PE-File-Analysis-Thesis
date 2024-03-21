#import used to work with OS functionality
import os 
#import used to optimise portable executable file functionality
import pefile

#Directing the path to where portable executable files are stored.
path_to_files = "/home/b00132407/Desktop/Stealc/"

#Dictionary to store calculated rich hash values
rich_hash_values = {}

#Loop through each file in directory 
for filename in os.listdir(path_to_files):
    file_path = os.path.join(path_to_files, filename)

    #Open and read file.
    with open(file_path, "rb") as f:
        read_file = f.read()

    #Calculate rich hash value 
    file_rich_hash = pefile.PE(file_path).get_rich_header_hash()

    #Check if value already in dictionary
    if file_rich_hash in rich_hash_values:

        #If value already in append to list 
        rich_hash_values[file_rich_hash].append(filename)
    else:
        #Else add to the dictionary 
        rich_hash_values[file_rich_hash] = [filename]

#Open new file in write mode to add calculated values
with open("/home/b00132407/Desktop/richOutput/StealCHeaderHashInformation.txt", "w") as f:
    
    #Iterate through dictionary to values
    for rich_hash, filenames in rich_hash_values.items():
        #List number of files related to specific rich hash value
        f.write(f"Number of files related with Rich hash value: {rich_hash} ({len(filenames)} files):\n")
        #List specific files containing rich hash value
        for index, filename in enumerate(filenames, start=1):
            f.write(f"{index}. {filename}\n")
        f.write("\n")

