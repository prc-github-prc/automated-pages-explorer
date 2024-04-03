# Disclaimer: This script is for educational purposes only. 
# Do not use against any network, system or application that you don't own or have authorisation to test.

import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse,urljoin
from sys import argv


def verify_url(url:str) -> str:
    """
    This function take as argument an url to test as str, and return a message to know if the url
    is correct or not.
    """
    if type(url) != str:
        return ""

    try:
        test = requests.get(url) # we try to make a request
        if test.status_code == 404: 
            return "error" # if the site exists but not the page, we return an error
        else:
            return "ok" # if the page exists, we return "ok"
    except:
        return "error" # if the site doesn't exists or if the url is malformed, we return an error


class explorer:
    def __init__(self,site_url:str) -> None:
        """
        This class is used as the explorer itself.
        """
        if type(site_url) != str:
            return None

        self.site_url = site_url # this is the url provided by user
        self.url_list = [self.site_url] # this is the list used to store the nexts links to process
        self.urls_and_sources = {} # this dictionnary store the "final data"


    def find_internal_links(self,url:str) -> tuple:
        """
        This method take as argument the url of a web page and return the url itself and all internal links found in the html content of the page.
        """
        if type(url) != str:
            return []

        internal_links = [] # list of internal links
        domain_name = urlparse(url).netloc # domain name of the site (this is useful to know if a link is internal or external)
        soup = bs(requests.get(url).content, "html.parser") # find the html content

        for a in soup.findAll("a"):
            """
            for each link we find :
            """
            href = a.attrs.get("href") # find the link itself
            if href == "" or href is None: # if the link is null, we continue
                continue
                
            href = urljoin(url, href)
            parsed_href = urlparse(href)
            href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path

            if href in internal_links:
                continue # if the link has been already found, we continue

            if domain_name in href:
                internal_links += [href] # if the link is internal, we add it to the list

        return (url,internal_links) #return of the url and the list


    def explore(self) -> None:
        """
        this method the the "main" method of the class explorer.
        """
        for url in self.url_list: # each url is processed.
            base_url,internal_links = self.find_internal_links(url) # find every internal links in the page.
            for link in internal_links:
                if not link in self.url_list: # if this is a new link :
                    print(f"[+] link found : {link} (source : {base_url})\n") # output
                    self.url_list.append(link) # added to urls to process
                try:
                    self.urls_and_sources[base_url].append(link) # if there is already an element for this base url into the dictionnary
                except:
                    self.urls_and_sources[base_url] = [link] 
    
    
    def save_results(self,filename:str) -> None:
        """
        This method is used to store data into a file if asked by user
        """
        if type(filename) != str:
            return None

        with open(filename,"w") as file:
            for key,value in self.urls_and_sources.items():
                file.write(key + " : \n") # we write the source url
                for link in value:
                    file.write(link + "\n") # we write each url found with the source url
                file.write("\n") # a space to make the file more readable
            file.close()
    
    
def main() -> None:
    """
    This is the main function. After doing some tests about the url provided by the user,
    we create an explorer and we use it. Then we verify if the user specified a file to store results.
    If it is, we write all urls found into the file.
    """
    print("###### automated pages explorer ######")
    try:
        url = argv[1] #try to store url provided by user 
    except IndexError:
        print("[-] error : url not specified")
        return None

    test_url = verify_url(url) # verification of the url

    if test_url == "error":
        print(f"[-] error : url {url} is invalid")
        return None

    pages_explorer = explorer(url) # create the explorer
    pages_explorer.explore() # explore
    
    try:
        filename = argv[2] # try to find the storing file name
        print(f"Saving into {filename}...")
    except IndexError:
        return None

    pages_explorer.save_results(filename) # store urls into the file
    
if __name__ == "__main__":
    main()
