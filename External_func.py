from typing import Dict
from urllib import response
from dotenv import load_dotenv
import requests as r
import json
import os
from reporeprs import *
from userreprs import *


def GetRepoData(username : str, repo_name : str) -> object:
    """Gets repo data through http get request

    Args:
        username (str): Login of a user whose repos' data we want to gather
        repo_name (str): Name of a repo we want to query github api about

    Returns:
        langs_repr (object): An object of LanguagesRepr class, which holds information about languages user used in this particular repo
    """
    load_dotenv()
    oauth_token = os.getenv("OAUTH_TOKEN")
    response = r.get(f"https://api.github.com/repos/{username}/{repo_name}/languages", headers={'Authorization': f'token {oauth_token}'})
    Data = json.loads(response.text)
    langs_repr = LanguagesRepr()
    for lang, bytes in Data.items():
        slang_repr = SingleLangRepr(lang, bytes)
        langs_repr.add_languages(slang_repr)
    return langs_repr

def GetAllRepos(username : str) -> object:
    """Gets a list of all of user's public repos

    Args:
        username (str): Login of a user whose repos we want to get

    Returns:
        repo_list (object): An object of RepoListRepr class, which holds all information about user's repositories
    """
    load_dotenv()
    oauth_token = os.getenv("OAUTH_TOKEN")
    repo_list = RepoListRepr()
    response = r.get(f"https://api.github.com/users/{username}/repos", headers={'Authorization': f'token {oauth_token}'})
    for item in response.json():
        repo_repr = RepoRepr(item['name'], GetRepoData(username, item['name']))
        repo_list.add_repo(repo_repr)
    
    return repo_list

def GetUserData(username : str) -> object:
    """Get user's login, real name and bio from Github profile

    Args:
        username (str): Login of a user whose data we want to gather

    Returns:
        user (object): An object of User class, which contains user's login, real name and bio
    """
    load_dotenv()
    oauth_token = os.getenv("OAUTH_TOKEN")
    response = r.get(f"https://api.github.com/users/{username}", headers={'Authorization': f'token {oauth_token}'})
    response = json.loads(response.text)
    user = User(response.get('login'), response.get('name'), response.get('bio'))
    
    return user

def GetRawRepoData(username : str, repo_name :str) -> Dict:
    """Serves JSON file containing user's repo data

    Args:
        username (str): Login of a user whose data we want to gather
        repo_name (str): Name of a repo we want to query github api about

    Returns:
        Data (Dict) : Dictionary containing all of singular repo data
    """
    load_dotenv()
    oauth_token = os.getenv("OAUTH_TOKEN")
    response = r.get(f"https://api.github.com/repos/{username}/{repo_name}/languages", headers={'Authorization': f'token {oauth_token}'})
    Data = json.loads(response.text)
    return Data
 
def GetRawRepos(username : str) -> Dict:
    """Serves JSON file containing data about all of user's repositories

    Args:
        username (str): Login of a user whose data we want to gather

    Returns:
        repo_dict: Dictionary containing information about all of user's public repositories
    """
    load_dotenv()
    oauth_token = os.getenv("OAUTH_TOKEN")
    repo_dict = {}
    response = r.get(f"https://api.github.com/users/{username}/repos", headers={'Authorization': f'token {oauth_token}'})
    if len(response.json()) == 2:
        return repo_dict
    for item in response.json():
        repo_dict.update({item['name'] : GetRawRepoData(username, item['name'])})
    return repo_dict

def AggregateLanguages(repo_list : object) -> Dict:
    """Add number of bytes written in each language in every known repository

    Args:
        repo_list (object): Object of RepoListRepr class, containing data about all of known user repos

    Returns:
        lang_dict (Dict): Dictionary containing information about number of bytes written in every language used by a user
    """
    lang_dict = {}
    for repo in repo_list.get_repos():
        for langs in repo.get_langs().get_languages():
            name = langs.get_name()
            if name in lang_dict:
                lang_dict[name] += langs.get_n_bytes()
            else:
                lang_dict[name] = langs.get_n_bytes()

    return lang_dict
