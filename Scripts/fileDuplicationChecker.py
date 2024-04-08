def count_file_occurrences(file_path):
    file_counts = {}
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip().endswith('.exe'):
                file_name = line.strip()
                if file_name not in file_counts:
                    file_counts[file_name] = 1
                else:
                    file_counts[file_name] += 1
    
    return file_counts

def write_output_to_file(file_occurrences, output_file):
    with open(output_file, 'w') as file:
        for file_name, count in file_occurrences.items():
            file.write(f"{file_name}: {count} times\n")

def main():
    input_file = '/home/b00132407/Desktop/richimphashOutput/StealcCombinedHashInformation.txt'
    output_file = '/home/b00132407/Desktop/richimphashOutput/FileMatch/Stealcoutput.txt'  # Change this to your desired output file path
    file_occurrences = count_file_occurrences(input_file)
    write_output_to_file(file_occurrences, output_file)

if __name__ == "__main__":
    main()
