import selenium

import random

from selenium import webdriver

from time import sleep


driver=webdriver.Chrome('/users/apple/desktop/chromedriver')

driver.get('form_url')

sleep(1)

js1="""get_random = function (list) {

  return list[Math.floor((Math.random()*list.length))];
  
}
var loc=[[0,1],[4,5],[11,12],[14,14],[15,16],[21,21],[22,23],[28,28],[32,33],[34,35]];

ifood=['AAA','BBB','CCC','DDD','EEE','FFF']

security=['AAAA','BBB','CCC','DDD']

overall=['AAA',"BBB","CCC",'DDD',"FFF"]

document.querySelectorAll("input.quantumWizTextinputPaperinputInput")[0].value =get_random(food);

document.querySelectorAll("input.quantumWizTextinputPaperinputInput")[1].value =get_random(security);

document.querySelectorAll("input.quantumWizTextinputPaperinputInput")[2].value =get_random(overall);

for(var i=0;i<10;i++){

    document.querySelectorAll('div.appsMaterialWizToggleRadiogroupRadioButtonContainer')[get_random(loc[i])].click();

console.log(i)

}"""



js2="""get_random = function (list) {

  return list[Math.floor((Math.random()*list.length))]; //random function to give random element from the list

}

var loc=[[0,1],[4,5],[11,12],[14,14],[15,16],[21,21],[22,23],[28,28],[32,33],[34,35]]; //change positions for radio button according to index and 2*2 is for getting a random button from a list 

ifood=['AAA','BBB','CCC','DDD','EEE','FFF']

security=['AAAA','BBB','CCC','DDD']

overall=['AAA',"BBB","CCC",'DDD',"FFF"]

document.querySelectorAll("input.quantumWizTextinputPaperinputInput")[0].value =get_random(food);

document.querySelectorAll("input.quantumWizTextinputPaperinputInput")[1].value =get_random(security);

document.querySelectorAll("input.quantumWizTextinputPaperinputInput")[2].value =get_random(overall);

for(var i=0;i<10;i++){

    document.querySelectorAll('div.quantumWizTogglePaperradioRadioContainer')[get_random(loc[i])].click();
    
console.log(i)

}"""
#There are majorly two types of radio buttons naming ....one is in js1 other is in js2.....basic understandin of js and python will help you understand the code 


for i in range(20):

    try:

        driver.execute_script(js1)

        driver.find_element_by_class_name('appsMaterialWizButtonPaperbuttonContent').click()

    except:

        driver.execute_script(js2)

        driver.find_element_by_class_name('appsMaterialWizButtonPaperbuttonContent').click()

    finally:

        driver.get('form_url_for_multiple_records')

