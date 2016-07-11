# useragent_hoodini
A UserAgent selector that retrieves list of potential user-agent strings from 'www.useragentstring.com'




Example

>> import useragent

To Select specific platforms:

>> plat = useragent.platform()
>> chrome = plat.browser('Chrome')
>> mobile_ie = plat.mobile('IE')

To show accepted platforms

>> useragent.platform().show_platforms('mobile') #For list of Mobile Platforms
>> useragent.platform().show_platforms('browser') #For list of Browser Platforms

The script will accept other valid values these functions just include the ones I controlled for more to come later

To Select UserAgent from complete list of 2958 (includes bots, gaming platforms, and others)

>> useragent.platform().from_all_()


