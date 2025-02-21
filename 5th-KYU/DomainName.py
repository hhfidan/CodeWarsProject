def domain_name(url):
    """
    Extracts the domain name from a given URL.
    
    Parameters:
        url (str): The URL from which to extract the domain.
    
    Returns:
        str: The extracted domain name.
    """
    # Remove protocol (http, https) and 'www' if present
    url = url.replace("http://", "").replace("https://", "").replace("www.", "")
    
    # Split by '.' and return the first part (domain name)
    return url.split(".")[0]
