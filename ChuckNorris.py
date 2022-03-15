import APICall

class ChuckNorris(APICall):
    ''' This is the ChuckNorris API, since those jokes are still, and have always been, the best. '''

    def __init__(self):
        self.api_url = 'https://api.chucknorris.io/jokes/random'

    def get_joke(self):
        ''' Get a random Chuck Norris joke. '''
        return self.call('get', self.api_url)
