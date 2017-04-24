

def correct(values=None):

    if(values == None or not 'lat' in values or not 'long' in values or not 'altitude' in values or not 'assumedLat' in values or not 'assumedLong' in values):
        values['error'] = 'mandatory information is missing'
        return values



    return values