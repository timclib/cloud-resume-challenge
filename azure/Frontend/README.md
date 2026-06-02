## Installed Azure CLI and BICEP

https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?view=azure-cli-latest&pivots=apt

'''sh
curl -fsSL 'https://azurecliprod.blob.core.windows.net/$root/deb_install.sh' | sudo bash
'''

### Login to CLI

'''sh
az login
'''

### install Ansible

'''sh
pipx install --include-deps ansible
'''

### install Ansible deps

'''sh
cd azure
ansible-galaxy collection install -r requirements.txt
'''

'''sh
/usr/local/py-utils/venvs/ansible/bin/python -m pip install --upgrade "ansible[azure]"
'''