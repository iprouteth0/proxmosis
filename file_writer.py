class FileWriter:
    def write_file(self, file_path, content):
        """
        Write the content to the specified file.
        """
        with open(file_path, 'w') as file:
            file.write(content)
