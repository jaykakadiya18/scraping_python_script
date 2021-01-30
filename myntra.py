'''All Outputs are Print in the program.
Modules use selenium, time and web driver
line no.10 & 34 (put your chrome driver's path)'''

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

url = "https://www.myntra.com/dresses?f=Gender%3Amen%20women%2Cwomen&plaEnabled=false"

links = []
driver = webdriver.Chrome("D:\chromedriver")
driver.get(url)
p=0
l=len(url)
for loops in range(4): #Collect 200 products links

    time.sleep(2)
    for product_base in driver.find_elements_by_class_name('product-base'):

        links.append(product_base.find_element_by_xpath('./a').get_attribute("href"))
    p=p+1

    action = ActionChains(driver)
    action.move_to_element(driver.find_element_by_class_name('pagination-next')).perform()
    action.click().perform()

    time.sleep(2)
driver.close()
print(links)
print("Total product link is 200 but duplicate links are deleted than total number og links: " + str(len(set(links))))

c=0
while(c<len(links)+1):
    for link in links: #open every product page
        driver = webdriver.Chrome("D:\chromedriver")
        driver.get(link)
        action = ActionChains(driver)
        action.move_to_element(driver.find_element_by_class_name(
            'index-showMoreText')).perform()
        action.click().perform()
        print("Product Number{}".format(c+1))
        p = 1
        for lin in driver.find_elements_by_class_name('image-grid-imageContainer'):
            try:
                imgl = lin.find_element_by_xpath('./div'.format(p)).get_attribute('style').replace(
                    'background-image: url("', '').replace('");', '')
                p += 1
                print(imgl)
            except:
                print(link)


        spe2 = driver.find_element_by_class_name('pdp-productDescriptorsContainer').text

        ##json method
        
        # pri = driver.find_element_by_xpath("/html/body/script[3]").get_attribute('innerHTML').replace("u002F","").replace("window.__myx = ","")
        # x = pri.split(",") 
        # y = x[1:-1]
        # lst = y[0].split(':')
        # print(lst)
        # res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst),2)}
        # print(res_dct['"name"'])


        print(spe2)
        print("--------------------------------------------------------------------")
        driver.close()
        c+=1


