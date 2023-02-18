import soundfile as sf
import os

'''
This code checks if the .wav files in a given directory are supported by the soundfile library or not.
The code works similarly to the previous code, but instead of using the sf.read function to read the contents of the file,
it uses the sf.SoundFile context manager to open the file. If the file is supported by the soundfile library, 
the code will successfully open the file and print a message indicating that the file is supported. 
If the file is not supported, the sf.SoundFile context manager will raise an exception, 
and the code in the except block will catch the exception and print a message indicating that the file is not supported, along with the error message.
'''
def check_soundfile_support(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".wav"):
            file_path = os.path.join(directory, filename)
            try:
                with sf.SoundFile(file_path) as f:
                    # Do nothing
                    pass
                print(f"{filename} is supported by soundfile")
            except Exception as e:
                print(f"{filename} is not supported by soundfile: {e}")

#check_soundfile_support("/mnt/ricproject4/commercial_product/data/cv-corpus/cv-corpus-12.0-2022-12-07/ta/converted_train_set")

'''
This code checks if the .wav files in a given directory are corrupted or not. 
The os.listdir function is used to get a list of all the filenames in the directory, 
and a for loop is used to iterate over the filenames. The code checks if each filename ends with ".wav" using the endswith method,
 and if so, it forms the full path to the file using the os.path.join function.

The sf.read function from the soundfile library is then used to try to read the contents of the file. If the file is not corrupted, 
the function will successfully read the file and print a message indicating that the file is not corrupted. If the file is corrupted, 
the sf.read function will raise an exception,and the code in the except block will catch the exception and print a message indicating that the file is corrupted,
along with the error message.
'''
def check_wav_files_corrupted(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".wav"):
            file_path = os.path.join(directory, filename)
            try:
                data, sr = sf.read(file_path)
                print(f"{filename} is not corrupted")
            except Exception as e:
                print(f"{filename} is corrupted: {e}")

#check_wav_files_corrupted("/mnt/ricproject4/commercial_product/data/cv-corpus/cv-corpus-12.0-2022-12-07/ta/converted_train_set")
'''
This code checks if the paths mentioned in the second column of a text file exist or not, and also updates the paths to include a specific base directory. 
The os.path.join function is used to combine the base directory with the path in the second column to form the full path to the file.
The os.path.exists function is then used to check if the file at the full path exists. If the file exists, 
a message indicating that the path exists is printed, and if the file does not exist, a message indicating that the path does not exist is printed.

'''
def check_paths_in_file(file):
    with open(file, "r") as f:
        for line in f:
            columns = line.strip().split(" ")
            path = columns[1]
            file_path = os.path.join("/mnt/ricproject4/commercial_product/data/cv-corpus/cv-corpus-12.0-2022-12-07/ta/seperated_converted_train_set_II/",path)
            if os.path.exists(file_path):
                print(f"{path} exists")
            else:
                print(f"{path} does not exist")
                
#check_paths_in_file("/mnt/ricproject4/commercial_product/data/cv-corpus/cv-corpus-12.0-2022-12-07/ta/train_CV_Tamil.txt")

'''
This function reads each line of the original text file and uses the os.path.exists function to check if the path in the second column exists.
If the path not exists, the line is added to a list of non_existent_paths.
After all the lines have been processed, new text file is written with the non_existent_paths that contain only the paths that non exist.
'''

def check_paths_in_file_II(file):
    non_existent_paths = []
    with open(file, "r") as f:
        for line in f:
            columns = line.strip().split(" ")
            path = columns[1]
            file_path = os.path.join("/mnt/ricproject4/commercial_product/data/cv-corpus/cv-corpus-12.0-2022-12-07/ta/seperated_converted_train_set_II/",path)
            if not os.path.exists(file_path):
                non_existent_paths.append(line)

    if non_existent_paths:
        with open("non_existent_paths.txt", "w") as f:
            for line in non_existent_paths:
                f.write(f"{line}\n")
        print(f"A list of non-existent paths has been saved to non_existent_paths.txt")
    else:
        print("All paths exist")

#check_paths_in_file_II("/mnt/ricproject4/commercial_product/data/cv-corpus/cv-corpus-12.0-2022-12-07/ta/train_CV_Tamil.txt")
'''
This function reads each line of the original text file and uses the os.path.exists function to check if the path in the second column exists.
If the path exists, the line is added to a list of new lines.
After all the lines have been processed, the original text file is overwritten with the new lines that contain only the paths that exist.
'''

def remove_non_existent_paths(file):
    new_lines = []
    with open(file, "r") as f:
        for line in f:
            columns = line.strip().split(" ")
            path = columns[1]
            file_path = os.path.join("/mnt/ricproject4/commercial_product/data/cv-corpus/cv-corpus-12.0-2022-12-07/ta/seperated_converted_train_set_II/",path)
            if os.path.exists(file_path):
                new_lines.append(line)

    with open(file, "w") as f:
        for line in new_lines:
            f.write(line)

remove_non_existent_paths("/mnt/ricproject4/commercial_product/data/cv-corpus/cv-corpus-12.0-2022-12-07/ta/train_CV_Tamil.txt")
