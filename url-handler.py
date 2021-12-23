# The logic behind this is code is to decode copied URLs from outllok in order to
# scan them using VirusTotal.com
# 
# How to use:
# Right-click an outlook link, copy it, paste it in safe-urls.txt, repeat for any links to test.
# Put each in a new line.
#
# Resulting URLs are found in unsafe-urls.txt. Make sure not to click them in case they are malicious.
#
# Code flow:
# Read the contents of the file safe-urls.txt, remove the Outlook safe link, 
# replace the UTF-8 symbols with their correct URL indentifier.
#


# Read the contents of the file safe-urls.txt
oldURL = open('safe-urls.txt', 'r')
oldURL = oldURL.read()

# Remove the Outlook safe link
oldURL = oldURL.replace('https://eur02.safelinks.protection.outlook.com/?url=', '')


# The symbols to replace
oldSymbols = ['%20', '%25', '%26', '%2B', '%2F', '%3A', '%3F', '%3D', '%40', '%7C',]
newSymbols = [' ',   '%',   '&',   '+',   '/',   ':',   '?',   '=',   '@',   '|']


# Loop replacing the symbols
for old, new in zip(oldSymbols, newSymbols):
    oldURL = oldURL.replace(old, new)

# Write the modifyied URLs into unsafe-urls.txt
unsafeURL = open('unsafe-urls.txt', 'a')
unsafeURL.write(oldURL)
unsafeURL.write('\n----------------------------------------------\n')
unsafeURL.close()
