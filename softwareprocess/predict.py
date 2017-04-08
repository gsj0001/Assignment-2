__CURRENT_YEAR__ = 2017

def predict(values=None):
    starNames = ['Alpheratz', 'Ankaa', 'Schedar', 'Diphda', 'Achernar', 'Hamal', 'Polaris', 'Akamar', 'Menkar', 'Mirfak', 'Aldebaran', 'Rigel', 'Capella', 'Bellatrix', 'Elnath', 'Alnilam', 'Betelgeuse', 'Canopus', 'Sirius', 'Adara', 'Procyon', 'Pollux', 'Avior', 'Suhail', 'Miaplacidus', 'Alphard', 'Regulus', 'Dubhe', 'Denebola', 'Gienah', 'Acrux', 'Gacrux', 'Alioth', 'Spica', 'Alcaid', 'Hadar', 'Menkent', 'Arcturus', 'Rigil', 'Kent', 'Zubenelg', 'Kochab', 'Alphecca', 'Antares', 'Atria', 'Sabik', 'Shaula', 'Rasalhague', 'Etamin', 'Kaus', 'Aust.', 'Vega', 'Nunki', 'Altair', 'Peacock', 'Deneb', 'Enif', 'Alnair', 'Fomalhaut', 'Scheat', 'Markab']

    if(values == None or not 'body' in values or not 'date' in values or not 'time' in values):
        return {'error':'mandatory information is missing', 'op':'predict'}
    if(not values['body'] in starNames):
        values['error'] = 'star not in catalog'
        return values
    dateValues = 
    if(dateValues[0] >= __CURRENT_YEAR__ or dateValues[1] > 12 or dateValues[2] > 31):
        values['error'] = 'invalid date'
        return values

    return  values
