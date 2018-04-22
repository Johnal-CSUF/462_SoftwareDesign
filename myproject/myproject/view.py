from django.http import HttpResponse
from django.shortcuts import render

import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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
    itemName = request.GET.get('itemName', '')
    qis = request.GET.get('QIS', '')
    unitPrice = request.GET.get('unitPrice', '')
    class1 = request.GET.get('class', '')
    leadTime = request.GET.get('leadTime', '')
    origin = request.GET.get('origin', '')
    itemId = np.random.randint(999999)
    connection = sqlite3.connect('./Parts.db')
    cursor = connection.cursor()
    sql_command = "INSERT OR REPLACE INTO PRODUCTS (ItemNumber, Description, Price, Available, Class, Origin, Lead_Time)" + " VALUES ('" + str(itemId) +"', '" + itemName + "', " + str(unitPrice) +", " + str(qis) + ", '" + class1 + "', '"+ origin + "', '" + leadTime + "'); "
    cursor.execute(sql_command)
    connection.commit()
    connection.close()
    return None

def deleteItem(request):
    itemId = request.GET.get('itemId', '')
    #request.POST['itemId']
    connection = sqlite3.connect('./Parts.db')
    cursor = connection.cursor()
    #sql_command = "INSERT OR REPLACE INTO PRODUCTS (ItemNumber, Description, Price, Available, Class, Origin, Lead_Time)" + " VALUES ('" + str(itemId) +"', '" + itemName + "', " + str(unitPrice) +", " + str(qis) + ", '" + class1 + "', '"+ origin + "', '" + leadTime + "'); "
    sql_command = "DELETE FROM PRODUCTS WHERE ItemNumber = " + itemId
    cursor.execute(sql_command)
    connection.commit()
    connection.close()
    return None



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
    itemId = request.GET.get('itemId', '')
    #request.POST['itemId']
    connection = sqlite3.connect('./Parts.db')
    cursor = connection.cursor()
    #sql_command = "INSERT OR REPLACE INTO PRODUCTS (ItemNumber, Description, Price, Available, Class, Origin, Lead_Time)" + " VALUES ('" + str(itemId) +"', '" + itemName + "', " + str(unitPrice) +", " + str(qis) + ", '" + class1 + "', '"+ origin + "', '" + leadTime + "'); "
    sql_command = "DELETE FROM TRANSACTIONSS WHERE ORDERNUMBER = " + itemId
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

def login_view(request,first=False):
  username = request.GET.get('username', '')
  password = request.GET.get('password', '')
  #if username == 'lizenan' and password == 'lizenan':
    #  user = 1
  #else:
      #user = 0
  user = verify(username, password)
  context = {}

  if user == 1:
    name1 = name(username, password)
    context['user'] = name1[0][3]
    # Correct password, and the user is marked "active"
    # Redirect to a success page.
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
    BSD = request.GET.get('BSD', '')
    itemId = np.random.randint(999999)
    reportDate =  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    enteredBy = 'zenanLi'
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
	    item['newsletter'] = i[5]
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
    firstName = request.GET.get('firstName', '')
    lastName = request.GET.get('lastName', '')
    phone = request.GET.get('phone', '')
    email = request.GET.get('email', '')
    newsletter = request.GET.get('newsletter', '')
    itemId = np.random.randint(999999)
    connection = sqlite3.connect('./Parts.db')
    cursor = connection.cursor()
    sql_command = "INSERT OR REPLACE INTO CUSTOMERS (CustID, Fname, Lname, Phone, Email, Newsletter)" + " VALUES ('" + str(itemId) +"', '" + firstName + "', '" + lastName +"', '" + phone + "', '" + email +"', '" + newsletter +"'); "
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
	
def mailQueue(request):
    newsletter = request.GET.get('newsletter', '')
    connection = sqlite3.connect('./Parts.db')
    cursor = connection.cursor()
    sql_command = "SELECT Email FROM CUSTOMERS WHERE Newsletter == 1 "
    cursor.execute(sql_command)
    result1 = cursor.fetchall()
    for c in result1:
	    fromaddr = "CSUFInventory@gmail.com"
	    toaddr = c[0]
	    msg = MIMEMultipart()
	    msg['From'] = fromaddr
	    msg['To'] = toaddr
	    msg['Subject'] = "CSUF Inventory Promotions"
		
	    html = """<html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta name="viewport" content="initial-scale=1.0"><meta name="format-detection" content="telephone=no"><title>MOSAICO Responsive Email Designer</title><style type="text/css">
    body{ margin: 0; padding: 0; }
    img{ border: 0px; display: block; }

    .socialLinks{ font-size: 6px; }
    .socialLinks a{
      display: inline-block;
    }

    .long-text p{ margin: 1em 0px; }
    .long-text p:last-child{ margin-bottom: 0px; }
    .long-text p:first-child{ margin-top: 0px; }
  </style><style type="text/css">
    /* yahoo, hotmail */
    .ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div{ line-height: 100%; }
    .yshortcuts a{ border-bottom: none !important; }
    .vb-outer{ min-width: 0 !important; }
    .RMsgBdy, .ExternalClass{
      width: 100%;
      background-color: #3f3f3f;
      background-color: #3f3f3f}

    /* outlook/office365 add buttons outside not-linked images and safari have 2px margin */
    [o365] button{ margin: 0 !important; }

    /* outlook */
    table{ mso-table-rspace: 0pt; mso-table-lspace: 0pt; }
    #outlook a{ padding: 0; }
    img{ outline: none; text-decoration: none; border: none; -ms-interpolation-mode: bicubic; }
    a img{ border: none; }

    @media screen and (max-width: 600px) {
      table.vb-container, table.vb-row{
        width: 95% !important;
      }

      .mobile-hide{ display: none !important; }
      .mobile-textcenter{ text-align: center !important; }

      .mobile-full{
        width: 100% !important;
        max-width: none !important;
      }
    }
    /* previously used also screen and (max-device-width: 600px) but Yahoo Mail doesn't support multiple queries */
  </style><style type="text/css">
    
    #ko_singleArticleBlock_5 .links-color a, #ko_singleArticleBlock_5 .links-color a:link, #ko_singleArticleBlock_5 .links-color a:visited, #ko_singleArticleBlock_5 .links-color a:hover{
      color: #3f3f3f;
      color: #3f3f3f;
      text-decoration: underline
    }
    
    #ko_sideArticleBlock_12 .links-color a, #ko_sideArticleBlock_12 .links-color a:link, #ko_sideArticleBlock_12 .links-color a:visited, #ko_sideArticleBlock_12 .links-color a:hover{
      color: #3f3f3f;
      color: #3f3f3f;
      text-decoration: underline
    }
    
    #ko_footerBlock_2 .links-color a, #ko_footerBlock_2 .links-color a:link, #ko_footerBlock_2 .links-color a:visited, #ko_footerBlock_2 .links-color a:hover{
      color: #cccccc;
      color: #cccccc;
      text-decoration: underline
    }
    </style></head><body style="margin: 0; padding: 0; background-color: #3f3f3f; color: #919191;" text="#919191" vlink="#cccccc" bgcolor="#3f3f3f" alink="#cccccc"><center>

 

  <table class="vb-outer" style="background-color: #ffffff;" id="ko_titleBlock_9" width="100%" cellspacing="0" cellpadding="0" border="0" bgcolor="#ffffff"><tbody><tr><td class="vb-outer" style="padding-left: 9px; padding-right: 9px; font-size: 0;" valign="top" align="center">
      <!--[if (gte mso 9)|(lte ie 8)]><table align="center" border="0" cellspacing="0" cellpadding="0" width="570"><tr><td align="center" valign="top"><![endif]--><!--
      --><div style="margin: 0 auto; max-width: 570px; -mru-width: 0px;"><table class="vb-row" style="border-collapse: separate; width: 100%; background-color: #0066A8; mso-cellspacing: 0px; border-spacing: 0px; max-width: 570px; -mru-width: 0px;" width="570" cellspacing="0" cellpadding="0" border="0" bgcolor="#0066A8"><tbody><tr><td style="font-size: 0; padding: 0 9px;" valign="top" align="center"><div style="display: inline-block; vertical-align: top; width: 100%; max-width: 552px; -mru-width: 0px;"><!--
        --><table class="vb-content" style="border-collapse: separate; width: 100%; mso-cellspacing: 9px; border-spacing: 9px;" width="552" cellspacing="9" cellpadding="0" border="0"><!-- TODO class="title" --><tbody><tr><td style="font-weight: normal; color: #ffffff; font-size: 25px; font-family: Arial, Helvetica, sans-serif; text-align: center;" valign="top" width="100%" align="center"><span style="font-weight: normal;">Inventory management system</span></td>
    </tr></tbody></table></div></td>
    </tr></tbody></table></div><!--
    --><!--[if (gte mso 9)|(lte ie 8)]></td></tr></table><![endif]-->
    </td></tr></tbody></table><table class="vb-outer" style="background-color: #ffffff;" id="ko_logoBlock_7" width="100%" cellspacing="0" cellpadding="0" border="0" bgcolor="#ffffff"><tbody><tr><td class="vb-outer" style="padding-left: 9px; padding-right: 9px; font-size: 0;" valign="top" align="center">
      <!--[if (gte mso 9)|(lte ie 8)]><table align="center" border="0" cellspacing="0" cellpadding="0" width="570"><tr><td align="center" valign="top"><![endif]--><!--
      --><div style="margin: 0 auto; max-width: 570px; -mru-width: 0px;"><table style="border-collapse: separate; width: 100%; mso-cellspacing: 9px; border-spacing: 9px; max-width: 570px; -mru-width: 0px;" class="vb-row" width="570" cellspacing="9" cellpadding="0" border="0"><tbody><tr><td style="font-size: 0;" valign="top" align="center"><div style="display: inline-block; vertical-align: top; width: 100%; max-width: 276px; -mru-width: 0px;"><!--
        --><table class="vb-content" style="border-collapse: separate; width: 100%; mso-cellspacing: 9px; border-spacing: 9px;" width="276" cellspacing="9" cellpadding="0" border="0"><!-- TODO nel template originale abbiamo anche un font-size: 18px, externalTextStyle.size ... --><tbody><tr><td class="links-color" valign="top" width="100%" align="center"><!--[if (lte ie 8)]><div style="display: inline-block; width: 258px; -mru-width: 0px;"><![endif]--><img alt="" style="border: 0px; display: block; vertical-align: top; height: auto; margin: 0 auto; color: #f3f3f3; font-size: 18px; font-family: Arial, Helvetica, sans-serif; width: 100%; max-width: 258px; height: auto;" src="https://mosaico.io/srv/f-86km13b/img?src=https%3A%2F%2Fmosaico.io%2Ffiles%2F86km13b%2FScreen%2520Shot%25202018-04-20%2520at%25206.40.48%2520PM.png&amp;method=resize&amp;params=258%2Cnull" width="258" vspace="0" hspace="0" border="0" align="middle"><!--[if (lte ie 8)]></div><![endif]--></td></tr></tbody></table></div></td>
    </tr></tbody></table></div><!--
    --><!--[if (gte mso 9)|(lte ie 8)]></td></tr></table><![endif]-->
      
    </td></tr></tbody></table><table class="vb-outer" style="background-color: #ffffff;" id="ko_sideArticleBlock_12" width="100%" cellspacing="0" cellpadding="0" border="0" bgcolor="#ffffff"><tbody><tr><td class="vb-outer" style="padding-left: 9px; padding-right: 9px; font-size: 0;" valign="top" align="center">
      <!--[if (gte mso 9)|(lte ie 8)]><table align="center" border="0" cellspacing="0" cellpadding="0" width="570"><tr><td align="center" valign="top"><![endif]--><!--
      --><div style="margin: 0 auto; max-width: 570px; -mru-width: 0px;"><table class="vb-row" style="border-collapse: separate; width: 100%; background-color: #0066A8; mso-cellspacing: 9px; border-spacing: 9px; max-width: 570px; -mru-width: 0px;" width="570" cellspacing="9" cellpadding="0" border="0" bgcolor="#0066A8"><tbody><tr><td style="font-size: 0;" valign="top" align="center"><div style="width: 100%; max-width: 552px; -mru-width: 0px;"><!--[if (gte mso 9)|(lte ie 8)]><table align="center" border="0" cellspacing="0" cellpadding="0" width="552"><tr><![endif]--><!--
        --><!--
          --><!--[if (gte mso 9)|(lte ie 8)]><td align="left" valign="top" width="184"><![endif]--><!--
      --><div class="mobile-full" style="display: inline-block; vertical-align: top; width: 100%; max-width: 184px; -mru-width: 0px; min-width: calc(33.333333333333336%); max-width: calc(100%); width: calc(304704px - 55200%);"><!--
        --><table class="vb-content" style="border-collapse: separate; width: 100%; mso-cellspacing: 9px; border-spacing: 9px;" width="184" cellspacing="9" cellpadding="0" border="0"><tbody><tr><td class="links-color" valign="top" width="100%" align="center"><!--[if (lte ie 8)]><div style="display: inline-block; width: 166px; -mru-width: 0px;"><![endif]--><img alt="" style="border: 0px; display: block; vertical-align: top; height: auto; margin: 0 auto; color: #3f3f3f; font-size: 13px; font-family: Arial, Helvetica, sans-serif; width: 100%; max-width: 166px; height: auto;" src="https://mosaico.io/srv/f-86km13b/img?src=https%3A%2F%2Fmosaico.io%2Ffiles%2F86km13b%2FParts-Feature-2-1%2520%25281%2529.png&amp;method=resize&amp;params=166%2Cnull" width="166" vspace="0" hspace="0" border="0" align="middle"><!--[if (lte ie 8)]></div><![endif]--></td></tr></tbody></table><!--
      --></div><!--[if (gte mso 9)|(lte ie 8)]></td><![endif]--><!--
          --><!--[if (gte mso 9)|(lte ie 8)]><td align="left" valign="top" width="368"><![endif]--><!--
      --><div class="mobile-full" style="display: inline-block; vertical-align: top; width: 100%; max-width: 368px; -mru-width: 0px; min-width: calc(66.66666666666667%); max-width: calc(100%); width: calc(304704px - 55200%);"><!--
        --><table class="vb-content" style="border-collapse: separate; width: 100%; mso-cellspacing: 9px; border-spacing: 9px;" width="368" cellspacing="9" cellpadding="0" border="0"><!-- TODO class="title" --><tbody><tr><td class="long-text links-color" style="font-weight: normal; color: #3f3f3f; font-size: 13px; font-family: Arial, Helvetica, sans-serif; text-align: left; line-height: normal;" valign="top" width="100%" align="left"><p style="margin: 1em 0px; margin-bottom: 0px; margin-top: 0px;">Far far away, behind the word mountains, far from the countries <a href="" style="color: #3f3f3f; color: #3f3f3f; text-decoration: underline;">Vokalia and Consonantia</a>, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia.</p></td></tr></tbody></table><!--
      --></div><!--[if (gte mso 9)|(lte ie 8)]></td><![endif]--><!--
          --><!--
        --><!--
      --><!--[if (gte mso 9)|(lte ie 8)]></tr></table><![endif]--></div></td>
    </tr></tbody></table></div><!--
    --><!--[if (gte mso 9)|(lte ie 8)]></td></tr></table><![endif]-->
    </td></tr></tbody></table><table class="vb-outer" style="background-color: #ffffff;" id="ko_singleArticleBlock_5" width="100%" cellspacing="0" cellpadding="0" border="0" bgcolor="#ffffff"><tbody><tr><td class="vb-outer" style="padding-left: 9px; padding-right: 9px; font-size: 0;" valign="top" align="center">
      <!--[if (gte mso 9)|(lte ie 8)]><table align="center" border="0" cellspacing="0" cellpadding="0" width="570"><tr><td align="center" valign="top"><![endif]--><!--
      --><div style="margin: 0 auto; max-width: 570px; -mru-width: 0px;"><table class="vb-row" style="border-collapse: separate; width: 100%; background-color: #0066A8; mso-cellspacing: 9px; border-spacing: 9px; max-width: 570px; -mru-width: 0px;" width="570" cellspacing="9" cellpadding="0" border="0" bgcolor="#0066A8"><tbody><tr><td style="font-size: 0;" valign="top" align="center"><div style="display: inline-block; vertical-align: top; width: 100%; max-width: 552px; -mru-width: 0px;"><!--
        --><table class="vb-content" style="border-collapse: separate; width: 100%; mso-cellspacing: 9px; border-spacing: 9px;" width="552" cellspacing="9" cellpadding="0" border="0"><tbody><tr><td class="links-color" style="padding-bottom: 9px;" valign="top" width="100%" align="center"><!--[if (lte ie 8)]><div style="display: inline-block; width: 534px; -mru-width: 0px;"><![endif]--><img alt="" style="border: 0px; display: block; vertical-align: top; height: auto; margin: 0 auto; color: #3f3f3f; font-size: 13px; font-family: Arial, Helvetica, sans-serif; width: 100%; max-width: 534px; height: auto;" src="https://mosaico.io/srv/f-86km13b/img?src=https%3A%2F%2Fmosaico.io%2Ffiles%2F86km13b%2Fslider-3%2520%25281%2529.jpg&amp;method=resize&amp;params=534%2Cnull" width="534" vspace="0" hspace="0" border="0" align="middle"><!--[if (lte ie 8)]></div><![endif]--></td></tr><!-- TODO class="title" --><tr><td style="font-weight: normal; color: #3f3f3f; font-size: 18px; font-family: Arial, Helvetica, sans-serif; text-align: left;" valign="top" width="100%" align="left"><span style="font-weight: normal;">Section Title</span></td>
    </tr><tr><td class="long-text links-color" style="font-weight: normal; color: #3f3f3f; font-size: 13px; font-family: Arial, Helvetica, sans-serif; text-align: left; line-height: normal;" valign="top" width="100%" align="left"><p style="margin: 1em 0px; margin-bottom: 0px; margin-top: 0px;">Far far away, behind the word mountains, far from the countries <a href="" style="color: #3f3f3f; color: #3f3f3f; text-decoration: underline;">Vokalia and Consonantia</a>, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia.</p></td></tr><tr><td valign="top" align="left"><table style="border-spacing: 0; mso-padding-alt: 6px 6px 6px 6px; padding-top: 4px;" cellspacing="0" cellpadding="6" border="0" align="left"><tbody><tr><td style="text-align: center; font-weight: normal; padding: 6px; padding-left: 18px; padding-right: 18px; background-color: #0066A8; color: #0066A8; font-size: 13px; font-family: Arial, Helvetica, sans-serif; border-radius: 4px;" valign="middle" width="auto" bgcolor="#0066A8" align="left"><a style="text-decoration: none; font-weight: normal; color: #0066A8; font-size: 13px; font-family: Arial, Helvetica, sans-serif;" target="_new" href="">BUTTON</a></td>
      </tr></tbody></table></td>
    </tr></tbody></table></div></td>
    </tr></tbody></table></div><!--
    --><!--[if (gte mso 9)|(lte ie 8)]></td></tr></table><![endif]-->
    </td></tr></tbody></table><table class="vb-outer" style="background-color: #ffffff;" id="ko_logoBlock_1" width="100%" cellspacing="0" cellpadding="0" border="0" bgcolor="#ffffff"><tbody><tr><td class="vb-outer" style="padding-left: 9px; padding-right: 9px; font-size: 0;" valign="top" align="center">
      <!--[if (gte mso 9)|(lte ie 8)]><table align="center" border="0" cellspacing="0" cellpadding="0" width="570"><tr><td align="center" valign="top"><![endif]--><!--
      --><div style="margin: 0 auto; max-width: 570px; -mru-width: 0px;"><table style="border-collapse: separate; width: 100%; mso-cellspacing: 9px; border-spacing: 9px; max-width: 570px; -mru-width: 0px;" class="vb-row" width="570" cellspacing="9" cellpadding="0" border="0"><tbody><tr><td style="font-size: 0;" valign="top" align="center"><div style="display: inline-block; vertical-align: top; width: 100%; max-width: 276px; -mru-width: 0px;"><!--
        --><table class="vb-content" style="border-collapse: separate; width: 100%; mso-cellspacing: 9px; border-spacing: 9px;" width="276" cellspacing="9" cellpadding="0" border="0"><!-- TODO nel template originale abbiamo anche un font-size: 18px, externalTextStyle.size ... --><tbody><tr><td class="links-color" valign="top" width="100%" align="center"><!--[if (lte ie 8)]><div style="display: inline-block; width: 258px; -mru-width: 0px;"><![endif]--><img alt="" style="border: 0px; display: block; vertical-align: top; height: auto; margin: 0 auto; color: #f3f3f3; font-size: 18px; font-family: Arial, Helvetica, sans-serif; width: 100%; max-width: 258px; height: auto;" src="https://mosaico.io/srv/f-86km13b/img?src=https%3A%2F%2Fmosaico.io%2Ffiles%2F86km13b%2FEVS-70SSP-S2%2520%25281%2529.jpg&amp;method=resize&amp;params=258%2Cnull" width="258" vspace="0" hspace="0" border="0" align="middle"><!--[if (lte ie 8)]></div><![endif]--></td></tr></tbody></table></div></td>
    </tr></tbody></table></div><!--
    --><!--[if (gte mso 9)|(lte ie 8)]></td></tr></table><![endif]-->
      
      </td></tr></tbody></table><!-- footerBlock --><table class="vb-outer" style="background-color: #3f3f3f;" id="ko_footerBlock_2" width="100%" cellspacing="0" cellpadding="0" border="0" bgcolor="#3f3f3f"><tbody><tr><td class="vb-outer" style="padding-left: 9px; padding-right: 9px; font-size: 0;" valign="top" align="center">
    <!--[if (gte mso 9)|(lte ie 8)]><table align="center" border="0" cellspacing="0" cellpadding="0" width="570"><tr><td align="center" valign="top"><![endif]--><!--
      --><div style="margin: 0 auto; max-width: 570px; -mru-width: 0px;"><table style="border-collapse: separate; width: 100%; mso-cellspacing: 0px; border-spacing: 0px; max-width: 570px; -mru-width: 0px;" class="vb-row" width="570" cellspacing="0" cellpadding="0" border="0"><tbody><tr><td style="font-size: 0; padding: 0 9px;" valign="top" align="center"><div style="display: inline-block; vertical-align: top; width: 100%; max-width: 552px; -mru-width: 0px;"><!--
        --><table class="vb-content" style="border-collapse: separate; width: 100%; mso-cellspacing: 9px; border-spacing: 9px;" width="552" cellspacing="9" cellpadding="0" border="0"><tbody><tr><td class="long-text links-color" style="font-weight: normal; color: #919191; font-size: 13px; font-family: Arial, Helvetica, sans-serif; text-align: center;" valign="top" width="100%" align="center"><p style="margin: 1em 0px; margin-bottom: 0px; margin-top: 0px;">Email sent to <a href="mailto:%5Bmail%5D" style="color: #cccccc; color: #cccccc; text-decoration: underline;">[mail]</a></p></td></tr><tr><td style="font-weight: normal; color: #ffffff; font-size: 13px; font-family: Arial, Helvetica, sans-serif; text-align: center;" valign="top" width="100%" align="center"><a href="%5Bunsubscribe_link%5D" style="color: #ffffff; text-decoration: underline;" target="_new">Unsubscribe</a></td></tr><tr style="text-align: center;"><td class="links-color" style="text-align: center;" valign="top" width="100%" align="center"><!--[if (lte ie 8)]><div style="display: inline-block; width: 170px; -mru-width: 0px;"><![endif]
    --><!--[if (gte mso 9)|(lte ie 8)]></td></tr></table><![endif]-->
  </td></tr></tbody></table><!-- /footerBlock --></center></body></html>
"""
	    msg.attach(MIMEText(html, 'html'))
		
	    server = smtplib.SMTP('smtp.gmail.com', 587)
	    server.starttls()
	    server.login("CSUFInventory@gmail.com", "CsufProject123")
	    text = msg.as_string()
	    server.sendmail(fromaddr, toaddr, text)
	    server.quit()

    connection.commit()
    connection.close()
    return None
	
		
	
  
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
