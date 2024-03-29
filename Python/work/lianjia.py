import requests
import time 
import re
from lxml import etree

# 获取某市区域的所有连接
def get_areas(url):
    print('start grabing areas')
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}
    response = requests.get(url, headers=headers)
    content = etree.HTML(response.text)
    areas = content.xpath("/html/body/div[3]/div[1]/div[3]/h1/a") 
    print(areas)
    # areas_link = content.xpath("//dd[@data-index = '0']//div[@class='option-list']/a/@href") 
    for i in range(1,len(areas)): 
        area = areas[i] 
        area_link = areas[i] 
        link = 'https://bj.lianjia.com' + area_link 
        print("开始抓取页面") 
        get_pages(area, link) 
 
#通过获取某一区域的页数，来拼接某一页的链接 
def get_pages(area,area_link): 
    headers = { 
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'} 
    resposne = requests.get(area_link, headers=headers) 
    pages =  int(re.findall("page-data=\'{\"totalPage\":(\d+),\"curPage\"", resposne.text)[0]) 
    print("这个区域有" + str(pages) + "页") 
    for page in range(1,pages+1): 
        url = 'https://bj.lianjia.com/zufang/dongcheng/pg' + str(page) 
        print("开始抓取" + str(page) +"的信息") 
        get_house_info(area,url) 
 
#获取某一区域某一页的详细房租信息 
def get_house_info(area, url): 
    headers = { 
       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'} 
    time.sleep(2) 
    try: 
        resposne = requests.get(url, headers=headers) 
        content = etree.HTML(resposne.text) 
        info=[] 
        for i in range(30): 
            title = content.xpath("//div[@class='where']/a/span/text()")[i] 
            room_type = content.xpath("//div[@class='where']/span[1]/span/text()")[i] 
            square = re.findall("(\d+)",content.xpath("//div[@class='where']/span[2]/text()")[i])[0] 
            position = content.xpath("//div[@class='where']/span[3]/text()")[i].replace(" ", "") 
            try: 
                detail_place = re.findall("([\u4E00-\u9FA5]+)租房", content.xpath("//div[@class='other']/div/a/text()")[i])[0] 
            except Exception as e: 
                detail_place = "" 
            floor =re.findall("([\u4E00-\u9FA5]+)\(", content.xpath("//div[@class='other']/div/text()[1]")[i])[0] 
            total_floor = re.findall("(\d+)",content.xpath("//div[@class='other']/div/text()[1]")[i])[0] 
            try: 
                house_year = re.findall("(\d+)",content.xpath("//div[@class='other']/div/text()[2]")[i])[0] 
            except Exception as e: 
                house_year = "" 
            price = content.xpath("//div[@class='col-3']/div/span/text()")[i] 
            with open('链家北京租房.txt','a',encoding='utf-8') as f: 
                f.write(area + ',' + title + ',' + room_type + ',' + square + ',' +position+ 
','+ detail_place+','+floor+','+total_floor+','+price+','+house_year+'\n') 
 
            print('writing work has done!continue the next page') 
 
    except Exception as e: 
        print( 'ooops! connecting error, retrying.....') 
        time.sleep(20) 
        return get_house_info(area, url) 
 
 
def main(): 
    print('start!') 
    url = 'https://bj.lianjia.com/zufang' 
    get_areas(url) 
 
 
if __name__ == '__main__': 
    main() 