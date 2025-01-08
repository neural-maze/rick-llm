import os
from huggingface_hub import hf_hub_download


def download_model(repo_id, filename, dest_folder="ollama_files"):
    """
    Download a model file from Hugging Face Hub.

    Args:
        repo_id (str): The Hugging Face repository ID (e.g., "theneuralmaze/RickLLama-3.1-8B")
        filename (str): The name of the file to download
        dest_folder (str): The destination folder
    """
    os.makedirs(dest_folder, exist_ok=True)

    try:
        downloaded_path = hf_hub_download(
            repo_id=repo_id,
            filename=filename,
            local_dir=dest_folder,
            local_dir_use_symlinks=False,
        )
        print(f"Successfully downloaded {filename} to {downloaded_path}")
    except Exception as e:
        print(f"Error downloading model: {e}")


if __name__ == "__main__":
    # Based on the repository shown in the finetune.py file
    repo_id = "theneuralmaze/RickLLama-3.1-8B"

    # Download the GGUF model file
    download_model(repo_id, "unsloth.Q8_0.gguf")
