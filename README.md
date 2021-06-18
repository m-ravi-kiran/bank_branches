# Sum numbers

Find Bank branch details.

## Description

A flask application which enables to find a bank using IFSC code or using other details like name, state, district, etc.

## Getting Started

### Dependencies

* python 3.9
* pip3

### Hosting Flask application on the localhost.
* In a new virtual environment, use requirements file to install all the dependencies.
```
pip3 install -r requirements.txt
```

* To install the ```application``` project as a package in the virtual environment run
```
pip3 install .
```

* Load the data from the csv file. This will create a sqlite3 database file with name ```bank_branches.db``` in the ```applications``` folder.
```
python scripts/copy_data.py
```

* Once the dependencies are installed, use the following command to start the Flask application on port 1121.
```
python run.py
```

### Calling the APIs after hosting the application.
* Once the application is hosted, you can visit ```localhost:1121``` to search bank details by IFSC or by name.
* Here is the postman collection link to view all the APIs that are being used with sample examples. https://www.getpostman.com/collections/7d4c2f9ac56cbe296c6d


