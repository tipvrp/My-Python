import webbrowser
import datetime
dt_now = datetime.datetime.now() # M0 T1 W2 H3 F4 S5 Sun6 
n=10
url = [ "https://zoom.us/j/92566534389?pwd=Y2FSbkhwOTZUS2xLai96NTJ3NmJVUT09", #English Conversation M9-12   0
        "https://zoom.us/j/7505560466?pwd=SzZFblRleVVsaVE2L0YweGgwNDBVUT09", #Select topic M13-16           1
        "https://zoom.us/j/8818507908?pwd=b3cvckxjMDNLVzhWeWY5a3dRRGZwdz09", #Optical M17-20                2
        "https://zoom.us/j/6693797485?pwd=cWVFc3BMVVZsNFVucWhSaVpkS1lIQT09", #Machine Learning T13-16       3
        "https://zoom.us/j/6456457914?pwd=MEN1SjJMaUwxZVR0Q242L042K2dmZz09", #Compro TA W13-15              4
        "https://zoom.us/j/97131084116?pwd=R1AvdXJBc0Vsa29keFd5cFYvdGVIZz09", #Bridge H10-12                5
        "https://zoom.us/j/7281157598?pwd=cDllSm81QkdMc1FaR0c5S2V2U2dxUT09", #Computer Network H13-16       6
        "https://zoom.us/j/6456457914?pwd=MEN1SjJMaUwxZVR0Q242L042K2dmZz09", #Compro TA F PIV               7
        "https://zoom.us/j/8671901631?pwd=YzJ5MzlxMTE3TVM5SHRBTGw0YklEUT09", #Compro TA F RSK               8
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
