import math

def correct(values=None):
#######################################################################################
# Testing for missing/invalid values
#######################################################################################

    if(values == None or not 'lat' in values or not 'long' in values or not 'altitude' in values or not 'assumedLat' in values or not 'assumedLong' in values):
        values = {'error': 'mandatory information is missing', 'op':'correct'}
        return values
    if(not 'd' in values['lat']):
        values['error'] = 'invalid input for lat'
        return values
    if (not 'd' in values['long']):
        values['error'] = 'invalid input for long'
        return values
    if (not 'd' in values['altitude']):
        values['error'] = 'invalid input for altitude'
        return values
    if (not 'd' in values['assumedLat']):
        values['error'] = 'invalid input for assumedLat'
        return values
    if (not 'd' in values['assumedLong']):
        values['error'] = 'invalid input for assumedLong'
        return values

#######################################################################################
#Testing for non-int values for degrees
#######################################################################################
    latitude = values['lat'].split('d')
    try:
        latitudeMinutes = int(latitude[0])
    except ValueError:
        values['error'] = 'invalid lat'
        return values
    if(latitudeMinutes >90 or latitudeMinutes<-90):
        values['error'] = 'invalid lat'
        return values
    latitudeSeconds = float(latitude[1])

    longitude = values['long'].split('d')
    try:
        longitudeMinutes = int(longitude[0])
    except ValueError:
        values['error'] = 'invalid long'
        return values
    longitudeSeconds = float(longitude[1])

    altitude = values['altitude'].split('d')
    try:
        altitudeMinutes = int(altitude[0])
    except ValueError:
        values['error'] = 'invalid altitude'
        return values
    altitudeSeconds = float(altitude[1])

    assumedLatitude = values['assumedLat'].split('d')
    try:
        assumedLatitudeMinutes = int(assumedLatitude[0])
    except ValueError:
        values['error'] = 'invalid assumedLat'
        return values
    if (assumedLatitudeMinutes > 90 or assumedLatitudeMinutes < -90):
        values['error'] = 'invalid assumedLat'
        return values
    assumedLatitudeSeconds = float(assumedLatitude[1])

    assumedLongitude = values['assumedLong'].split('d')
    try:
        assumedLongitudeMinutes = int(assumedLongitude[0])
    except ValueError:
        values['error'] = 'invalid assumedLong'
        return values
    assumedLongitude[1] = float(assumedLongitude[1])

#######################################################################################
#Converting to radians, for the use of math library trig functions
#######################################################################################

    latitudeRadians = convertStringToRadians(values['lat'])
    longitudeRadians = convertStringToRadians(values['long'])
    altitudeRadians = convertStringToRadians(values['altitude'])
    assumedLatitudeRadians = convertStringToRadians(values['assumedLat'])
    assumedLongitudeRadians = convertStringToRadians(values['assumedLong'])

#######################################################################################
#Computing
#######################################################################################

    localHourAngleRadians = addAngleRadians(longitudeRadians, assumedLongitudeRadians)

    intermediateDistanceRadians = (math.sin(latitudeRadians) * math.sin(assumedLatitudeRadians)) + (math.cos(latitudeRadians) * math.cos(assumedLatitudeRadians) * math.cos(localHourAngleRadians))

    correctedAltitudeRadians = math.asin(intermediateDistanceRadians)

    correctedDistanceRadians = altitudeRadians - correctedAltitudeRadians

    correctedDistanceArcMinutes = int(correctedDistanceRadians * 10800 / math.pi)

    correctedAzimuthRadians = azimuth(latitudeRadians, assumedLatitudeRadians, intermediateDistanceRadians)

    values['correctedDistance'] = str(correctedDistanceArcMinutes)

    values['correctedAzimuth'] = convertDegreesToString(convertRadiansToDegrees(correctedAzimuthRadians))

    return values

def azimuth(lat, assumedLat, intermediateDistance):
    return math.acos( (math.sin(lat) - (math.sin(assumedLat) * intermediateDistance)) / (math.cos(assumedLat) * math.cos(math.asin(intermediateDistance))))


##assuming string
def convertStringToRadians(angle):
    splitStrings = angle.split('d')
    minutes = splitStrings[0]
    seconds = splitStrings[1]
    angleDegrees = float(splitStrings[0]) + float(splitStrings[1])
    angleRadians = angleDegrees * math.pi / 180

    return angleRadians

#assuming two floats
def addAngleRadians(angle1, angle2):
    angle = angle1 + angle2
    simplifyRadians(angle)
    return angle


#angleAsAList is assumed to have only two elements in it, minutes and seconds
#returns a string for the purposes of values[]
def convertDegreesToString(angleAsAList):
    return str(angleAsAList[0]) + 'd' + str(angleAsAList[1])

def convertRadiansToDegrees(radians):
    degrees = float(radians * 180 / math.pi)

    degreesInt = int(degrees)

    degreesList = [degreesInt, float(degrees - degreesInt)]

    degreesList[1] = round(degreesList[1] * 60, 1)

    return degreesList

def simplifyRadians(radians):
    while(radians > math.pi):
        radians-=2*math.pi
    while(radians < -1 * math.pi):
        radians+=2*math.pi

    return radians
