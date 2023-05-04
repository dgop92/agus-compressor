import filecmp


def compare_files(file_path1: str, file_path2: str) -> bool:
    """Compare two files and return True if they are the same, False otherwise."""
    return filecmp.cmp(file_path1, file_path2)
