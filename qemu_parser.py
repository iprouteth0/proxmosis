class QemuParser:
    def parse_file(self, file_path):
        """
        Parse the QEMU configuration file and return the configuration as a dictionary.
        """
        qemu_config = {}
        with open(file_path, 'r') as file:
            for line in file:
                key, value = line.strip().split(': ', 1)
                qemu_config[key] = value
        return qemu_config
