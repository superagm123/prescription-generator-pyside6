from pathlib import Path 

def absolute_path(file: str) -> str:
    """Returns the absolute path of the given file path"""
    return Path(__file__).parent.absolute() / file