import os
import json

def read_file(file_path):
    """Read a file and return its contents."""
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    """Write content to a file."""
    with open(file_path, 'w') as file:
        file.write(content)

def load_json(file_path):
    """Load a JSON file and return its contents."""
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(file_path, data):
    """Save data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def list_files(directory):
    """List all files in a directory."""
    return os.listdir(directory)