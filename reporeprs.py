from tokenize import Double
from typing import List


class RepoListRepr():
    """A class used to represent all of repos instances

    Attributes:
        repos (List): A list containing objects representing known Github repos of a queried user

    Methods:
        get_repos() : Returns a list containing objects representing all added repos
        add_repo(repo : object) : Add new RepoRepr class object to the list
"""

    def __init__(self) -> None:
        """
        Parameters: None
        """
        self.__repos = []

    def get_repos(self) -> List[object]:
        """Returns a list containing objects representing all added repos

        Args: None

        Returns:
            repos (List[object]): A list containing objects of RepoRepr class representing known Github repos of a queried user
        """
        return self.__repos

    def add_repo(self, repo : object) -> None:
        """Appends new repo object of RepoRepr class to the list

        Args:
            repo (object): Object of RepoRepr class representing an existing Github repository

        Returns: None
        """
        self.__repos.append(repo)


class RepoRepr():
    """A class representing single repository

    Attributes:
        name (str): Name of the repository
        langs (object): Object of LanguagesRepr class representing programming languages used in this repo

    Methods:
        get_name() : Returns repo's name
        get_langs() : Returns object of LanguagesRepr class representing programming languages used in this repo
        set_name(name : str) : Sets repositories name
        add_langs(langs: object) : Adds an object of LanguagesRepr class representing programming languages used in this repo
    """

    def __init__(self, name : str, langs : object) -> None:
        """
        Parameters:
            name (str) : Repo's name
            langs (object) : Object of LanguagesRepr class representing programming languages used in this repo
        """
        self.__name = name
        self.__langs = langs

    def get_name(self) -> str:
        """Returns repo's name

        Args: None

        Returns:
            name (str): Repo's name
        """
        return self.__name

    def get_langs(self) -> object:
        """Returns object of LanguagesRepr class representing programming languages used in this repo

        Args: None

        Returns:
            langs (object): Object of LanguagesRepr class representing programming languages used in this repo
        """
        return self.__langs

    def set_name(self, name : str) -> None:
        """Sets repositories name

        Args:
            name (str): A new name to be set for the repository

        Returns: None
        """
        self.__name = name

    def add_langs(self, langs : object) -> None:
        """Adds an object of LanguagesRepr class representing programming languages used in this repo

        Args:
            langs (object): Object of LanuagesRepr class which will represent programming languages used in this repo

        Returns: None
        """
        self.__langs = langs


class LanguagesRepr():
    """A class which represents languages and their number of bytes

    Attributes:
        languages (List[object]): List containing objects of SingleLangRepr class

    Methods:
        get_languages(): Returns list containing objects of SingleLangRepr class
        add_languages(): Appends object of SingleLangRepr class to the languages list
    """

    def __init__(self) -> None:
        """
        Parameters:
            languages (List[object]): List containing objects of SingleLangRepr class
        """
        self.__languages = []

    def get_languages(self) -> List[object]:
        """Returns list containing objects of SingleLangRepr class

        Args: None

        Returns:
            languages (List[object]): List containing objects of SingleLangRepr class
        """
        return self.__languages

    def add_languages(self, lang : object):
        """Appends object of SingleLangRepr class to the languages list

        Args:
            lang (object): A single instance of SingleLangRepr object to be added to the list

        Returns: None
        """
        self.__languages.append(lang)
    


class SingleLangRepr():
    """A class representing a single language and a number of bytes written in it

    Attributes:
        name (str): A name of language to be described
        n_bytes (double): Number of bytes written in specified language

    Methods:
        get_name() : Returns name of language described in this class instance
        get_n_bytes() : Returns number of bytes written in language specified in this class instance
    """

    def __init__(self, name : str, n_bytes : Double) -> None:
        """
        Parameters:
            name (str): A name of language to be described
            n_bytes (double): Number of bytes written in specified language
        """
        self.name = name
        self.n_bytes = n_bytes

    def get_name(self) -> str :
        """Returns name of language described in this class instance

        Args: None

        Returns:
            name (str):  A name of language described in this class instance
        """
        return self.name

    def get_n_bytes(self) -> Double:
        """Number of bytes written in specified language

        Args: None

        Returns:
            n_bytes (double): Number of bytes written in specified language
        """
        return self.n_bytes
