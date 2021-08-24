
import datetime
import time
import pytz




def input_checker(val1, val2):
    users_input = input()
    while users_input.lower() != val1 and users_input.lower() != val2:
        print('Please enter either "%s" or "%s"!'%(val1,val2))
        users_input = input()
    return users_input.lower()

def complex_countdown(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    date = date-datetime.datetime.now()
    t = int(date.total_seconds())*60
    print(t)
    while t > 0:
        mins, secs = divmod(t,60)
        timeformat = '{:d}:{:02d}'.format(mins, secs)
        print(timeformat)
        time.sleep(1)
        t -= 1
    print('Time is up!')
    return

def simple_countdown(t):
    while t > 0:
        mins, secs = divmod(t,60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat)
        time.sleep(1)
        t -= 1
    print('Time is up!')
    return

def main():
    print('Hello! Would you like to enter a full date or just time?')
    print('Please enter "date" or "simple"')
    users_input = input_checker('date', 'simple')
    future_countdown = ''
    if users_input == 'simple':
        while True:
            countdown_input = input('Please enter the duration of your countdown in seconds: ')
            try:
                countdown_input = int(countdown_input)
                break
            except:
                print('Please enter an integer.')
        simple_countdown(countdown_input)
    else:
        while True:
            input_year = 2000
            while True:
                input_year = input('Please enter the year: ')
                try:
                    input_year = int(input_year)
                    if input_year >= datetime.date.today().year:
                        break
                except:
                    print('Please enter an integer...')
            while True:
                input_month = input('Please enter the month: ')
                try:
                    input_month = abs(int(input_month))
                    if input_month <= 12:
                        if input_year > datetime.date.today().year or input_month >= datetime.date.today().month:
                            break
                except:
                    print('Please enter an integer...')
            while True:
                input_day = input('Please enter the day: ')
                try:
                    input_day = int(input_day)
                    future_date = str(input_year)+'-'+str(input_month)+'-'+str(input_day)
                    future_date_comparison1 = str(input_year)+'-'+str(input_month)+'-'+str(1)
                    future_date_comparison2 = str(input_year)+'-'+str(input_month+1)+'-'+str(1)
                    future_date_comparison1 = datetime.datetime.strptime(future_date_comparison1, '%Y-%m-%d')
                    future_date_comparison2 = datetime.datetime.strptime(future_date_comparison2, '%Y-%m-%d')

                    days_of_the_month=future_date_comparison2-future_date_comparison1
                    days_of_the_month = days_of_the_month.days
                    future_date = datetime.datetime.strptime(future_date, '%Y-%m-%d')
                    if input_day <= days_of_the_month and input_day>0:
                        if input_year > datetime.date.today().year:
                            break
                        elif input_month > datetime.date.today().month:
                            break
                        elif input_day > datetime.date.today().day:
                            break
                except Exception as e:
                    print('Please enter an integer...')
                    print(e)
            break
        future_countdown = str(input_year)+'-'+str(input_month)+'-'+str(input_day)
        complex_countdown(future_countdown)
    print('Would you like to start over? (y/n)')
    start_over = input_checker('y','n')
    if start_over == 'y':
        main()
    else:
        print('Goodbye!')




if __name__=='__main__':main()