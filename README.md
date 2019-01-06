# Message-Project

## How to set up your environment
1. Clone this repository
```
cd yourDirectory
git clone https://github.com/gbrown3/Message-Project
cd Message-Project
```
2. Make sure you have the latest version of Python and pip installed, then set up your virtual environment
```
python3 -m venv venv
. ./venv/bin/activate
```
You should now see `(venv)` before each line of your command line prompt.  

3. With your virtual environment activated, install flask.
```
pip install flask
```

That's it! Remember to always activate your virtual environment with `. ./venv/bin/activate` in the `PiratePlunder` directory before you start the server.

## How to start the server and access the website

In the `Message-Project` directory, with the virtual environment activated, run the following command:
```
python server.py
```

This will start up a local Flask server. The terminal will then list a url you can go to using any browser, most likely `http://127.0.0.1:5000/`. You should be able to access the message generation system at that url. 
