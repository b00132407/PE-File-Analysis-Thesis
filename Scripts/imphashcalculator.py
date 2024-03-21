#import used to work with OS functionality
import os 
#import used to optimise portable executable file functionality
import pefile

#Directing the path to where portable executable files are stored.
path_to_files = "/home/b00132407/Desktop/Stealc/"

#Dictionary to store calculated imphash values
imphash_values = {}

#Loop through each file in directory 
for filename in os.listdir(path_to_files):
    file_path = os.path.join(path_to_files, filename)

    #Open and read file.
    with open(file_path, "rb") as f:
        read_file = f.read()

    #Calculate Imphash
    file_imphash = pefile.PE(file_path).get_imphash()

    #Check if value already in dictionary
    if file_imphash in imphash_values:

        #If value already in append to list 
        imphash_values[file_imphash].append(filename)
    else:
        #Else add to the dictionary 
        imphash_values[file_imphash] = [filename]

#Open new file in write mode to add calculated values to it
with open("StealCImpHashInformation.txt", "w") as f:
    
    #Iterate through dictionary to values
    for imphash, filenames in imphash_values.items():
        #List number of files related to specific imphash value
        f.write(f"Number of files related with ImpHash value: {imphash} ({len(filenames)} files):\n")
        #List specific files containing imphash value
        for index, filename in enumerate(filenames, start=1):
            f.write(f"{index}. {filename}\n")
        f.write("\n")

