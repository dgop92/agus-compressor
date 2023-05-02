def compare_files(file_path1: str, file_path2: str) -> bool:
    """
    Compare two text files to determine if they are the same.

    Args:
        file_path1 (str): The path of the first text file.
        file_path2 (str): The path of the second text file.

    Returns:
        bool: True if the files are the same, False otherwise.
    """
    with open(file_path1, "r") as file1, open(file_path2, "r") as file2:
        for line1, line2 in zip(file1, file2):
            if line1 != line2:
                return False
    return True
