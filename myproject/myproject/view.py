from django.http import HttpResponse
from django.shortcuts import render
import sqlite3

dict = {"0":"Description", "1":"ItemNumber", "2":"Price", "3":"Available",
        "4":"Description", "5":"ItemNumber", "6":"Price", "7":"Available"  }

dict1 = {"0":"productline", "1":"OrderNumber", "2":"sales", "3":"quantityordered",
        "4":"productline", "5":"OrderNumber", "6":"sales", "7":"quantityordered"  }
def hello(request):
    context = {}
    context['hello'] = 'new page!!!!'
    context['dudu'] = 'smaller new page!!!!'
    context['decision'] = False
    context['list'] = {'a':'a', 'b':'b'}
    return render(request, 'hello.html', context)

def items(request):
    if 'page' in request.GET:
        page = int(request.GET['page'])
    else:
        page = 0
    if 'limit' in request.GET:
        limit = request.GET['limit']
    else:
        limit = "5"
    if 'sortby' in request.GET:
        sortby = request.GET['sortby']
    else:
        sortby = "0"
    if 'itemName' in request.GET:
        itemName = request.GET['itemName']
    else:
        itemName = ""
    connection = sqlite3.connect('./Parts.db')
    #kk = connection.execute("SELECT * FROM PRODUCTS")
    #return HttpResponse(kk)
    cursor = connection.cursor()
    dict = {"0": "Description", "1": "ItemNumber", "2": "Price", "3": "Available",
            "4": "Description", "5": "ItemNumber", "6": "Price", "7": "Available"}
    orderBy = dict[sortby]
    if sortby in ["0","1","2","3"]:
        is_asc = "ASC"
    else:
        is_asc = "DESC"
    sql = "SELECT * FROM PRODUCTS WHERE DESCRIPTION LIKE "+ "'" + str(itemName) + "%'" + " ORDER BY "+ orderBy + " "+is_asc + " LIMIT " + str(limit) + " OFFSET " + str(page)
    cursor.execute(sql)
    result = cursor.fetchall()
    sql1 = "SELECT count(*) FROM PRODUCTS WHERE DESCRIPTION LIKE "+ "'" + str(itemName) + "%'"
    cursor1 = connection.cursor()
    cursor1.execute(sql1)
    countNum = cursor1.fetchall()
    connection.commit()
    connection.close()
    totalPage = countNum[0][0]//int(limit) + 1
    context = {}
    list = []
    for i in result:
        item = {}
        item['id'] = i[0]
        item['description'] = i[1]
        item['price'] = i[2]
        item['quantity'] = i[3]
        item['class'] = i[4]
        item['origin'] = i[5]
        item['leadTime'] = i[6]
        list.append(item)
    context['items'] = list
    enen = result[0][0]
    context['enen'] = enen
    context['kk'] = sql
    first_index = page * int(limit) + 1
    last_index = (page+1) *int(limit)
    context['firstIndex'] = first_index
    context['lastIndex'] = last_index
    context['limit'] = limit
    context['sortNumber'] = sortby
    pages = []
    for page in range(totalPage - 1):
        pages.append(page)
    context['totalPage'] = pages
    context['totalPageNumber'] = totalPage - 2
    context['totalPageNumber1'] = totalPage - 3
    return render(request, 'Items.html', context)


def search(request):
    if 'page' in request.GET:
        page = int(request.GET['page'])
    else:
        page = 0
    if 'limit' in request.GET:
        limit = request.GET['limit']
    else:
        limit = "5"
    if 'sortby' in request.GET:
        sortby = request.GET['sortby']
    else:
        sortby = "0"
    if 'itemName' in request.GET:
        itemName = request.GET['itemName']
    else:
        itemName = ""
    connection = sqlite3.connect('./Parts.db')
    #kk = connection.execute("SELECT * FROM PRODUCTS")
    #return HttpResponse(kk)

    cursor = connection.cursor()
    dict = {"0": "Description", "1": "ItemNumber", "2": "Price", "3": "Available",
            "4": "Description", "5": "ItemNumber", "6": "Price", "7": "Available"}
    orderBy = dict[sortby]
    if sortby in ["0","1","2","3"]:
        is_asc = "ASC"
    else:
        is_asc = "DESC"
    sql = "SELECT * FROM PRODUCTS WHERE DESCRIPTION LIKE "+ "'" + str(itemName) + "%'" + " ORDER BY "+ orderBy + " "+is_asc + " LIMIT " + str(limit) + " OFFSET " + str(page)
    cursor.execute(sql)
    result = cursor.fetchall()
    sql1 = "SELECT count(*) FROM PRODUCTS WHERE DESCRIPTION LIKE "+ "'" + str(itemName) + "%'"
    cursor1 = connection.cursor()
    cursor1.execute(sql1)
    countNum = cursor1.fetchall()
    connection.commit()
    connection.close()
    totalPage = countNum[0][0]//int(limit) + 1
    context = {}
    list = []
    for i in result:
        item = {}
        item['id'] = i[0]
        item['description'] = i[1]
        item['price'] = i[2]
        item['quantity'] = i[3]
        item['class'] = i[4]
        item['origin'] = i[5]
        item['leadTime'] = i[6]
        list.append(item)
    context['items'] = list
    enen = result[0][0]
    context['enen'] = enen
    context['kk'] = sql
    first_index = page * int(limit) + 1
    last_index = (page+1) *int(limit)
    context['firstIndex'] = first_index
    context['lastIndex'] = last_index
    context['limit'] = limit
    context['sortNumber'] = sortby
    pages = []
    for page in range(totalPage - 1):
        pages.append(page)
    context['totalPage'] = pages
    context['totalPageNumber'] = totalPage - 2
    context['totalPageNumber1'] = totalPage - 3
    return render(request, 'search.html', context)


def transaction(request):
    if 'page' in request.GET:
        page = int(request.GET['page'])
    else:
        page = 0
    if 'limit' in request.GET:
        limit = request.GET['limit']
    else:
        limit = "5"
    if 'sortby' in request.GET:
        sortby = request.GET['sortby']
    else:
        sortby = "0"
    if 'itemName' in request.GET:
        itemName = request.GET['itemName']
    else:
        itemName = ""
    connection = sqlite3.connect('./Parts.db')
    #kk = connection.execute("SELECT * FROM PRODUCTS")
    #return HttpResponse(kk)

    cursor = connection.cursor()
    dict = {"0": "productline", "1": "OrderNumber", "2": "sales", "3": "quantityordered",
             "4": "productline", "5": "OrderNumber", "6": "sales", "7": "quantityordered"}
    orderBy = dict[sortby]
    if sortby in ["0","1","2","3"]:
        is_asc = "ASC"
    else:
        is_asc = "DESC"
    sql = "SELECT * FROM TRANSACTIONSS WHERE PRODUCTLINE LIKE "+ "'" + str(itemName) + "%'" + " ORDER BY "+ orderBy + " "+is_asc + " LIMIT " + str(limit) + " OFFSET " + str(page)
    cursor.execute(sql)
    result = cursor.fetchall()
    sql1 = "SELECT count(*) FROM TRANSACTIONSS WHERE PRODUCTLINE LIKE "+ "'" + str(itemName) + "%'"
    cursor1 = connection.cursor()
    cursor1.execute(sql1)
    countNum = cursor1.fetchall()
    connection.commit()
    connection.close()
    totalPage = countNum[0][0]//int(limit) + 1
    context = {}
    list = []
    for i in result:
        item = {}
        item['id'] = i[0]
        item['quantity'] = i[1]
        item['price'] = i[2]
        item['pay'] = i[4]
        item['orderdate'] = i[5]
        item['status'] = i[6]
        item['product'] = i[10]
        item['customerName'] = i[13]
        item['phone'] = i[14]
        item['address'] = i[15]
        item['city'] = i[17]
        item['state'] = i[18]
        item['country'] = i[20]
        item['dealSize'] = i[24]
        list.append(item)
    context['items'] = list
    enen = result[0][0]
    context['enen'] = enen
    context['kk'] = sql
    first_index = page * int(limit) + 1
    last_index = (page+1) *int(limit)
    context['firstIndex'] = first_index
    context['lastIndex'] = last_index
    context['limit'] = limit
    context['sortNumber'] = sortby
    pages = []
    for page in range(totalPage - 1):
        pages.append(page)
    context['totalPage'] = pages
    context['totalPageNumber'] = totalPage - 2
    context['totalPageNumber1'] = totalPage - 3
    return render(request, 'Transaction.html', context)

import numpy as np

def addItem(request):
    print ('hello from addItem')
    itemName = request.POST.get('itemName', '')
    qis = request.POST.get('QIS', '')
    unitPrice = request.POST.get('unitPrice', '')
    class1 = request.POST.get('class', '')
    leadTime = request.POST.get('leadTime', '')
    origin = request.POST.get('origin', '')
    itemId = np.random.randint(999999)
    connection = sqlite3.connect('./Parts.db')
    cursor = connection.cursor()
    sql_command = "INSERT OR REPLACE INTO PRODUCTS (ItemNumber, Description, Price, Available, Class, Origin, Lead_Time)" + " VALUES ('" + str(itemId) +"', '" + itemName + "', '" + str(unitPrice) +"', '" + str(qis) + "', '" + class1 + "', '"+ origin + "', '" + leadTime + "'); "
    #print ('itemId '+str(itemId))
    #print ('itemName ' + itemName)

    cursor.execute(sql_command)
    connection.commit()
    connection.close()

    if 'page' in request.GET:
        page = int(request.GET['page'])
    else:
        page = 0
    if 'limit' in request.GET:
        limit = request.GET['limit']
    else:
        limit = "5"
    if 'sortby' in request.GET:
        sortby = request.GET['sortby']
    else:
        sortby = "0"
    if 'itemName' in request.GET:
        itemName = request.GET['itemName']
    else:
        itemName = ""
    connection = sqlite3.connect('./Parts.db')
    #kk = connection.execute("SELECT * FROM PRODUCTS")
    #return HttpResponse(kk)
    cursor = connection.cursor()
    dict = {"0": "Description", "1": "ItemNumber", "2": "Price", "3": "Available",
            "4": "Description", "5": "ItemNumber", "6": "Price", "7": "Available"}
    orderBy = dict[sortby]
    if sortby in ["0","1","2","3"]:
        is_asc = "ASC"
    else:
        is_asc = "DESC"
    sql = "SELECT * FROM PRODUCTS WHERE DESCRIPTION LIKE "+ "'" + str(itemName) + "%'" + " ORDER BY "+ orderBy + " "+is_asc + " LIMIT " + str(limit) + " OFFSET " + str(page)
    cursor.execute(sql)
    result = cursor.fetchall()
    sql1 = "SELECT count(*) FROM PRODUCTS WHERE DESCRIPTION LIKE "+ "'" + str(itemName) + "%'"
    cursor1 = connection.cursor()
    cursor1.execute(sql1)
    countNum = cursor1.fetchall()
    connection.commit()
    connection.close()
    totalPage = countNum[0][0]//int(limit) + 1
    context = {}
    list = []
    for i in result:
        item = {}
        item['id'] = i[0]
        item['description'] = i[1]
        item['price'] = i[2]
        item['quantity'] = i[3]
        item['class'] = i[4]
        item['origin'] = i[5]
        item['leadTime'] = i[6]
        list.append(item)
    context['items'] = list
    enen = result[0][0]
    context['enen'] = enen
    context['kk'] = sql
    first_index = page * int(limit) + 1
    last_index = (page+1) *int(limit)
    context['firstIndex'] = first_index
    context['lastIndex'] = last_index
    context['limit'] = limit
    context['sortNumber'] = sortby
    pages = []
    for page in range(totalPage - 1):
        pages.append(page)
    context['totalPage'] = pages
    context['totalPageNumber'] = totalPage - 2
    context['totalPageNumber1'] = totalPage - 3

    return render(request, 'Items.html', context)

def deleteItem(request):
    itemId = request.GET.get('itemId', '')
    #request.POST['itemId']
    connection = sqlite3.connect('./Parts.db')
    cursor = connection.cursor()
    #sql_command = "INSERT OR REPLACE INTO PRODUCTS (ItemNumber, Description, Price, Available, Class, Origin, Lead_Time)" + " VALUES ('" + str(itemId) +"', '" + itemName + "', " + str(unitPrice) +", " + str(qis) + ", '" + class1 + "', '"+ origin + "', '" + leadTime + "'); "
    sql_command = "DELETE FROM PRODUCTS WHERE ItemNumber = " +  str(itemId)
    cursor.execute(sql_command)
    connection.commit()
    connection.close()
    return None

def searchItem(request):
    itemName = request.GET.get('itemName', '')
    #request.POST['itemId']
    connection = sqlite3.connect('./Parts.db')
    cursor = connection.cursor()
    sql_command = "SELECT * FROM PRODUCTS WHERE Description = "  + itemName
    cursor.execute(sql_command)
    connection.commit()
    connection.close()
    return render(request, 'search.html', context)

def addTransaction(request):
    itemName = request.GET.get('itemName', '')
    qoo = request.GET.get('QOO', '')
    unitPrice = request.GET.get('unitPrice', '')
    pay = request.GET.get('pay', '')
    orderDate = request.GET.get('orderDate', '')
    status = request.GET.get('status', '')
    customerName = request.GET.get('customerName', '')
    phone = request.GET.get('phone', '')
    address = request.GET.get('address', '')
    city = request.GET.get('city', '')
    state = request.GET.get('state', '')
    country = request.GET.get('country', '')
    dealSize = request.GET.get('dealSize', '')
    itemId = np.random.randint(999999)
    connection = sqlite3.connect('./Parts.db')
    cursor = connection.cursor()
    sql_command = "INSERT OR REPLACE INTO TRANSACTIONSS (ORDERNUMBER, PRODUCTLINE, QUANTITYORDERED, PRICEEACH, SALES, ORDERDATE, STATUS, CUSTOMERNAME, PHONE, ADDRESSLINE1, CITY, STATE, COUNTRY, DEALSIZE)" + " VALUES ('" + str(itemId) +"', '" + itemName + "', '" + qoo +"', '" + unitPrice + "', '" + pay + "', '"+ orderDate + "', '" + status + "' , '" + customerName + "', '" + phone + "', '"+ address + "', '"+ city + "', '"+ state + "', '" + country + "', '"+ dealSize + "'); "
    cursor.execute(sql_command)
    connection.commit()
    connection.close()
    return transaction(request)

def deleteTransaction(request):
    print ('delete')
    print (str(itemId))
    itemId = request.GET.get('itemId', '')
    #request.POST['itemId']
    connection = sqlite3.connect('./Parts.db')
    cursor = connection.cursor()
    sql_command = "DELETE FROM TRANSACTIONSS WHERE ORDERNUMBER = " + str(itemId)
    cursor.execute(sql_command)
    connection.commit()
    connection.close()
    return transaction(request)

def verify(username, password):
    sql = "SELECT * FROM ACCOUNT WHERE account_name = " + "'" + str(username) + "' and " + " password = " + "'" + str(password) + "'"
    connection = sqlite3.connect('./Parts.db')
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    if len(result) == 0:
        return 0
    else:
        return 1

def name(username, password):
    sql = "SELECT * FROM ACCOUNT WHERE account_name = " + "'" + str(username) + "' and " + " password = " + "'" + str(password) + "'"
    connection = sqlite3.connect('./Parts.db')
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

def register(request,first=False):
  username = request.POST.get('username', '')
  password = request.POST.get('password', '')
  connection = sqlite3.connect('./Parts.db')
  cursor = connection.cursor()
  sql = "SELECT COUNT (*) FROM ACCOUNT"
  cursor.execute(sql)
  rowcount = cursor.fetchone()[0]
  print(rowcount)
  connection.close()
  return render(request, 'homepage.html', context)

usernameG = "User"
usernameGlobal = {}
def login_view(request,first=False):
  username = request.POST.get('username', '')
  password = request.POST.get('password', '')
  #if username == 'lizenan' and password == 'lizenan':
    #  user = 1
  #else:
      #user = 0
  user = verify(username, password)
  context = {}
  global usernameG 
  usernameG = username
  if user == 1:
    name1 = name(username, password)
    context['user'] = name1[0][3]
    global usernameGlobal
    usernameGlobal['user'] = name1[0][3]
    # Correct password, and the user is marked "active"
    # Redirect to a success page.
    print ('homeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
    print (context)
    return render(request, 'homepage.html', context)#("/account/loggedin/")
  else:
    # Show an error page
    if first:
        context['info'] = ""
    else:
        context['info'] = "your account or password is incorrect"
    return render(request, 'login.html', context)#HttpResponseRedirect("/account/invalid/")


def logout_view(request):
    context = {}
  # Redirect to a success page.
    return render(request, 'logout.html', context)#HttpResponseRedirect("/account/loggedout/")

def homepage(request):
    print ('hommmmmmmmmmmmmmmmmmmmeeeeeee')
    print (usernameGlobal)
    return render(request, 'homepage.html', usernameGlobal)

def home(request):
  # Redirect to a success page.
    return login_view(request,True)#HttpResponseRedirect("/account/loggedout/")


def bugs(request):
    if 'page' in request.GET:
        page = int(request.GET['page'])
    else:
        page = 0
    if 'limit' in request.GET:
        limit = request.GET['limit']
    else:
        limit = "5"
    connection = sqlite3.connect('./Parts.db')
    #kk = connection.execute("SELECT * FROM PRODUCTS")
    #return HttpResponse(kk)

    cursor = connection.cursor()
    sql = "SELECT * FROM BUGS LIMIT " + str(limit) + " OFFSET " + str(page)
    cursor.execute(sql)
    result = cursor.fetchall()
    sql1 = "SELECT count(*) FROM BUGS"
    cursor1 = connection.cursor()
    cursor1.execute(sql1)
    countNum = cursor1.fetchall()
    connection.commit()
    connection.close()
    totalPage = countNum[0][0]//int(limit) + 1
    context = {}
    list = []
    for i in result:
        item = {}
        item['id'] = i[0]
        item['description'] = i[1]
        item['reportDate'] = i[2]
        item['recorder'] = i[3]
        item['solution'] = i[4]
        item['fixer'] = i[5]
        item['fixedTime'] = i[6]
        list.append(item)
    context['items'] = list
    enen = result[0][0]
    context['enen'] = enen
    context['kk'] = sql
    first_index = page * int(limit) + 1
    last_index = (page+1) *int(limit)
    context['firstIndex'] = first_index
    context['lastIndex'] = last_index
    context['limit'] = limit
    pages = []
    for page in range(totalPage - 1):
        pages.append(page)
    context['totalPage'] = pages
    context['totalPageNumber'] = totalPage - 2
    context['totalPageNumber1'] = totalPage - 3
    return render(request, 'Bugs.html', context)

import datetime

def addBug(request):
    BSD = request.POST.get('BSD', '')
    itemId = np.random.randint(999999)
    reportDate =  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    enteredBy = usernameG
    connection = sqlite3.connect('./Parts.db')
    cursor = connection.cursor()
    sql_command = "INSERT OR REPLACE INTO BUGS (report_id, report_desc, report_date, entered_by)" + " VALUES ('" + str(itemId) +"', '" + BSD + "', '" + reportDate +"', '" + enteredBy +  "'); "
    cursor.execute(sql_command)
    connection.commit()
    connection.close()
    return bugs(request)

def deleteBug(request):
    itemId = request.GET.get('itemId', '')
    #request.POST['itemId']
    connection = sqlite3.connect('./Parts.db')
    cursor = connection.cursor()
    #sql_command = "INSERT OR REPLACE INTO PRODUCTS (ItemNumber, Description, Price, Available, Class, Origin, Lead_Time)" + " VALUES ('" + str(itemId) +"', '" + itemName + "', " + str(unitPrice) +", " + str(qis) + ", '" + class1 + "', '"+ origin + "', '" + leadTime + "'); "
    sql_command = "DELETE FROM BUGS WHERE report_id = " + itemId
    cursor.execute(sql_command)
    connection.commit()
    connection.close()
    return bugs(request)

def customer(request):
    if 'page' in request.GET:
        page = int(request.GET['page'])
    else:
        page = 0
    if 'limit' in request.GET:
        limit = request.GET['limit']
    else:
        limit = "5"
    connection = sqlite3.connect('./Parts.db')
    #kk = connection.execute("SELECT * FROM PRODUCTS")
    #return HttpResponse(kk)

    cursor = connection.cursor()
    sql = "SELECT * FROM CUSTOMERS LIMIT " + str(limit) + " OFFSET " + str(page)
    cursor.execute(sql)
    result = cursor.fetchall()
    sql1 = "SELECT count(*) FROM CUSTOMERS"
    cursor1 = connection.cursor()
    cursor1.execute(sql1)
    countNum = cursor1.fetchall()
    connection.commit()
    connection.close()
    totalPage = countNum[0][0]//int(limit) + 1
    context = {}
    list = []
    for i in result:
        item = {}
        item['id'] = i[0]
        item['firstName'] = i[1]
        item['lastName'] = i[2]
        item['phone'] = i[3]
        item['email'] = i[4]
        list.append(item)
    context['items'] = list
    enen = result[0][0]
    context['enen'] = enen
    context['kk'] = sql
    first_index = page * int(limit) + 1
    last_index = (page+1) *int(limit)
    context['firstIndex'] = first_index
    context['lastIndex'] = last_index
    context['limit'] = limit
    pages = []
    for page in range(totalPage - 1):
        pages.append(page)
    context['totalPage'] = pages
    context['totalPageNumber'] = totalPage - 2
    context['totalPageNumber1'] = totalPage - 3
    return render(request, 'Customer.html', context)


def addCustomer(request):
    firstName = request.POST.get('firstName', '')
    lastName = request.POST.get('lastName', '')
    phone = request.POST.get('phone', '')
    email = request.POST.get('email', '')
    itemId = np.random.randint(999999)
    connection = sqlite3.connect('./Parts.db')
    cursor = connection.cursor()
    sql_command = "INSERT OR REPLACE INTO CUSTOMERS (CustID, Fname, Lname, Phone, Email)" + " VALUES ('" + str(itemId) +"', '" + firstName + "', '" + lastName +"', '" + phone + "', '" + email +"'); "
    cursor.execute(sql_command)
    connection.commit()
    connection.close()
    return customer(request)

def deleteCustomer(request):
    itemId = request.GET.get('itemId', '')
    #request.POST['itemId']
    connection = sqlite3.connect('./Parts.db')
    cursor = connection.cursor()
    #sql_command = "INSERT OR REPLACE INTO PRODUCTS (ItemNumber, Description, Price, Available, Class, Origin, Lead_Time)" + " VALUES ('" + str(itemId) +"', '" + itemName + "', " + str(unitPrice) +", " + str(qis) + ", '" + class1 + "', '"+ origin + "', '" + leadTime + "'); "
    sql_command = "DELETE FROM CUSTOMERS WHERE CustID = " + itemId
    cursor.execute(sql_command)
    connection.commit()
    connection.close()
    return customer(request)
"""
    def itemslocal():
        page = 0
        limit = "5"
        sortby = "0"
        itemName = ""
        connection = sqlite3.connect('./Parts.db')
        kk = connection.execute("SELECT * FROM PRODUCTS")
        return print(kk)

    itemslocal()
"""