import requests
from bs4 import BeautifulSoup

login_url_str = 'http://202.113.5.137/stuslls/login/login!login'
class_url_str = 'http://202.113.5.137/stuslls/course/course!selectedCourse'

session = requests.session()

params = {'loginBean.username': 'your user name',
          'loginBean.password': 'your password'}

session.post(login_url_str, params)

context = BeautifulSoup(session.get(class_url_str).text, 'lxml')
class_infos = context.find_all('tr', attrs={'bgcolor': '#FFFFFF'})
class_infos = [i.find_all('td') for i in class_infos]

class_order_dict = {'上课时间': 6, '课程名称': 3}

infos = [{'课程名称': ' '.join(class_info[class_order_dict['课程名称']].text.split()),
          '上课时间': ' '.join(class_info[class_order_dict['上课时间']].text.split())} for class_info in class_infos]

print(infos)
