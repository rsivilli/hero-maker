"""
Installation based heavily off atomatic1111's suggestions https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Developing-extensions
"""

import launch
import os
import pkg_resources
import sys

req_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")
models_dir = os.path.abspath('models/HeroMaker')

if not os.path.exists(models_dir):
    os.makedirs(models_dir)
    print(f"HeroMaker : You can put the model in {models_dir} directory")

print("Check HeroMaker requirements")
with open(req_file) as file:
    for package in file:
        try:
            python = sys.executable
            package = package.strip()

            if not launch.is_installed(package):
                print(f"Install {package}")
                launch.run_pip(f'install {package}', f"sd-webui-heromaker requirement: {package}")
            elif '==' in package:
                package_name, package_version = package.split('==')
                installed_version = pkg_resources.get_distribution(package_name).version
                if installed_version != package_version:
                    print(f"Install {package}")
                    launch.run_pip(f'install {package}', f"sd-webui-heromaker requirement: changing {package_name} version from {installed_version} to {package_version}")
                
        except Exception as e:
            print(e)
            print(f'Warning: Failed to install {package}, heromaker will not work.')            
            raise e
