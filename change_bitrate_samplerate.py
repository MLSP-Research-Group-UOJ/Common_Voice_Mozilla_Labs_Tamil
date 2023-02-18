## Example usage of the function
#source_dir = '/mnt/ricproject4/commercial_product/data/cv-corpus/cv-corpus-12.0-2022-12-07/ta/clips/'
#dest_dir = "/mnt/ricproject4/commercial_product/data/cv-corpus/cv-corpus-12.0-2022-12-07/ta/converted_train_set/"
#bitrate = 256
#sample_rate = 16000
#num_workers = 8
#convert_directory(source_dir, dest_dir, bitrate, sample_rate, num_workers)

#import os
#import subprocess
#from tqdm import tqdm
#
#def convert_wave_files(src_folder, dst_folder, sample_rate, bit_rate):
#     #Create the destination folder if it doesn't exist
#    if not os.path.exists(dst_folder):
#        os.makedirs(dst_folder)
#
#     #Get the list of wave files in the source folder
#    files      = [f for f in os.listdir(src_folder) if f.endswith(".wav")]
#    
#     #Get the count of wave files in the source folder
#    total = len(files)
#    
#     #Convert each wave file to the specified sample rate and bitrate
#    for i, file in enumerate(tqdm(files, desc='Converting Files', total=total, unit='files')):
#        src_path = os.path.join(src_folder, file)
#        dst_path = os.path.join(dst_folder, file)
#        subprocess.run(['ffmpeg', '-i', src_path, '-ar', str(sample_rate), '-b:a', str(bit_rate) + 'k', dst_path], check=True)
#
#
# #Example usage
#src_folder = '/mnt/ricproject4/commercial_product/data/cv-corpus/cv-corpus-12.0-2022-12-07/ta/clips/'
#dst_folder = "/mnt/ricproject4/commercial_product/data/cv-corpus/cv-corpus-12.0-2022-12-07/ta/converted_train_set/"
#convert_wave_files(src_folder, dst_folder, 16000, 256)

###############################################################################################################################
import concurrent.futures
import subprocess
import os
from tqdm import tqdm

def convert_wave_files(source_dir, destination_dir, sample_rate, bit_rate):
    # Get the list of all wave files in the source directory and its subdirectories
    wave_files = []
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".wav"):
                wave_files.append(os.path.join(root, file))

    # Create a progress bar to track the progress of the wave file conversion
    progress_bar = tqdm(total=len(wave_files), desc="Converting wave files")

    # Create a ThreadPoolExecutor with the specified number of workers
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        # For each wave file, submit a task to convert it to the desired sample rate and bit rate
        for wave_file in wave_files:
            # Get the relative path of the wave file from the source directory
            relative_path = os.path.relpath(wave_file, source_dir)
            # Get the destination directory for the wave file
            dest_dir = os.path.join(destination_dir, os.path.dirname(relative_path))
            # Create the destination directory if it doesn't already exist
            os.makedirs(dest_dir, exist_ok=True)
            # Get the destination path for the wave file
            dest_path = os.path.join(dest_dir, os.path.basename(wave_file))
            # Submit the task to convert the wave file
            executor.submit(convert_wave_file, wave_file, dest_path, sample_rate, bit_rate, progress_bar)

def convert_wave_file(wave_file, dest_path, sample_rate, bit_rate, progress_bar):
    # Call ffmpeg to convert the wave file to the desired sample rate and bit rate
    subprocess.run(["ffmpeg", "-i", wave_file, "-ar", str(sample_rate), "-b:a", str(bit_rate) + "k", dest_path])
    # Update the progress bar after the wave file has been converted
    progress_bar.update(1)


# Example usage
src_folder = '/mnt/ricproject4/commercial_product/data/cv-corpus/cv-corpus-12.0-2022-12-07/ta/clips/'
dst_folder = "/mnt/ricproject4/commercial_product/data/cv-corpus/cv-corpus-12.0-2022-12-07/ta/converted_train_set/"
#num_workers = 2
convert_wave_files(src_folder, dst_folder, 16000, 256)
