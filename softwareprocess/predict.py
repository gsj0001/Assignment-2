def predict(values=None):
    if(values == None or not 'body' in values or not 'date' in values or not 'time' in values):
        return {'error':'mandatory information is missing', 'op':'predict'}
    return  values
