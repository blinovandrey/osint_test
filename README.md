# osint_test
Test project about OSINT 

In this project there were used 2 OSINT frameworks: Harpoon and Datasploit. At first time I decided to use Birdwatcher for building twitter social graph. But this framework is only an interactive console tool and does not provide any API to use it in your code. By the way most of these frameworks that were listed in the test task are firstly console tools, and do not provide API. Datasploit provides API and can be used as library but only in python2. So, the only possible way I found was to call them directly from python script by executing shell commands and then printing and parsing stdout.

# how to use:
There are 2 ways:
1) open example.ipynb file by jupyter notebook and see the examples of using these frameworks
2) install and configure Harpoon and Datasploit, then run osint_test.py file and try extract some information
