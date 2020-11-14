from selenium import webdriver
from lxml import etree
import csv
import pymysql
import time
import json


url = 'http://account.for-test.cn/login.php'

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get(url)

driver.find_element_by_name('email').send_keys('328504342@qq.com')
driver.find_element_by_name('pass').send_keys('jay13403630587')
driver.find_element_by_name('submit').click()

for i in range(1,91):
    driver.get('http://account.for-test.cn/jlptshitidata.php?shitibiaoming=t_30&tihao={}&shitibiao=30&yanzheng=1&yshipin=&jinru=0'.format(i))
    req = driver.page_source
    # print(req)
    # print(type(html))
    html = etree.HTML(req)
    # print(type(html))

    qes = html.xpath("//div[@class='jumbotron']/p//text()")

    qes = ''.join(qes)

    selector = html.xpath("//div[@class='jumbotron']/label/span/text()")

    a = selector[0]
    b = selector[1]
    c = selector[2]
    d = selector[3]

    ans = html.xpath("//p/span[@class='con']/text()")[-2]

    jiexi = html.xpath("//span[@class='con']/p/text()")
    jiexi = ''.join(jiexi)

    info = html.xpath("//p/span[@class='con']/text()")[-1]

    print(qes)
    print(a,b,c,d,ans)
    print(jiexi,type(jiexi))

    db = pymysql.connect(host='192.168.1.239',user='root',password='930825',db='jlptoline',port=3306)
    cursor = db.cursor()

    sql = "INSERT INTO TIKU30(QES,A,B,C,D,ANS,JIEXI,INFO) \
            VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (qes,a,b,c,d,ans,jiexi,info)
    try:
        cursor.execute(sql)
        db.commit()
        print("执行成功")

    except:
        db.rollback()
        print("执行失败")

    db.close()

    # with open('tiku67.csv','a',newline='',encoding='utf-8-sig') as f:
    #     writer = csv.writer(f)
    #     writer.writerow([qes,a,b,c,d,ans,jiexi])



