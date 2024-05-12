#import used to work with OS functionality
import os 
#import used to optimise portable executable file functionality
import pefile

#Directing the path to where portable executable files are stored.
path_to_files = "/home/b00132407/Desktop/Vidar/"

#Dictionary to store calculated imphash and rich hash values
combined_values = {}

#Loop through each file in directory 
for filename in os.listdir(path_to_files):
    file_path = os.path.join(path_to_files, filename)

    #Open and read file.
    with open(file_path, "rb") as f:
        read_file = f.read()

    #Calculate imphash
    file_imphash = pefile.PE(file_path).get_imphash()

    #Calculate rich hash value 
    file_rich_hash = pefile.PE(file_path).get_rich_header_hash()

    #Check if imphash or rich hash already in dictionary
    if file_imphash in combined_values:
        #If imphash already in, append to list 
        combined_values[file_imphash].append(filename)
    else:
        #Else add to the dictionary 
        combined_values[file_imphash] = [filename]

    if file_rich_hash in combined_values:
        #If rich hash already in, append to list 
        combined_values[file_rich_hash].append(filename)
    else:
        #Else add to the dictionary 
        combined_values[file_rich_hash] = [filename]

#Open new file in write mode to add calculated values
with open("/home/b00132407/Desktop/richimphashOutput/VidarCombinedHashInformation.txt", "w") as f:
    
    #Iterate through dictionary to values
    for hash_value, filenames in combined_values.items():
        if len(filenames) >= 2 and hash_value is not None and hash_value != "":
            #List number of files related to specific hash value
            f.write(f"Number of files related with Hash value: {hash_value} ({len(filenames)} files):\n")
            #List specific files containing hash value
            for index, filename in enumerate(filenames, start=1):
                f.write(f"{index}. {filename}\n")
            f.write("\n")
