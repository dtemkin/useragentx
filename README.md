# useragentx
A UserAgent spoofer that retrieves list of potential user-agent strings from 'www.useragentstring.com'

<b>Example</b>

>> import useragentx
# OR
>> from useragentx import spoofer

To select specific platforms:

>> plat = useragentx.spoofer.platform()

>> chrome = plat.browser('Chrome')

>> chrome = plat.browser('Chrome', 0) (Automatically returns most recent version of Chrome from available list)

>> mobile_ie = plat.mobile('IE')

>> mobile_ie = plat.mobile('IE', 0) (Same in Mobile and Crawler functions)

>> crawler_google = plat.crawler('google') 
For google crawler only, available crawlers are numbered as follows:

  0: googlebot
  1: googlebot-images
  2: googlebot-videos
  3: googlebot-smartphone (Android I believe)

To show accepted platforms

>> useragentx.spoofer.platform().show_supported('mobile') #For list of Mobile Agents

>> useragentx.spoofer.platform().show_supported('browser') #For list of Web Browser Agents

>> useragentx.spoofer.platform().show_supported('crawler') #For list of Web Crawler Agents

The script will accept other valid values these functions just include the ones I controlled for more to come later

To Select UserAgent from complete list of 2958 (includes web browsers, mobile, bots, gaming platforms, and others)

>> useragentx.spoofer.platform().ALL()

<b>Sample Usage Script </b>

    import requests (or urllib) 

    from useragentx import spoofer
    
    urlargs = {'connection':'keep-alive','user-agent': spoofer.platform().browser('Chrome', 2)}
    
    req = requests.get('http://foo.com/bar', params=urlargs)
    
    return req.text
