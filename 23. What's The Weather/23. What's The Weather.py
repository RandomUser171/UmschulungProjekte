import OpenWeatherMapClass


def input_checker(val,type):
    user_input = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    val_found = False
    if type == 'int':
        while val_found == False:
            user_input = input(f'Please enter the ZIP code: ')
            if len(user_input) == val:
                try:
                    int(user_input)
                    val_found = True
                except:
                    pass

    else:
        while val_found == False:
            user_input = input(f'Please enter the country code: ')
            if len(user_input) == val:
                val_found = True
                for letter in user_input:
                    if letter.lower() not in alphabet:
                        val_found = False
                        break
    return user_input

def main():
    user_input_country = input_checker(2, 'str')
    user_input_zip = input_checker(5, 'int')
    owm_api = OpenWeatherMapClass.OpenWeatherMap_api
    owm_api(user_input_country,user_input_zip)




if __name__=='__main__':main()