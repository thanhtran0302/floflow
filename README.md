# Flowflow (built with Instapy)

**Disclaimer:** Python 3 is used for this project.

This bot can only follow accounts for now. If you guys want more feature. Please, feel free to contribute, or make a request :) 

## How to start
First of all, we recommended to use [virtualenv](https://pypi.org/project/virtualenv/1.7.1.2/#:~:text=You%20can%20install%20virtualenv%20with,it%20with%20python%20virtualenv.py.) to separate your machine python environment vs your `project` python environment.

To do that, you should do:
```bash
$> virtualenv .
$> source ./bin/activate
```

Once your virtual environment is set up. Install dependencies:
```bash
 $> pip3 install -r requirements.txt
```

## Add accounts file.

Create a new file called `accounts.json`. Inside of this json, each key is an account information.

Example:
```json
{
  "account_1": {
    "username": "account_1",
    "password": "your_password"
  },
  "account_2": {
    "username": "account_2",
    "password": "your_password"
  }
}
```

## Launch FloFlow

```bash
$> python3 main.py account_1 #should match accounts.json key
```
