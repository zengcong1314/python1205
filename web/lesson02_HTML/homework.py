from selenium import webdriver

def test_login():
    driver = webdriver.Chrome()
    url = 'http://localhost:63342/python36/lesson02_HTML/login.html?_ijt=fnsjf389n1erjuqhbkr87jm5vj'
    driver.get(url)

    elem_user = driver.find_element_by_xpath('/html/body/div[1]/input[1]')
    elem_pwd = driver.find_element_by_xpath('/html/body/div[1]/input[2]')
    print(elem_user)
    print(elem_pwd)



