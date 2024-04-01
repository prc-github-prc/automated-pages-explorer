# Automated Pages Explorer :

**Disclaimer: This script is for educational purposes only.**
**Do not use against any network, system or application that you don't own or have authorisation to test.**

**Licence** : this project is under the [MIT licence](https://mit-license.org/).
************************************

**Automated Pages Explore**r is a **python** script to **automatically** explore a web application.
It is a **solo** project that I ([prc-github-prc](https://github.com/prc-github-prc)) developed to help web developers, web designers, web application pentesters or bug hunters to **enumerate** web applications. This program is different from tools like **gobuster** or **dirb**, which are tools that launch **dictionary based bruteforce attacks** against web application to find hidden files or *directory*. But the way that the script work will be detailed later.

**********
## Installation and configuration :

##### 1. Install git :
-windows : download the exe file for windows from the [official website](https://git-scm.com/download/win)

-linux (debian, ubuntu, kali...) : 
```
sudo apt install git
```
-linux (arch) : 
```
sudo pacman -S git
```

##### 2. Install python(3) :
-windows : download the exe file from the [official website](https://www.python.org/downloads/) (if pip is **not directly installed** with python, please consider **searching solutions on internet**)

-linux (debian, ubuntu, kali...) : 
```
sudo apt install python3 python3-pip
```
-linux (arch) : 
```
sudo pacman -S python3 python3-pip
```

##### 3. Install dependencies with pip (some dependencies may be already satisfied):

-powershell or cmd for windows, bash or sh for linux : 
```
pip install requests BeautifulSoup
```
or :
```
pip3 install requests BeautifulSoup
```

##### 4. Clone the project (commands are the same for windows and linux) :
```
git clone https://github.com/prc-github-prc/automated-pages-explorer/
cd automated-pages-explorer
```

##### 5. Utilisation (commands are the same for windows and linux) : 
from the project clone directory (./automated-pages-explorer/) :
```
python pages_expl.py <url> <save file (optional)>
```
or :
```
python3 pages_expl.py <url> <save file (optional)>
```

***************
## How it works ? :

The **main function** is the entry point of our program. It takes a user-provided url in argument. First, it tests the validity of the url with the **verify_url function**. Then, it creates an instance of the **explorer** class (it will be detailed later). It runs the **explore method** of the class and print the urls found. If a file is specified to store results, the main function writes all urls found.

The **explorer class** : Upon instantiation, it receives the user-provided url. The **explore method** is the "main method"of the explorer. Here’s what it does: 
```
urls_list <- [user_provided_url]
for url in urls_list :
	links <- internal_links(url)
	for link in links :
		if not link in urls_list:
			urls_list <- urls_list + link
```

This way of process works because in python when we iterate on a list, if new elements are added to the list, theses element **are processed to**. So in the case, we find **internal links** with the **user-provided url** . For each link, we do the **same**. And when there is no new link anymore, **the loop ends**.

If you want more details about how the **script works**, you can just **read the code and the comments**.

*******************

## How are structured the results backup files :

if the user-provided url is **https://www.random-example.url/**, the results backup file will be :
```
https://www.random-example.url/ :
https://www.random-example.url/page1
https://www.random-example.url/page2
...

https://www.random-example.url/page1 :
https://www.random-example.url/
...

https://www.random-example.url/page2 :
https://www.random-example.url/
...

```
This structure allow the user to know **from which page** the url was found. It is useful to make a **schema** or a **grap**h of the **structure of the targeted website**.
