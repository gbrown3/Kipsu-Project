# Message-Project
Gabriel Brown

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

That's it! Remember to always activate your virtual environment with `. ./venv/bin/activate` in the `Message-Project` directory before you start the server.

## How to start the server and access the website

In the `Message-Project` directory, with the virtual environment activated, run the following command:
```
python server.py
```

This will start up a local Flask server. The terminal will then list a url you can go to using any browser, most likely `http://127.0.0.1:5000/`. You should be able to access the message generation system at that url. 

## Design Decisions

The first, and most important decision I made about the design of this project was which languages and frameworks to use. Swapping between different names and guests and companies seemed like it could be a painful process if not run through a GUI, and since HTML already has some prefabrications to create simple UI elements, I thought it would be best to use a web language. However, I'm not particularly fond of or comfortable with Javascript's interpretation of object oriented programming, so I wanted to use another language if I could. As it so happens, for one of my most recent projects I wrote the backend using Flask and Python, and I much prefer object oriented programming in Python. Thus, I decided to use a combination of HTML, Javascript, and Python to write my project, with most of the data processing happening on the server side in Python, and just enough Javascript to pass information between the client and server and update the page. 

I decided to make classes for messages, guests, companies and reservations, because they were already clearly distinct parts in the JSON files provided. I also decided to make a template class seperate from the message class, as I wanted to make it easy to store more information about each template in the future (a nickname, for instance). 

I spent a long time trying to decide how best to store templates in JSON files, and ultimately I decided that a list of "parts" would be the most appropriate. By storing message template as a list of strings, with the variable keywords as individual entries, I could preserve the order of the sentence and keep the variable parts distinct without having to do any fancy (and expensive) string computations. 

## Testing Process

Unfortunately, I didn't have time to write proper unit tests, so I tested as carefully as possible by thinking of as many edge cases as I could and what the expected output should be, then running those tests through my program. I believe that Flask accounts for a lot of security concerns like sanitizing user input, so I didn't put as much focus on testing the security of this project.

## Future Work

As with any project, there are plenty of features I wish I could have worked on, but didn't have time to. One of the first things I would implement with more time is to have the greeting variable change based on the client-side timezone, and not just be based on the server's timezone. I would also like to make the GUI look a lot nicer, and rework it with good web design principles in mind.
