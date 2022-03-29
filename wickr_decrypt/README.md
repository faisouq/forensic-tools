# Decrypt Wickr Me database
This application is made specifically for Wickr Me. The idea behind this is retrieving the Wickr Me database password. After it has been retrieved it can be fed as input to SQLcipher to decrypt the database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

What things you need and what to install and how to install them on your own machine

#### Software

* [Git](https://git-scm.com/)
* Python3 with pip 

### Installing

A step by step series of examples that tell you how to start using the application.

In your environment, firstly clone the repository, using HTTPS or SSH
```bash
# The following command is to clone the repository using HTTPS
git clone https://github.com/faisouq/wickr-decrypt.git

# The following comment is to clone the repository using SSH (recommended)
git clone git@github.com:faisouq/wickr-decrypt.git
```

When you succesfully cloned the repository, change the directory to the repository using: `cd wickr_decrypt/`, then you're in the right folder, install the necessary packages that's inside the requirements.txt file

```bash
python -m pip install -r requirements.txt
```

And now you can run the file by using the command:
```bash
 python .\wickr_decrypt.py
```

## Built With

* [Python](https://www.python.org/) - The programming language used