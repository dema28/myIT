from function import user
def get_file_size(function):
    def wrapper(file_path):
        if not file_path.endswith(".txt"):
            return "Error: File should be a text file."
        try:
            size = function(file_path)
            return f"File size: {size} bytes"
        except FileNotFoundError:
            return "Error: File not found."
    return wrapper
