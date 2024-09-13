import gdown
import os
import zipfile

def download_and_extract_with_gdown(gdrive_link, folder_name, download_path, extract_path):
    zip_path = os.path.join(download_path, folder_name + '.zip').replace("\\","/")

    # Check if the folder is already extracted
    if os.path.exists(extract_path):
        print(f"Folder '{folder_name}' already exists, skipping download.")
        return

    # If the zip file exists, check if it's a valid zip file
    if os.path.exists(zip_path):
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.testzip()  # Test if it's a valid zip
            print(f"Zip file '{folder_name}.zip' already exists and is valid.")
        except zipfile.BadZipFile:
            print(f"Zip file '{folder_name}.zip' is invalid or corrupted, redownloading...")
            os.remove(zip_path)
            gdown.download(gdrive_link, zip_path, quiet=False)
    else:
        print(f"Downloading '{folder_name}' from Google Drive...")
        gdown.download(gdrive_link, zip_path, quiet=False)
        print(f"Downloaded '{folder_name}.zip' to {zip_path}")

    # Extract the zip file
    print(f"Extracting '{folder_name}.zip'...")
    print(zip_path)
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
