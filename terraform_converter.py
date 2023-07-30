class TerraformConverter:
    def convert(self, qemu_config):
        """
        Convert the QEMU configuration to Terraform YAML format.
        """
        terraform_yaml = ''
        for key, value in qemu_config.items():
            terraform_yaml += f'{key}: {value}\n'
        return terraform_yaml
