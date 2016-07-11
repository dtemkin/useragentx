import requests
from bs4 import BeautifulSoup as bsoup

notice = "\
I only selected the browers and mobile browsers I felt were most popular but there are many, many more available.\
Check: http://www.useragentstring.com/pages/useragentstring.php for a complete list,\
\
If you want to take a gamble that the name is right, you can try inputing your own name string\
in their respective fields there is no value check on these fields for this purpose and the id numbering\
varies depending the length of the url reponse field."

class platform:

    def __init__(self, parser='lxml'):
        self.htmlparser = parser
        self.url = 'http://www.useragentstring.com/'
        self.supported_browsers = ['Chrome','Firefox','Internet Explorer',
                                   'Opera','Safari','Netscape']
        self.supported_mobile = ['NokiaGo','BlackBerry','Opera','Android']

    def show_platforms(self, typ):
        print(notice)
        if typ is 'mobile':
            print("Mobile UserAgent Platforms: \n\n")
            print(self.supported_mobile)
        elif typ is 'browser':
            print("Web Browser UserAgent Platforms: \n\n")
            print(self.supported_browser)
        else:
            print('Bots and Other Platforms are not yet referenced explicitly \
but I intend on adding that functionality soon. Til then you are more than welcome to try \
the name in the browser_name field of the browser function just place %20 \
for every space in the name.')
            
    def browser(self, name):
        if name is 'IE':
            browser_ = 'Internet%20Explorer'
        else:
            browser_ = name
        url = ''.join([self.url, 'pages/%s/' % browser_])
        uareq  = requests.get(url)
        soup = bsoup(uareq.text, self.htmlparser)
        listraw = soup.find('div', {'id':'liste'})
        ualist = [x.string for x in listraw.findAll('h4')]
        ualist_ids = [i for i in range(len(ualist))]
        uadict = map(lambda x, y: (x, y), ualist_ids, ualist)
        useragent_dict = dict(uadict)
        if len(ualist_ids) > 100:
            print("Warning: There are more than 100 User Agents detected!")
            limit = input('Would you like to set a limit on the number displayed (Max: %s)? (Enter Number or No)' % len(ualist_ids))
            if limit is "No":
                print('Displaying All Available User Agents: \n')
                print(useragent_dict)
            elif int(limit) <= len(ualist):
                print("Displaying %s of %s Available UserAgent Strings: \n" % (limit, len(ualist)))
                print({k: useragent_dict[k] for k in sorted(useragent_dict.keys())[:int(limit)]})
        else:
            print('Displaying All Available User Agents: \n')
            print(useragent_dict)
            
        ua_select = input("\nID of desired User Agent: ")
        if int(ua_select) not in ualist_ids:
            print("Invalid ID")
        else:
            return useragent_dict[int(ua_select)]

    def mobile(self, name):
        name_conv_dict = {'NokiaGo':'Go%20Browser','Opera':'Opera%20Mobile',
                          'IE':'IE%20Mobile','Android':'Android%20Webkit%20Browser'}
        if name in name_conv_dict.keys:
            mobile_ = name_conv_dict[mobile_name]
        else:
            mobile_ = name
        url = ''.join([self.url, 'pages/%s/' % mobile_])
        uareq  = requests.get(url)
        soup = bsoup(uareq.text, self.htmlparser)
        listraw = soup.find('div', {'id':'liste'})
        ualist = [x.string for x in listraw.findAll('h4')]
        ualist_ids = [i for i in range(len(ualist))]
        uadict = map(lambda x, y: (x, y), ualist_ids, ualist)
        useragent_dict = dict(uadict)
        if len(ualist_ids) > 100:
            print("Warning: There are more than 100 User Agents detected!")
            limit = input('Would you like to set a limit on the number displayed (Max: %s)? (Enter Number or No)' % len(ualist_ids))
            if limit is "No":
                print('Displaying All Available User Agents: \n')
                print(useragent_dict)
            elif int(limit) <= len(ualist):
                print("Displaying %s of %s Available UserAgent Strings: \n" % (limit, len(ualist)))
                print({k: useragent_dict[k] for k in sorted(useragent_dict.keys())[:int(limit)]})
        else:
            print('Displaying All Available User Agents: \n')
            print(useragent_dict)
            
        ua_select = input("\nID of desired User Agent: ")
        if int(ua_select) not in ualist_ids:
            print("Invalid ID")
        else:
            return useragent_dict[int(ua_select)]


    def from_all_(self):
        ## Warning: There are an enormous number (2958 at last count) of potential UserAgents
            ## Not all of which may fit in the active browser window!
        url = ''.join([self.url, 'pages/All/'])
        uareq  = requests.get(url)
        soup = bsoup(uareq.text, self.htmlparser)
        listraw = soup.find('div', {'id':'liste'})
        ualist = [x.string for x in listraw.findAll('h4')]
        ualist_ids = [i for i in range(len(ualist))]
        uadict = map(lambda x, y: (x, y), ualist_ids, ualist)
        useragent_dict = dict(uadict)
        if len(ualist_ids) > 100:
            print("Warning: There are more than 100 User Agents detected!")
            limit = input('Would you like to set a limit on the number displayed (Max: %s)? (Enter Number or No)' % len(ualist_ids))
            if limit is "No":
                print('Displaying All Available User Agents: \n')
                print(useragent_dict)
            elif int(limit) <= len(ualist):
                print("Displaying %s of %s Available UserAgent Strings: \n" % (limit, len(ualist)))
                print({k: useragent_dict[k] for k in sorted(useragent_dict.keys())[:int(limit)]})
        else:
            print('Displaying All Available User Agents: \n')
            print(useragent_dict)
            
        ua_select = input("\nID of desired User Agent: ")
        if int(ua_select) not in ualist_ids:
            print("Invalid ID")
        else:
            return useragent_dict[int(ua_select)]

