from . import *

notice = "\
I only selected the browers and mobile browsers I felt were most popular but there are many, many more available.\
Check: http://www.useragentstring.com/pages/useragentstring.php for a complete list,\
\
If you want to take a gamble that the name is right, you can try inputing your own name string\
in their respective fields there is no value check on these fields for this purpose and the id numbering\
varies depending the length of the url reponse field."


googlebots = {0:'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
              1:'Googlebot-Image/1.0',2:'Googlebot-Video/1.0',
              3:'​Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

def get(name_, parser, u, typ):

    uareq  = requests.get(u)
    soup = bs4.BeautifulSoup(uareq.text, parser)
    listraw = soup.find('div', {'id':'liste'})
    if typ == 0:
        ualist = [x.string for x in listraw.findAll('h4')]
    elif typ == 1 or 2:
        ualist = [x.string for x in listraw.findAll('li')]
    else:
        print('Type ID Error')
        
    ualist_ids = [i for i in range(len(ualist))]
    uadict = map(lambda x, y: (x, y), ualist_ids, ualist)
    uadict = dict(uadict)
    return uadict


def select(name_, useragents):
    if len(useragents) > 100:
        print("Warning: There are more than 100 User Agents detected!")
        limit = input('Would you like to set a limit on the number displayed (Max: %s)? (Enter Number or No) ' % len(useragents))
        if str(limit).lower() in ["no",'n']:
            print('Displaying All Available User Agents: \n')
            print(useragents)
        else:
            if int(limit) <= len(useragents):
                print("Displaying %s of %s Available UserAgent Strings: \n" % (limit, len(useragents)))
                print({k: useragents[k] for k in sorted(useragents.keys())[:int(limit)]})
            else:
                print('Displaying All Available User Agents: \n')
                print(useragents)
    else:
        print('Displaying All Available User Agents: \n')
        print(useragents)

    ua_select = input("\nID of desired User Agent: ")
    if int(ua_select) not in useragents:
        print("Invalid ID")
    else:
        return int(ua_select)

class spoof:

    def __init__(self, parser='lxml'):
        self.htmlparser = parser
        self.baseurl = 'http://www.useragentstring.com/pages/useragentstring.php?'
        self.supported_browsers = ['Chrome','Firefox','Internet Explorer',
                                   'Opera','Safari','Netscape']
        self.supported_mobile = ['NokiaGo','BlackBerry','Opera','Android']
        self.supported_crawlers = ['Google-Search','Google-Image',
                                   'Google-Video','Google-Smartphone',
                                   'YandexBot','BaiduSpider','Holmes']
        self.ua_select = None
        self.useragent_dict = None
        
    def show_supported(self, typ):
        print(notice)
        if typ.lower() is 'mobile':
            print("Known Mobile UserAgent Platforms: \n\n")
            print(self.supported_mobile)
        elif typ.lower() is 'browser':
            print("Known Web Browser UserAgent Platforms: \n\n")
            print(self.supported_browser)
        elif typ.lower() is 'crawler' or 'bot':
            print("Known Web Crawler UserAgent Platforms: \n\n")
            print(self.supported_crawlers)
        else:
            print('Bots and Other Platforms are not yet referenced explicitly \
but I intend on adding that functionality soon. Til then you are more than welcome to try \
the name in the browser_name field of the browser function just place %20 \
for every space in the name.')

    def browser(self, name, uaid=None):
        if name.lower() is 'ie':
            browser_ = 'Internet Explorer'
        elif name.lower() in [x.lower() for x in self.supported_browsers]:
            browser_ = name
        else:
            print('Name not recognized but trying url request anyway.')
            browser_ = name

        url = ''.join([self.baseurl, "name=%s" % browser_])
        try:
           self.useragent_dict = get(browser_, self.htmlparser, url, 0)
        except Exception as errmsg:
            print('Error: %s' % errmsg)
        else:
            if uaid is not None:
                if int(uaid) in self.useragent_dict:
                    return self.useragent_dict[uaid]
                else:
                    print('Invalid ID')
            else:
                selection = select(browser_, self.useragent_dict)
                return self.useragent_dict[int(selection)]
                    

    def mobile(self, name, uaid=None):
        name_conv_dict = {'nokiago':'Go%20Browser','opera':'Opera%20Mobile',
                          'ie':'IE%20Mobile','android':'Android%20Webkit%20Browser'}
        if name.lower() in name_conv_dict:
            mobile_ = name_conv_dict[name.lower()]
        elif name.lower() in [x.lower() for x in self.supported_mobile]:
            mobile_ = name
        else:
            print('Name not internally listed will try anyway.')
            mobile_ = name
        
        url = ''.join([self.baseurl, 'name=%s' % mobile_])
        try:
            self.useragent_dict = get(mobile_, self.htmlparser, url, 1)
        except Exception as errmsg:
            print("Error: %s" % errmsg)
        else:
            if uaid is not None:
                if int(uaid) in self.useragent_dict:
                    return self.useragent_dict[uaid]
                else:
                    print('Invalid ID')
            else:
                selection = select(mobile_, self.useragent_dict)
                return self.useragent_dict[int(selection)]

    def crawler(self, name, uaid=None):
        name_conv_dict = {'baidu':'Baiduspider','yahoo':'YahooSeeker',
                          'yandex':'YandexBot'}
        googlebots_dict ={0: 'google-search',1:'google-image', 2: 'google-video', 3: 'google-smartphone'}
        if name.lower() in ['google','googlebot','google-bot','google-crawler']:
            if uaid is None:
                print('Available Google Bots: \n')
                print(dict({0: 'google-search',1: 'google-image',
                            2: 'google-video', 3: 'google-smartphone'}))
                googlebot_select = input('Enter ID of Desired Google Bot UserAgent: ')
                if int(googlebot_select) in googlebots:
                    return googlebots[int(googlebot_select)]
                else:
                    print("ID not valid")
            else:
                googlebot_select = uaid
                if int(googlebot_select) in googlebots:
                    return googlebots[googlebot_select]
                else:
                    print("ID not valid")
            
        else:
            if name.lower() in name_conv_dict:
                bot_ = name_conv_dict[name.lower()]
            elif name.lower() in [x.lower() for x in self.supported_crawlers]:
                bot_ = name
            else:
                print('Name not internally listed will try anyway.')
                bot_ = name

        
        url = ''.join([self.baseurl, 'name=' % bot_])
        try:
            self.useragent_dict = get(bot_, self.htmlparser, url, 2)
        except Exception as errmsg:
            print('Error: %s' % errmsg)
        else:
            if uaid is not None:
                if int(uaid) in self.useragent_dict:
                    return self.useragent_dict[uaid]
                else:
                    print('Invalid ID')
            else:
                selection = select(bot_, self.useragent_dict)
                return self.useragent_dict[int(selection)]
                    
              
    def ALL(self, uaid=None):
        ## Warning: There are an enormous number (2958 at last count) of potential UserAgents
            ## Not all of which may fit in the active browser window!
        url = ''.join([self.url, 'name=All'])
        try:
            self.useragent_dict = get('All', url, 0)
        except Exception as errmsg:
            print("Error: %s" % errmsg)
        else:
            if uaid is not None:
                if int(uaid) in self.useragent_dict:
                    return self.useragent_dict[uaid]
                else:
                    print('Invalid ID')
            else:
                selection = select('All', self.useragent_dict)
                return self.useragent_dict[int(selection)]

