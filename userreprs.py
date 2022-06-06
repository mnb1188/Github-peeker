class User():
    """A class used to represent a single Github user

    Attributes:
        login (str): User's login on Github
        name (str): User's real name
        bio (str): User's bio on Github

    Methods:
        get_login() : Returns user's login
        get_name() : Returns user's name
        get_bio() : Returns user's bio
    """
    def __init__(self, login : str, name : str, bio : str) -> None:
        """
        Patameters:
            login (str) : User's login on Github
            name (str) : User's name on Github
            bio (str) : User's bio on Github
        """
        self.__login = login
        self.__name = name
        self.__bio = bio

    def get_login(self) -> str:
        """Returns user's login

    Args: None

    Returns:
        login (str): User's Github username
        """
        return self.__login

    def get_name(self) -> str:
        """Returns user's real name
    
    Args: None

    Returns:
        name (str): User's real name
        """
        return self.__name

    def get_bio(self) -> str:
        """Returns user's Github bio

    Args: None

    Returns:
        bio (str): User's Github bio
        """
        return self.__bio
