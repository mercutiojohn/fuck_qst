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

username = ""
password = ""

getVideo = 0

auth = ""

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

# course_name ='tmp'

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
    global course_name
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
            try:
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
                    file_url = urllib.parse.unquote(file_url[50:])
                    file_path = this_layer_name + "." + file_type

                    if getVideo == 1:
                        file_list.append([
                            file_path,
                            file_url
                        ])
                    elif getVideo == 2:
                        if file_type == 'mp4':
                            file_list.append([
                                file_path,
                                file_url
                            ])
                    else:
                        if file_type != 'mp4':
                            file_list.append([
                                file_path,
                                file_url
                            ])

                except NoSuchElementException:
                    print(NoSuchElementException)
            except (TypeError, KeyError):
                print("叶子节点内容获取失败")
                print(requests.get(res_url, headers=headers).json())





if __name__ == '__main__':
    username = input("输入用户名：")
    password = input("输入密码：")

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
    while 1:
        file_list = []
        course_list = getAllCourses()
        iterator = 1
        for item in course_list:
            print(str(iterator) + ". " + item['name'])
            iterator += 1
        requested_course = int(input("输入希望下载课程的编号:"))
        if requested_course >= 0 and requested_course <= len(course_list):
            requested_course -= 1
            content_list = getCourseChapter(requested_course, course_list)
            getCourseContent(0, '' + course_name, content_list)
            for item in file_list:

                print("下载至:" + item[0])
                try:
                    tmp = requests.get(item[1])
                    # file_list.remove({item[0], item[1]})
                    open(item[0], 'wb').write(tmp.content)
                except requests.exceptions.ConnectionError:
                    file_list.append({
                        item[0],
                        item[1]
                    })
                    print("尝试在队末重新下载")

            # with open(course_list[requested_course]['name'] + '.txt', mode='x') as file:
            #     for item in file_list:
            #         file.write(item + '\n')
        else:
            print("请重新输入")
