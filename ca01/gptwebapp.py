'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
from flask import request,redirect,url_for,Flask
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get("APIKEY"))

# Set the secret key to some random bytes. Keep this really secret!


@app.route('/')
def index():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1>GPT Demo</h1>
        <li><a href="/about">about</a></li>
        <a href="{url_for('gptdemo')}">Ask questions to GPT</a>
        <a href="{url_for('gptdemo')}">Ask questions to GPT</a> <br>
        <a href="{url_for('getResponseJames')}">Ask GPT to write a poetry </a> <br>
        <a href="{url_for('willsPage')}">Ask GPT to generate code for a game </a>
        <li><a href="/Emma"> Emma </a></li>

    '''

@app.route('/about')
def about():
    ''' display a link to the general query page '''
    print('processing /about route')
    return f'''
        <h1>GPT app Team 42</h1>
        this is the GPT app for team 42, which uses GPT3 to solve issues based on the preset prompts, and generate responses
        Here is our repository for reference: <a href="https://github.com/emmalala123/TeamAwesome_COSI103/tree/2103969f715eea0d3519b1804938e662735ae770">Team42</a>
    '''

@app.route('/Emma')
def about():
    ''' display a link to the general query page '''
    print('processing /about route')
    return f'''
        <h1> Emma </h1>
        Hello world!
    '''
   

@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemo')}> make another query</a>
        '''
    else:
        return '''
        <h1>GPT Demo App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
    
'''create a poem based on the topic of the user's choice'''
@app.route('/getResponseJames', methods=['GET', 'POST'])
def getResponseJames():
   
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponseJames(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptpoetry')}> make another query</a>
        '''
    else:
        return '''
        <h1>Generate Poetry</h1>
        Enter the topic of your choice below, and GPT would generate a poem for you
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
    
'''create a poem based on the topic of the user's choice'''
@app.route('/willsPage', methods=['GET', 'POST'])
def willsPage():
   
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponseWill(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('index')}> make another query</a>
        '''
    else:
        return '''
        <h1>Generate Poetry</h1>
        Type the name of a simple game, and GPT will generate the python code for it
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)
