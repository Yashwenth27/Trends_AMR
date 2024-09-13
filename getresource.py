import gdown
import os
import zipfile

def download_and_extract_with_gdown(gdrive_link, folder_name, download_path, extract_path):
    zip_path = "Final Data-20240913T063708Z-001.zip"
    print(f"Extracting '{folder_name}.zip'...")
    print("")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    print(f"Extracted to '{extract_path}'")

# Main usage
if __name__ == "__main__":
    gdrive_link = "https://drive.google.com/uc?id=your_file_id"  # Replace with the actual file ID
    folder_name = "resource"
    download_path = "./downloads"  # Path to store the zip file
    extract_path = "./extracted_folder"  # Path to extract the folder

    # Ensure the download path exists
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Download and extract folder
    download_and_extract_with_gdown(gdrive_link, folder_name, download_path, extract_path)
