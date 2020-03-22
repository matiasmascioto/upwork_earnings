# Upwork Earnings

## Description
Resample Upwork *Transaction History* CSV file by predefined periods (*month*, *week*, ...) so it is easier to know the 
earnings in Upwork in each period.

## Directory structure
 * */data/*: Data files
	* */input/*: Input file
	* */output/*: Output files
 * */logs/*: Log files
 * */src/*: Python scripts
	* */helpers/*: Helper functions
	* *upwork_earnings.py*: Main script
	* *upwork_earnings.yml*: Configuration file
 
## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt
```

### Packages
* [pandas](https://pandas.pydata.org/)
* [PyYAML](https://pyyaml.org/)


## Usage
1. Copy the input file (*.csv file*) to */data/input/*
    - Download the *Transaction History* .csv file from *Reports -> Transaction History*
    - Filters values: *All transactions* and *All Clients*
2. Update the configuration file (*upwork_earnings.yml*):
	- *input/filepath_or_buffer*: input folder path
	- *periods*: data is sampled by the periods defined there
3. Run */src/upwork_earnings.py*
```bash
python upwork_earnings.py
```
4. Wait until the '*Script finished*' message
5. Ready! Results in */data/output/* (*.csv files*)

