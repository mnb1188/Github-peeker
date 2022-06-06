<!-- ## Github-peeker-->
# Github peeker

## Basic description
The premise of the given task was to create a API app that would communicate with Github and return predetermined information about user and hers or his repositories.

## Initial assumptions
In the beginning it was assumed that a potential user would like to access app not only through CLI or some external app (i.e. Postman) requests but also through some visual medium. Therefore, a simple web page was created to serve this very purpose of easy visualization. That does not however mean that app is only reachable through that single medium, as there is also a set of API commands, which return JSON files.

## Installation
After pulling files from Github repository user needs to cd into it's local path
```
cd ~/{some_path}/Github-peeker/
```
Then it is needed to install required dependencies into virtual enviroment:
<br>
<br>
Using conda: 
```
conda create --name test_env
conda activate test_env
pip install -r requirements.txt
```
Using venv:
```
python -m venv $PATH
source venv/bin/activate
python -m pip install -r requirements.txt
```

## Running the app
After setting everything up we are ready to run the app. To do this it is only needed to run the app.py file:
```
python $PATH/app.py
```
This leads us to 2 basic ways to access data mentioned in the task.

## 1st way: Using a web browser of choice
While letting the app run we open a web browser of choice and enter the following address:
```
localhost:5000/
```
This should display the following page:
<p align="center">
          <img width="700" height="400" src="/resources/index.png">
</p>
To find a user it is needed to enter hers/his name into the searchbar and press find button:
<p2 align="center">
          <img width="700" height="250" src="/resources/search.png">
</p2>
This should redirect the user to the final web page containing all of required infromation:
<p3 align="center">
          <img width="1800" height="400" src="/resources/results.png">
</p3>
          
          
## 2nd way: Calling the app directly
The alternative to the aforementioned method is to directly call the app through console. First possible addres under which we can access needed data is
```
localhost:5000/api.get.user/<username>
```
Here is a mock output from curl command:
<p4 align="center">
          <br>
          <img width="600" height="200" src="/resources/api_output_user.png">
</p4>
<br>
<br>
The second possible command is:
```
localhost:5000/api.get.repos/<username>
```
Here is a mock output from curl command:
<p5 align="center">
          <br>
          <img width="500" height="175" src="/resources/api_output_repos.png">
</p5>



          
                                                                                                                
