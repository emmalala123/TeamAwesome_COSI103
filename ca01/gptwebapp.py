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

app = Flask(__name__, static_url_path='/static')
gptAPI = GPT(os.environ.get("APIKEY"))

# Set the secret key to some random bytes. Keep this really secret!


@app.route('/')
def index():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1><a href="/">GPT Prompt Engineering</a></h1>
        <h2>Team 42: Emma Barash, Nina Zhang, James Wang, William Messenger</h2>
        <h3>Menu:</h3>
        <ul>
            <li><a href="/about">About</a></li>
            <li><a href="/ourTeam">Our Team</a> </li>
            <li><a href="/ninaPage">Ask GPT to proofread your code</a> </li>
            <li><a href="/getResponseJames">Ask GPT to write a poetry</a></li>
            <li><a href="/willsPage">Ask GPT to generate code for a game</a></li>
            <li><a href="/emmaPage"> Ask GPT to generate a CSS file with chosen color theme</a></li>
        </ul>

    '''

@app.route('/ourTeam')
def ourTeam():
    ''' display our team members '''
    print('processing /ourTeam route')
    return f'''
        <h1><a href="/">GPT Prompt Engineering</a></h1>
        <h2>Our Team</h2>
        <h3>Emma Barash</h3>
        <ul>
            <li>Graduation Year: 2023</li>
            <li>Major: BS/MS Neuroscience, BA Computer Science</li>
            <li>Role: Created <a href="/emmaPage">CSS color-theme generator</a></li>
        </ul>
        <h3>Nina Zhang</h3>
        <ul>
            <li>Graduation Year: 2024 </li>
            <li>Major: Computer Science, Biology </li>
            <li>Role: Created <a href="/ninaPage">python checker</a> from prompt</li> 
        </ul>
        <h3>James Wang</h3>
        <ul>
            <li>Graduation Year: 2025 </li>
            <li>Major: Business, Computer Science</li>
            <li>Role: Created <a href="/getResponseJames">Ask GPT to write a poetry</a></li>
        </ul>
        <h3>William Messenger</h3>
        <ul>
            <li>Graduation Year: 2025</li>
            <li>Major: Business, Computer Science, Economics (minor)</li>
            <li>Role: Created <a href="/willsPage">python game</a> prompt</li>
        </ul>
    '''

@app.route('/about')
def about():
    ''' display a link to the general query page '''
    print('processing /about route')
    return f'''
        <h1><a href="/">GPT Prompt Engineering</a></h1>
        <h2>GPT App Team 42</h2>
        This is the GPT app for Team 42, which uses GPT3 to solve issues based on the preset prompts, and generate responses.<br>
        Click <a href="https://github.com/emmalala123/TeamAwesome_COSI103/tree/2103969f715eea0d3519b1804938e662735ae770">here</a> to view our repository for reference. 
    '''

# create a CSS file based on a color scheme of the user's choice
@app.route('/emmaPage', methods=['GET', 'POST'])
def emmaPage():
    ''' display a link to the general query page '''
    css_url = url_for('static', filename='styles.css')
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getresponseEmma(prompt)
        return f'''
            <link rel="stylesheet" type="text/css" href="{css_url}">
            <h1><a href="/">GPT Prompt Engineering</a></h1>
            <h2> Generate Cascading Style Sheet (CSS)</h2>
            <pre>{prompt}</pre>
            <hr>
            <p class="answer">Here is the answer in text mode:</p>
            <div class="answer-div">{answer}</div>
            <p class="answer">Here is the answer in "pre" mode:</p>
            <pre class="answer-pre">{answer}</pre>
            <a href="/emmaPage"> make another query</a>
            '''
    else:
        return f'''
            <link rel="stylesheet" type="text/css" href="{css_url}">
            <h1><a href="/">GPT Prompt Engineering</a></h1>
            <h2> Generate Cascading Style Sheet (CSS)</h2>
          Please choose a color theme, and GPT will generate a .css file for you
        <form method="post" class="my-form">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response" class="btn-primary">
        </form>
        '''
    
'''create a poem based on the topic of the user's choice'''
@app.route('/getResponseJames', methods=['GET', 'POST'])
def getResponseJames():
   
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponseJames(prompt)
        return f'''
        <h1><a href="/">GPT Prompt Engineering</a></h1>
        <h2>Generate Poetry</h2>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href="/getResponseJames"> make another query</a>
        '''
    else:
        return '''
        <h1><a href="/">GPT Prompt Engineering</a></h1>
        <h2>Generate Poetry</h2>
        Enter the topic of your choice below, and GPT would generate a poem for you
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
    
'''proofreads code of the user's choice'''
@app.route('/ninaPage', methods=['GET', 'POST'])
def ninaPage(): 
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponseNina(prompt)
        return f'''
        <h1><a href="/">GPT Prompt Engineering</a></h1>
        <h2>Proofread Input Code</h2>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href="/ninaPage"> make another query</a>
        '''
    else:
        return '''
        <h1><a href="/">GPT Prompt Engineering</a></h1>
        <h2>Proofread Input Code</h2>
        Input the code you want to check and proofread, and GPT will check the code for errors.
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

'''create a python game based on the user's choice'''
@app.route('/willsPage', methods=['GET', 'POST'])
def willsPage():
   
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponseWill(prompt)
        return f'''
        <h1><a href="/">GPT Prompt Engineering</a></h1>
        <h2>Generate Python Game</h2>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href="/willsPage"> make another game</a>
        '''
    else:
        return '''
        <h1><a href="/">GPT Prompt Engineering</a></h1>
        <h2>Generate Python Game</h2>
        Type the name of a simple game, and GPT will generate the python code for it:
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
    
if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)
    





