import urllib3
import json

class Latest_fact():
    def __init__(self):
        self.file_read = open ('21. TIL facts.txt','r')
        self.file_append = open ('21. TIL facts.txt', 'a')
        self.file_urls = open('21. TIL facts urls.txt', 'a')
        self.file_lines = [lines.strip() for lines in self.file_read.readlines()]
        req = urllib3.PoolManager()
        header = {'User-agent': 'Python test'}
        url = 'https://www.reddit.com/r/todayilearned/new.json'
        url_json = req.request('GET', url, headers=header)
        url_json_data = json.loads(url_json.data.decode('utf-8'))
        self.json_data = url_json_data['data']['children'][0]['data']
        self.__fact_grammar()
        self.__duplicate_check()
        self.__print_result()
        self.file_read.close()
        self.file_append.close()
        self.file_urls.close()
        return



    def __fact_grammar(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.json_data_title = self.json_data['title']
        if 'TIL that' in self.json_data_title:
            self.json_data_title = self.json_data_title[9].upper() + self.json_data_title[10:]
        elif 'TIL: ' in self.json_data_title:
            self.json_data_title[-1] = self.json_data_title[5].upper() + self.json_data_title[6:]
        elif 'TIL ' in self.json_data_title:
            self.json_data_title = self.json_data_title[4].upper() + self.json_data_title[5:]
        if self.json_data_title[-1] not in alphabet:
            self.json_data_title = self.json_data_title[:-1] + '!'
        else:
            self.json_data_title = self.json_data_title + '!'
        return

    def __duplicate_check(self):
        try:
            if self.json_data_title == self.file_lines[-1]:
                print('Fact already exists')
            else:
                self.file_append.write(self.json_data_title+'\n')
                self.file_urls.write(self.json_data['url']+'\n')
        except IndexError:
            print('file = empty')
            self.file_append.write(self.json_data_title + '\n')
            self.file_urls.write(self.json_data['url'] + '\n')
        return

    def __print_result(self):
        print(self.json_data_title)

    def title(self):
        return self.json_data['title']

    def link(self):
        return self.json_data['url']
