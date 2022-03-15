import requests

class APICall:
    ''' Base class to make basic API calls with requests. '''
    
    def call(self, method, api_url):
        if method.lower() == 'get':
            return self.get(api_url)
        else:
            print(f'Method {method} not supported.')
        

    def get(self, api_url):
        ''' Make a GET request to the API. '''
        try:
            response = requests.get(api_url)
            if response.status_code in [200, 201, 202]:
                return response.json()
            else:
                raise Exception(f'API Error: {response.status_code}')
            
        except requests.exceptions.RequestException as e:
            print(e)
            return None