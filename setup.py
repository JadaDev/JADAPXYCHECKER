import sys
import subprocess
required_packages = ['requests', 'termcolor']
pip_commands = ['pip', 'pip3']
pip_command = None
for command in pip_commands:
    if subprocess.call(['which', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0:
        pip_command = command
        break

if pip_command is None:
    print('Error: pip or pip3 is not installed.')
    sys.exit(1)
for package in required_packages:
    try:
        subprocess.check_call([pip_command, 'install', package])
    except subprocess.CalledProcessError:
        print(f'Error: failed to install {package} using {pip_command}. Trying alternative method.')
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        except subprocess.CalledProcessError:
            print(f'Error: failed to install {package} using alternative method.')
            choice = input(f'Do you want to try installing {package} manually? (y/n) ')
            if choice.lower() == 'y':
                print(f'Please install {package} using your preferred method.')
            else:
                print('Installation cancelled.')
                sys.exit(1)

print('All required packages have been successfully installed.')
