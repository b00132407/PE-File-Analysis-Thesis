#import used to work with OS functionality
import os 
#import used to optimise portable executable file functionality
import pefile

#Directing the path to where portable executable files are stored.
path_to_files = "/home/b00132407/Desktop/Stealc/"

#Dictionary to store calculated exphash values
exphash_values = {}

#Loop through each file in directory 
for filename in os.listdir(path_to_files):
    file_path = os.path.join(path_to_files, filename)

    #Open and read file.
    with open(file_path, "rb") as f:
        read_file = f.read()

    #Calculate exphash
    file_exphash = pefile.PE(file_path).get_exphash()

    #Check if value already in dictionary
    if file_exphash in exphash_values:

        #If value already in append to list 
        exphash_values[file_exphash].append(filename)
    else:
        #Else add to the dictionary 
        exphash_values[file_exphash] = [filename]

#Open new file in write mode to add calculated values to it
with open("/home/b00132407/Desktop/exphashOutput/StealCExpHashInformation.txt", "w") as f:
    
    #Iterate through dictionary to values
    for exphash, filenames in exphash_values.items():
        #List number of files related to specific exphash value
        f.write(f"Number of files related with ExpHash value: {exphash} ({len(filenames)} files):\n")
        #List specific files containing exphash value
        for index, filename in enumerate(filenames, start=1):
            f.write(f"{index}. {filename}\n")
        f.write("\n")
