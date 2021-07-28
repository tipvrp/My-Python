import webbrowser
import datetime
dt_now = datetime.datetime.now() # M0 T1 W2 H3 F4 S5 Sun6 
n=10
url = [ "https://zoom.us/j/***********************************************", #English Conversation M9-12   0
        "https://zoom.us/j/***********************************************", #Select topic M13-16          1
        "https://zoom.us/j/***********************************************", #Optical M17-20               2
        "https://zoom.us/j/***********************************************", #Machine Learning T13-16      3
        "https://zoom.us/j/***********************************************", #Compro TA W13-15             4
        "https://zoom.us/j/***********************************************", #Bridge H10-12                5
        "https://zoom.us/j/***********************************************", #Computer Network H13-16      6
        "https://zoom.us/j/***********************************************", #Compro TA F PIV              7
        "https://zoom.us/j/***********************************************", #Compro TA F RSK              8
      ]
#-------------------------------------------------------------- Monday
if dt_now.weekday() == 0 and 8 <= dt_now.hour < 12 :
    n = 0
if dt_now.weekday() == 0 and 12 <= dt_now.hour < 16 :
    n = 1
if dt_now.weekday() == 0 and 16 <= dt_now.hour < 20 :
    n = 2
#--------------------------------------------------------------  Tuesday 
if dt_now.weekday() == 1 and 12 <= dt_now.hour < 16 :
    n = 3
#--------------------------------------------------------------  Wednesday
if dt_now.weekday() == 2 and 12 <= dt_now.hour < 16 :
    n = 4
#--------------------------------------------------------------  Thursday
if dt_now.weekday() == 3 and 9 <= dt_now.hour < 12 :
    n = 5
if dt_now.weekday() == 3 and 12 <= dt_now.hour < 16 :
    n = 6
#-------------------------------------------------------------- Friday
if dt_now.weekday() == 4 and 12 <= dt_now.hour < 15 :
    n = 7
if dt_now.weekday() == 4 and 15 <= dt_now.hour < 17 :
    n = 8
#---------------------------------------------------------------
if n != 10 :
    webbrowser.open_new(url[n])
