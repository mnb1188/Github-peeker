from app import app
from flask import render_template, url_for, request, redirect
from External_func import *

@app.route('/', methods = ['POST', 'GET'])
def hello():
    """Route for index page

    Args: None

    Returns: 
        str: An index page for the API's website
    """
    if request.method == 'POST':
        username = request.form['login']
        try:
            return redirect(url_for('userinfo', username = username))
        except:
            return "No such user was found, please try another username"
    else:
        return render_template('hello.html')

@app.route('/userinfo/<username>.html')
def userinfo(username : str) -> str:
    """Route for a web page dedicated to displaying found user info.

    Args:
        username (str) : Username of user whose Github information we want to acquire

    Returns:
        str: A webpage displaing all found data
    """
    user_data = GetUserData(username)
    if user_data.get_login() == None:
        return redirect('/notfound.html')
    repos_list = GetAllRepos(username)
    lang_stats = AggregateLanguages(repos_list)
    return render_template('user_info.html', user = user_data, repos_list = repos_list, lang_stats=lang_stats)

@app.route('/notfound.html')
def notfound() -> str:
    """Route for a web page handling usernotfound error

    Args: None

    Returns: 
        str: A web page informing client that user was not found 
    """
    return render_template('notfound.html')

@app.route('/api.get.user/<username>')
def api_get_user(username : str) -> Dict:
    """Route designated to serve user info as a json file

    Args:
        username (str): Login of a user whose info we want to acquire

    Returns:
        Dict: Json file containing all necessary information or an error message
    """
    user_data = GetUserData(username)
    if user_data.get_login() == None:
        return {
            "Error" : "No such user exists. Please try again"
        }
    lang_stats = AggregateLanguages(GetAllRepos(username))
    return {
        "login" : user_data.get_login(),
        "real name" : user_data.get_name(),
        "bio" : user_data.get_bio(),
        "used languages" : lang_stats
    }

@app.route('/api.get.repos/<username>')
def api_get_repos(username : str) -> str:
    """Route designed to serve repo information for stated github user

    Args:
        username (str): Login of a user whose info we want to acquire

    Returns:
        Dict: Json file containing all necessary information or an error message 
    """
    repos_list = GetRawRepos(username)
    if len(repos_list) == 0:
        return {
            "No repos error" : "No public repos were found for this user. Please try again"
        }
    return repos_list
