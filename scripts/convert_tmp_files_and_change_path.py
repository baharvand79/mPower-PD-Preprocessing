import os
import shutil

# Define the source and destination directories
source_dir = "data(.synapseCache)"
destination_dir = "data"

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

counter = 0
success_counter = 0
failed_counter = 0
failed = []
for i in range(0, 1000):
    folder_to_process = str(i) # Convert the number to a string
    source_subfolder_path = os.path.join(source_dir, folder_to_process)
    # Check if the folder exists before processing
    if os.path.isdir(source_subfolder_path):
        # Recursively walk through all subdirectories in the current folder
        for root, dirs, files in os.walk(source_subfolder_path):
            for file in files:
                # Check for files with the specific naming convention
                if file.startswith("audio_audio.m4a") and file.endswith(".tmp"):
                    source_file_path = os.path.join(root, file)
                    
                    # Extract the name of the immediate subdirectory
                    subfolder_name = os.path.basename(root)
                    
                    # Define the new filename (e.g., "1.wav")
                    new_filename = f"{subfolder_name}.wav"
                    
                    # Construct the full path for the destination file
                    destination_file_path = os.path.join(destination_dir, new_filename)
                    counter = counter + 1
                    # print ("File: ", counter)
                    try:
                        shutil.copy2(source_file_path, destination_file_path)
                        # print(f"Success: Copied and renamed '{file}' to '{destination_file_path}'")
                        success_counter = success_counter + 1
                    except Exception as e:
                        print(f"Error: Could not copy '{source_file_path}'. Reason: {e}")
                        failed.appened(subfolder_name)
                        failed_counter = failed_counter + 1
    else:
        print(f"Folder '{source_subfolder_path}' does not exist. Skipping.")

    print("Folder: ", i)

print("Copied: ", success_counter, ", Failed: ", failed_counter)