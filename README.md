# PriceTracker

This project scrapes many shopping websites based in Turkey. 
The main goal: 
  Let's say you have 100 Turkish Liras and you want anything from the websites specified in the program from over 100 Turkish Liras.
  You copy the link and paste it to the program. After that program asks you, what price do you want to buy it. Later, when program is runned, program scrapes the price ticket
  and if price is under than the price you wanted, it sends an mail to your e-mail address.
  
  
The program scrapes these websites:
 -n11
 -gittigidiyor
 -amazon
 -morhipo
 -epttavm
 -trendyol
 -hepsiburada
 
Program uses Requests, BeautifulSoup4, and SMTPLib.
Main file is url_seperator.py
