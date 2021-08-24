import urllib3
import json
import webbrowser

class random_article():

    def __init__(self):
        req = urllib3.PoolManager()
        header = {'User-agent':'Python test'}
        url = 'https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=100&format=json'
        url_json = req.request('GET',url,headers=header)
        url_json = json.loads(url_json.data.decode('utf-8'))
        self.json_data = url_json['query']['random']
        '''for i in range(len(self.json_data)):
            print(self.json_data[i]['title'])
        pass'''
        self.article_chooser()

    def article_chooser(self):
        for i in range(len(self.json_data)):
            article = self.json_data[i]['title']
            print(self.json_data)
            print(f'Would you like to learn something about "{article}"?')
            user_input = input('Please enter "yes" or "no": ')
            while user_input != 'yes' and user_input != 'no':
                user_input = input('Please enter "yes" or "no".....: ')
            if user_input == 'no':
                pass
            else:
                temp_url = 'http://en.wikipedia.org/?curid=' + str(self.json_data[i]['id'])
                webbrowser.open(temp_url)
                break