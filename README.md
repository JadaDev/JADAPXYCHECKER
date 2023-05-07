![Alt text](https://github.com/JadaDev/JADAPXYCHECKER/blob/main/JADAPXY.png)


# Jada Proxy Checker

Jada Proxy Checker is a tool to check HTTP and HTTPS proxies from a given list of proxies. The tool uses multiple threads to check the proxies and prints the results in the terminal. It also writes the working proxies to a file named `proxy.txt`.

## Installation

To install the required packages for the tool, run the following command:

>python setup.py


If the installation encounters any errors, it will prompt you to try an alternative installation method.

## Usage

To use the tool, run the following command:

>python jadapxcheck.py


When prompted, enter the URL of the proxy list you wish to check. The tool will then check the proxies and display the results in the terminal. Working proxies will also be written to a file named `proxy.txt`.

## Requirements

The tool requires the following packages to be installed:

- requests
- threading
- termcolor
- time
- os

These packages can be installed by running the following command:

>pip install -r requirements.txt

