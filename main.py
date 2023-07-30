import argparse
from qemu_parser import QemuParser
from terraform_converter import TerraformConverter
from file_writer import FileWriter

def main():
    parser = argparse.ArgumentParser(description='Convert Proxmox QEMU configuration files to Terraform YAML files')
    parser.add_argument('input_file', help='Path to the input QEMU configuration file')
    parser.add_argument('output_file', help='Path to the output Terraform YAML file')
    args = parser.parse_args()

    # Parse the QEMU configuration file
    qemu_parser = QemuParser()
    qemu_config = qemu_parser.parse_file(args.input_file)

    # Convert the QEMU configuration to Terraform YAML
    terraform_converter = TerraformConverter()
    terraform_yaml = terraform_converter.convert(qemu_config)

    # Write the Terraform YAML to the output file
    file_writer = FileWriter()
    file_writer.write_file(args.output_file, terraform_yaml)

if __name__ == '__main__':
    main()
