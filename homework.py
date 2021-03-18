import datetime
import time
from string import Template

import requests

auth = "eyJhbGciOiJIUzUxMiJ9.eyJyZnQiOmZhbHNlLCJqdGkiOiJkNDIxMjZjN2UxMmM0ZDcyODcxMzhhYzRiZjI5YzIwMSIsImlzcyI6ImF1dGgiLCJzdWIiOiJhYzZkZmIxMzIxYjg0M2FjODM1ODZlNmM5OTEwMjYzOCIsImF1ZCI6WyIqIl0sImlhdCI6MTYxNTI1NTc5MCwibmJmIjoxNjE1MjU1NzkwLCJleHAiOjE2MTc4NDc3OTAsImFleCI6MCwicG1zIjp7ImV4YW0iOjQ2LCJiaWdkYXRhIjo5ODk1ODgxNzQ1NTUwLCJhdHRhY2htZW50Ijo0NjExNjg2MDE4NDI3Mzg3OTA2LCJjb3Vyc2UiOjY4NzE5NTcwMzU4LCJncmFkIjoxNTM4LCJiYXNlIjo2Njk0ODAyMn0sIm1hbiI6eyJhY2NvdW50SWQiOiJhYzZkZmIxMzIxYjg0M2FjODM1ODZlNmM5OTEwMjYzOCIsImFjY291bnQiOiJMQ1UyMDE4MjA1NzAwIiwibW9iaWxlIjoiMTk4NjE5MDg4MjgiLCJjYWxsaW5nQ29kZSI6Iis4NiIsIm1lbWJlcklkIjoiZTI4NTljMjYzNjcxMTFlOTgyMTJmYTE2M2VmNWJhOGEiLCJuYW1lIjoi6auY5a6H6L6wIiwic2V4IjoiTWFuIiwicG9ydHJhaXQiOiJodHRwczovL3N0YXRpY2ZpbGUuZWVjLWNuLmNvbS9kZWZhdWx0L3RlYWNoZXItbWFuLWhlYWQucG5nIiwidHlwZSI6IlN0dWRlbnQifSwib3JnIjp7InNjaG9vbElkIjoiZmY4MDgwODE2MjRkMmQ2ZjAxNjI2MTQwNmQ1ZTBlNjkiLCJzY2hvb2xDb2RlIjoiTENVIiwic2Nob29sTmFtZSI6IuiBiuWfjuWkp-WtpiIsImNvbGxlZ2VJZCI6ImZmODA4MDgxNjI0ZDJkNmYwMTYyNjE1NzViNDUwZjg3IiwiY29sbGVnZUNvZGUiOiJMQ1UtQzAwMiIsImNvbGxlZ2VOYW1lIjoi6K6h566X5py65a2m6ZmiIiwibWFqb3JJZCI6IjE5NTY5YWM0NGVlYjExZWE4OGZlZmExNjNlZjViYThhIiwibWFqb3JDb2RlIjoiTENVLUMwMDItUzAwNSIsIm1ham9yTmFtZSI6Iui9r-S7tuW3peeoiyIsImNsYXNzcmFkZUlkIjoiOGViMmIyNGM0ZWVkMTFlYTg4ZmVmYTE2M2VmNWJhOGEiLCJjbGFzc3JhZGVDb2RlIjoiTENVLUMwMDItUzAwNS0yMDE4LTE3MjAxODIwOSIsImNsYXNzcmFkZU5hbWUiOiIyMDE457qn6L2v5Lu25bel56iLMTcyMDE4MjA554-tIn19.y-Yb78ZvsMNyOpIoEkrIbW9gWs_wR0r-fTQl-6pqArtwY7N8Xvk9fyddhv_gdnx3yquwAAttunbz7HhXO80yaQ"
cookie = 'UM_distinctid=177f171ee078de-05e64fe5e6e147-7a667166-144000-177f171ee0855d; Hm_lvt_b3449bd91e10abed98f17f713d67e11b=1615695793,1615770329,1615796733,1615861853; CNZZDATA1279392396=1158029126-1614661485-%7C1615877658; Hm_lpvt_b3449bd91e10abed98f17f713d67e11b=1615878142'
base_url = "https://www.eec-cn.com"
api_url = base_url + "/api"
headers = {
    'Host': 'www.eec-cn.com',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'Authentication': auth,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': base_url + '/u/ordCou/4028804277b8a7530177cc989b3514f2/1/teachClassStudent',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-HK;q=0.8',
    'Cookie': cookie
}
file_base_url = "https://privatefile.eec-cn.com"


def getAllCourses():
    # All Courses
    course_url = api_url + "/course/courses/joinedCourses?type=3"

    try:
        course_data = requests.get(course_url, headers=headers).json()['data']
    except TypeError:
        print("获取失败")
        print(requests.get(course_url, headers=headers).json())
    finally:
        course_list = course_data['fieldList']
        return course_list


def getExpContent(requested_course, course_list):
    exp_content_url = '/course/courseTestcases/byStudent?courseId='
    return getCourseContent(requested_course, course_list, exp_content_url)


def getHmwkContent(requested_course, course_list):
    hmwk_content_url = "/course/homeworks/student?courseId="
    return getCourseContent(requested_course, course_list, hmwk_content_url)


def getCourseContent(requested_course, course_list, content_url):
    course_info = course_list[requested_course]
    course_id = course_info['id']
    course_name = course_info['name']
    request_url = api_url + content_url + course_id
    try:
        content_data = requests.get(request_url, headers=headers).json()['data']
    except TypeError:
        print("获取失败")
        print(requests.get(request_url, headers=headers).json())
    finally:
        content_list = content_data['fieldList']
        return content_list


class DeltaTemplate(Template):
    delimiter = '%'


def strfdelta(tdelta, fmt):
    d = {}
    l = {'D': 86400, 'H': 3600, 'M': 60, 'S': 1}
    rem = int(tdelta.total_seconds())

    for k in ('D', 'H', 'M', 'S'):
        if "%{}".format(k) in fmt:
            d[k], rem = divmod(rem, l[k])

    t = DeltaTemplate(fmt)
    return t.substitute(**d)


def showHomeworkInfo(content_list):
    fmt_time = datetime.datetime.now()
    unix_time = time.mktime(fmt_time.timetuple())
    for item in content_list:
        title = item['name']
        unix_end_time = item['endTime']
        fmt_end_time = datetime.datetime.fromtimestamp(unix_end_time)
        fmt_countdown = fmt_end_time - fmt_time
        homework_url = 'https://www.eec-cn.com/workAnswer/' + item['courseId'] + '/' + item[
            'id'] + '/true?isPiYue=noPiYue'
        if item['subStatus'] or item['submitTask'] == 1:
            print(end='')
            # print("\t", "[作业]", end="")
            # if str(fmt_countdown).startswith('-'):
            #     print('已截止', end=" ")
            # else:
            #     print(strfdelta(fmt_countdown, "%D天%H小时%M分"),
            #           time.strftime("%m月%d日 %H:%M", fmt_end_time.timetuple()), end=" ")
            # print(title)
        else:
            print("\t", "[作业]", end="")
            # print("(未提交)", end="")
            if str(fmt_countdown).startswith('-'):
                print('已截止', end=" ")
            else:
                print(strfdelta(fmt_countdown, "%D天%H小时%M分"),
                      time.strftime("%m月%d日 %H:%M", fmt_end_time.timetuple()), end=" ")
            print(title, homework_url)


def showExperimentsInfo(content_list, course_id):
    fmt_time = datetime.datetime.now()
    unix_time = time.mktime(fmt_time.timetuple())
    for item in content_list:
        id = item['id']
        title = item['name']
        detail_url = api_url + '/course/testcaseReports/byStudent?testcaseId=' + id
        detail_data = {}
        try:
            detail_data = requests.get(detail_url, headers=headers).json()['data']
        except TypeError:
            print("获取失败")
            print(requests.get(detail_url, headers=headers).json())
        finally:
            unix_end_time = detail_data['submitTime']
            fmt_end_time = datetime.datetime.fromtimestamp(unix_end_time)
            fmt_countdown = fmt_end_time - fmt_time
            homework_url = 'https://www.eec-cn.com/u/ordCou/' + course_id + '/1/generalExperimentStu/generalTestDetail/' + id + '/' + \
                           detail_data['attachmentId']
        if str(fmt_countdown).startswith('-'):
            print(end='')
            # print('已截止', end=" ")
            # print(title, homework_url)
        else:
            print("\t", "[实验]", end="")
            print(strfdelta(fmt_countdown, "%D天%H小时%M分"),
                  time.strftime("%m月%d日 %H:%M", fmt_end_time.timetuple()), end=" ")
            print(title, homework_url)


if __name__ == '__main__':
    course_list = getAllCourses()
    iterator = 0
    for item in course_list:
        course_id = item['id']
        print(item['name'])
        iterator += 1
        requested_course = iterator
        requested_course -= 1
        hmwk_content_list = getHmwkContent(requested_course, course_list)
        exp_content_list = getExpContent(requested_course, course_list)

        showHomeworkInfo(hmwk_content_list)
        showExperimentsInfo(exp_content_list, course_id)
