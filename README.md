# Most Active Cookie
Most Active Cookie is a Python program to process a cookie log file and return the most active cookie for the specified day.

## Necessary Packages
Use the package manager [pip] to install PyInstaller and PyTest
Note: PyInstaller strictly used for generating a Python executable. One is already available in the repository. 

```bash
pip3 install pytest
pip3 install pyinstaller 
```
## Using PyInstaller to Generate an Executable

```bash
python3 -m PyInstaller most_active_cookie.py
```
When generating, make sure you put a CSV file in the executable directory.


## Running Test Cases

```bash
python3 -m pytest most_active_cookie_test.py
```

## Executing the code

### Using Executable
1. Navigate to dist/most_active_cookie in terminal
2. Execute the command 

```bash
./most_active_cookie cookie_log.csv -d 2018-12-09
```

### Using Python File 

```bash
python3 most_active_cookie.py cookie_log.csv -d 2018-12-09
```
