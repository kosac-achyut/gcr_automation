# gcr_automation
This project is based on Automating the login procedure in classes for student having multiple classes using Python3 and  Selenium.
This project only work on Chrome.

Selenium is a portable framework for testing web applications. Selenium provides a playback tool for authoring functional tests without
the need to learn a test scripting language.

Project is based on fixied automation (No Intelligent Automation)
The Whole process of automation is divide into three step:

## Login in to Google account
Now if you try to login in google account direct there is chance that it wil not allow as the project usese Chrome automation extension and
Google detect the Chrome as automated Chrome.
So the approach is to login in to stackover flow using google then redirect to google meets which will work as Login in only one time.
So no Captcha....

## Login in GCR
The automation will log in to the Google Class Room.
The automation will wait for the given length of the class then redirect to new class room.
For time tigger I have use  TIME library of python.<br>

Input flow<br>
username<br>
password<br>
number of classes<br>
class code<br> 
class start time in 24:00 format<br>
length of class in minute<br>

input shall be given via your os command line/terminal
