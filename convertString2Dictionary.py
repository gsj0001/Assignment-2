import urllib

def convertString2Dictionary(inputString = ""):
    inputString = urllib.unquote(inputString)
    returnDict = {}
    while inputString.find('=') != -1:
        equalsIndex = inputString.find('=')
        keyTemp = inputString[:equalsIndex].rstrip()
        keyTemp = keyTemp.lstrip()
        if keyTemp in returnDict:
            break
        if stringContainsInvalidCharacters(keyTemp):
            break
        commaIndex = inputString.find(',')
        if commaIndex == -1:
            valueTemp = inputString[equalsIndex+1:].rstrip()
            valueTemp = valueTemp.lstrip()
            print valueTemp
            if stringContainsInvalidCharacters(valueTemp):
                break
            returnDict[keyTemp] = valueTemp
            return returnDict
        else:
            valueTemp = inputString[equalsIndex+1:commaIndex].rstrip()
            valueTemp = valueTemp.lstrip()
            if stringContainsInvalidCharacters(valueTemp):
                break
            returnDict[keyTemp] = valueTemp
            inputString = inputString[commaIndex+1:]

    errorDict = {'error':'true'}
    return errorDict

#checks for characters that aren't alphanumeric, '=', or ','; Returns true if any are found.
#essentially, all characters that are given in this list that can be percent-encoded, as listed here: https://developer.mozilla.org/en-US/docs/Glossary/percent-encoding
#also checks to make sure the string isn't blank, after white space is stripped from the right
#also checks to make sure that a numeral doesn't lead the string
def stringContainsInvalidCharacters(testString = ""):
    return testString == "" or testString.find(' ') != -1 or testString.find('/') != -1 or testString.find('?') != -1 or testString.find('#') != -1 or testString.find('[') != -1 or testString.find(']') != -1 or testString.find('@') != -1 or testString.find('!') != -1 or testString.find('$') != -1 or testString.find('&') != -1 or testString.find("'") != -1 or testString.find('(') != -1 or testString.find(')') != -1 or testString.find('*') != -1 or testString.find('+') != -1 or testString.find(';') != -1 or testString.find('%') != -1 or testString.find('1') == 0 or testString.find('2') == 0 or testString.find('3') == 0 or testString.find('4') == 0 or testString.find('5') == 0 or testString.find('6') == 0 or testString.find('7') == 0 or testString.find('8') == 0 or testString.find('9') == 0 or testString.find('0') == 0