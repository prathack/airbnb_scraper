from selenium import webdriver
import csv
def intro():
    print("""*****Airbnb Web Scraper 1.0 by prathack *****
                          Author : Prathap
                      FacebookID : prathack
                      Website    : pythongui.com
    """)
    print(""" Python3 Modules need to be Installed :
                 1.selenium
                 2.chrome web driver
                 3.csv """)
    print(""" Ussage:
                 1.Open Airbnb and type any place in search bar
                 2***.Copy and paste the results url which has offset parameter value is empty
                 3.Ex: https://www.airbnb.co.in/s/sukhumvit/homes?allow_override%5B%5D=&s_tag=SPeAs5nW&section_offset=
    """)
    

    
    
def scraper(url):
    f = int(input("Enter From page: "))
    t = int(input("Enter To page: "))
    with open('airbnb.csv', 'w') as csvfile:
        fieldnames = ['Title', 'Price','Beds','RoomType']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        cpath = r"C:\Python34\chromedriver.exe"
        driver = webdriver.Chrome(cpath)
        for k in range(f,t):
            driver.get(url+str(k))
            source = driver.find_elements_by_tag_name('div')
            for i in source:
                
                value = i.get_attribute('id')
                if ("list" in value):
                    
                    try:
                        title = driver.find_element_by_xpath('//*[@id="'+str(value)+'"]/div[2]/a/div[1]/span/span').text
                        prices = driver.find_element_by_xpath('//*[@id="'+str(value)+'"]/div[2]/a/div[1]/div/span[1]/span[1]/span[2]').text
                        beds = driver.find_element_by_xpath('//*[@id="'+str(value)+'"]/div[2]/a/div[2]/span[2]/span[2]/span').text
                        roomtype = driver.find_element_by_xpath('//*[@id="'+str(value)+'"]/div[2]/a/div[2]/span[1]/span').text
                    
                        price = prices[1:]
                    
                        writer.writerow({'Title': title, 'Price': price,'Beds': beds ,'RoomType': roomtype })
                    except :
                        pass

intro()
url = input("Enter URL to scrape: ")

scraper(url)
