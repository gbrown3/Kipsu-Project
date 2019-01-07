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

## Design Decisions

The first, and most important decision I made about the design of this project was which languages and frameworks to use. Swapping between different names and guests and companies seemed like it could be a painful process if not run through a GUI, and since HTML already has some prefabrications to create simple UI elements, I thought it would be best to use a web language. However, I'm not particularly fond of or comfortable with Javascript's interpretation of object oriented programming, so I wanted to use another language if I could. As it so happens, for one of my most recent projects I wrote the backend using Flask and Python, and I much prefer object oriented programming in Python. Thus, I decided to use a combination of HTML, Javascript, and Python to write my project, with most of the data processing happening on the server side in Python, and just enough Javascript to pass information between the client and server and update the page. 

## Testing Process

## Future Work
