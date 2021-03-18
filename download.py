from datetime import time
import os
import ghost
import lxml
import requests
import urllib.parse
from bs4 import BeautifulSoup
# import ghost
import lxml.html
import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from msedge.selenium_tools import Edge, EdgeOptions
from time import sleep
import wget

username = "LCU2018205700"
password = "gyc123456"

getVideo = 0

auth = "eyJhbGciOiJIUzUxMiJ9.eyJyZnQiOmZhbHNlLCJqdGkiOiJkNDIxMjZjN2UxMmM0ZDcyODcxMzhhYzRiZjI5YzIwMSIsImlzcyI6ImF1dGgiLCJzdWIiOiJhYzZkZmIxMzIxYjg0M2FjODM1ODZlNmM5OTEwMjYzOCIsImF1ZCI6WyIqIl0sImlhdCI6MTYxNTI1NTc5MCwibmJmIjoxNjE1MjU1NzkwLCJleHAiOjE2MTc4NDc3OTAsImFleCI6MCwicG1zIjp7ImV4YW0iOjQ2LCJiaWdkYXRhIjo5ODk1ODgxNzQ1NTUwLCJhdHRhY2htZW50Ijo0NjExNjg2MDE4NDI3Mzg3OTA2LCJjb3Vyc2UiOjY4NzE5NTcwMzU4LCJncmFkIjoxNTM4LCJiYXNlIjo2Njk0ODAyMn0sIm1hbiI6eyJhY2NvdW50SWQiOiJhYzZkZmIxMzIxYjg0M2FjODM1ODZlNmM5OTEwMjYzOCIsImFjY291bnQiOiJMQ1UyMDE4MjA1NzAwIiwibW9iaWxlIjoiMTk4NjE5MDg4MjgiLCJjYWxsaW5nQ29kZSI6Iis4NiIsIm1lbWJlcklkIjoiZTI4NTljMjYzNjcxMTFlOTgyMTJmYTE2M2VmNWJhOGEiLCJuYW1lIjoi6auY5a6H6L6wIiwic2V4IjoiTWFuIiwicG9ydHJhaXQiOiJodHRwczovL3N0YXRpY2ZpbGUuZWVjLWNuLmNvbS9kZWZhdWx0L3RlYWNoZXItbWFuLWhlYWQucG5nIiwidHlwZSI6IlN0dWRlbnQifSwib3JnIjp7InNjaG9vbElkIjoiZmY4MDgwODE2MjRkMmQ2ZjAxNjI2MTQwNmQ1ZTBlNjkiLCJzY2hvb2xDb2RlIjoiTENVIiwic2Nob29sTmFtZSI6IuiBiuWfjuWkp-WtpiIsImNvbGxlZ2VJZCI6ImZmODA4MDgxNjI0ZDJkNmYwMTYyNjE1NzViNDUwZjg3IiwiY29sbGVnZUNvZGUiOiJMQ1UtQzAwMiIsImNvbGxlZ2VOYW1lIjoi6K6h566X5py65a2m6ZmiIiwibWFqb3JJZCI6IjE5NTY5YWM0NGVlYjExZWE4OGZlZmExNjNlZjViYThhIiwibWFqb3JDb2RlIjoiTENVLUMwMDItUzAwNSIsIm1ham9yTmFtZSI6Iui9r-S7tuW3peeoiyIsImNsYXNzcmFkZUlkIjoiOGViMmIyNGM0ZWVkMTFlYTg4ZmVmYTE2M2VmNWJhOGEiLCJjbGFzc3JhZGVDb2RlIjoiTENVLUMwMDItUzAwNS0yMDE4LTE3MjAxODIwOSIsImNsYXNzcmFkZU5hbWUiOiIyMDE457qn6L2v5Lu25bel56iLMTcyMDE4MjA554-tIn19.y-Yb78ZvsMNyOpIoEkrIbW9gWs_wR0r-fTQl-6pqArtwY7N8Xvk9fyddhv_gdnx3yquwAAttunbz7HhXO80yaQ"

access_key_id = '1PG60VBB4MWJWS139PTB'
expires = '1615953485'
signature = 'xPrcPJN82P3TOXZUAO61k30A6S0%3D'
# "https%3A%2F%2Fprivatefile.eec-cn.com%2F402880c077d38edf0177dc109246703b%2Fcourseware%2Fa080d49237e3406f8ce4f6f6813e0f5f.docx%3FAccessKeyId%3D1PG60VBB4MWJWS139PTB%26Expires%3D1615892375%26response-content-disposition%3Dinline%253B%2Bfilename*%2B%253D%2BUTF-8%2527%252720210303-PM-%2525E8%2525AF%2525BE%2525E5%2525A0%252582%2525E7%2525AC%252594%2525E8%2525AE%2525B0.docx%26Signature%3Dn0p%252FIssIgRIEwAOstp4ikRQ%252BDiE%253D"
base_url = "https://www.eec-cn.com/api"
headers = {
    'Host': 'www.eec-cn.com',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'Authentication': auth,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.eec-cn.com/u/ordCou/4028804277b8a7530177cc989b3514f2/1/teachClassStudent',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-HK;q=0.8',
    # 'Cookie': 'UM_distinctid=177f171ee078de-05e64fe5e6e147-7a667166-144000-177f171ee0855d; Hm_lvt_b3449bd91e10abed98f17f713d67e11b=1615695793,1615770329,1615796733,1615861853; CNZZDATA1279392396=1158029126-1614661485-%7C1615877658; Hm_lpvt_b3449bd91e10abed98f17f713d67e11b=1615878142'
}
file_base_url = "https://privatefile.eec-cn.com"
file_list = []

course_name ='tmp'

def getAllCourses():
    # All Courses
    course_url = base_url + "/course/courses/joinedCourses?type=3"

    try:
        course_data = requests.get(course_url, headers=headers).json()['data']
        course_list = course_data['fieldList']
    except TypeError:
        print("课程列表获取失败！")
        print(requests.get(course_url, headers=headers).json())
        course_list = ''
    finally:
        return course_list


def getCourseChapter(requested_course, course_list):
    course_info = course_list[requested_course]
    course_id = course_info['id']
    course_name = course_info['name']
    print(course_name)
    isExists = os.path.exists(course_name)
    if not isExists:
        os.makedirs(course_name)
    content_url = base_url + "/course/chapters/byCourse?courseId=" + course_id
    try:
        content_data = requests.get(content_url, headers=headers).json()['data']
    except TypeError or KeyError:
        print("章节信息获取失败！")
        print(requests.get(content_url, headers=headers).json())
    finally:
        content_list = content_data['fieldList']
        # print(content_list)
        return content_list

def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        os.makedirs(path)
        print(path + ' 创建成功')
    else:
        print(path + ' 目录已存在')
    return True


def getCourseContent(layer, layer_name, content_list):
    for item in content_list:
        for i in range(layer):
            print("\t", end="")
        print(item['name'])
        this_layer_name = layer_name + '\\' + item['name']
        if item['isLeaf'] == 0:
            mkdir(this_layer_name)
            getCourseContent(layer + 1, this_layer_name, item['children'])
        else:
            res_id = item['id']
            res_url = base_url + '/course/chapters/' + res_id + '/resources'
            # try:
            res_data = requests.get(res_url, headers=headers).json()['data'][0]
            file_id = res_data['id']
            file_attachment_id = res_data['attachmentId']
            file_type = res_data['attachmentDTO']['type']
            file_preview_url = "https://www.eec-cn.com/preView/" + file_attachment_id + "/1/" + file_id + "/1?userType=0"
            try:
                browser.get(file_preview_url)
                sleep(1)
                input_first = browser.find_element_by_css_selector('body > div.qst-app-container > div.qst-tecs-src-onlineOreview-preview_ > div > div.qst-tecs-src-onlineOreview-preview__office-container > div > iframe')
                file_url = input_first.get_attribute("src")
                for i in range(layer):
                    print("\t", end="")
                file_url = urllib.parse.unquote(file_url[50:])
                print("下载至:"+this_layer_name)
                wget.download(file_url, this_layer_name + "."+file_type)
                # if getVideo == 1:
                #     file_list.append(file_url)
                # elif getVideo == 2:
                #     if res_data[0]['attachmentDTO']['type'] == 'mp4':
                #         file_list.append(file_url)
                # else:
                #     if res_data[0]['attachmentDTO']['type'] != 'mp4':
                #         file_list.append(file_url)

                file_list.append(file_url)
            except NoSuchElementException:
                print(NoSuchElementException)
            # except (TypeError, KeyError):
            #     print("叶子节点内容获取失败")
            #     print(requests.get(res_url, headers=headers).json())
                # file_name = urllib.parse.quote_plus(res_data['attachmentDTO']['originFileName'])
                # response_content_disposition = 'inline%3B+filename*+%3D+UTF-8%27%27' + file_name
                # dt = '?AccessKeyId=' + access_key_id + '&Expires=' + expires + '&response-content-disposition=' + response_content_disposition + '&Signature=' + signature
                # file_url = res_data['attachmentDTO']['url'] + dt

                # res_url = file_base_url + res_data['attachmentDTO']['filePath']





# File

# others = "/"+course_template_id+"/courseware/6837174DA632426CA263995D56299A49.pptx?AccessKeyId=1PG60VBB4MWJWS139PTB&Expires=1615879187&response-content-disposition=inline%3B+filename*+%3D+UTF-8%27%2701_Internet%25E8%25B5%25B7%25E6%25BA%2590%25E4%25B8%258EHTML%25E6%25A6%2582%25E8%25BF%25B0.pptx&Signature=K0xNhWO2DpNBlQ05ZKmiWo3btmk%3D"
if __name__ == '__main__':
    driver_url = './edgedriver_win64/msedgedriver.exe'
    options = EdgeOptions()
    options.use_chromium = True
    browser = Edge(options=options, executable_path=driver_url)

    browser.get("https://www.eec-cn.com/student/group")

    browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[4]/div[1]/input").send_keys(username)
    browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[4]/div[2]/input").send_keys(password)
    browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[4]/div[4]").click()
    sleep(5)

    auth = browser.execute_script('return localStorage.getItem("crossToken");')

    choice = input("是否下载视频？(Y:全部, N:不下载视频, O:只下载视频)")
    if choice == 'Y':
        getVideo = 1
    elif choice == 'N':
        getVideo = 0
    elif choice == 'n':
        getVideo = 0
    elif choice == 'O':
        getVideo = 2
    elif choice == 'o':
        getVideo = 2
    else:
        getVideo = 0

    course_list = getAllCourses()
    iterator = 1
    for item in course_list:
        print(str(iterator) + ". " + item['name'])
        iterator += 1
    while 1:
        requested_course = int(input("输入希望下载课程的编号:"))
        if requested_course >= 0 and requested_course <= len(course_list):
            requested_course -= 1
            content_list = getCourseChapter(requested_course, course_list)
            getCourseContent(0, '' + course_name, content_list)
            # with open(course_list[requested_course]['name'] + '.txt', mode='x') as file:
            #     for item in file_list:
            #         file.write(item + '\n')
        else:
            print("请重新输入")
