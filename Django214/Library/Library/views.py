from django.shortcuts import render
from django.contrib import auth
import pymysql
import pandas as pd
# from webapp import models
usr = 'root'
pwd = 'Aaa89823'
db = 'masonlin'


def f_add_book(self):
    new_name = input('請輸入書籍名稱：')
    new_author = input('請輸入作者名稱：')
    new_year = input('請輸入書籍年份：')
    new_review = input('請輸入閱讀心得：(如未看過請填寫無)')
    connection = pymysql.connect(
        host='localhost', port=3306, user=usr, password=pwd, database=db)
    cursor = connection.cursor()
    try:
        with connection.cursor() as cursor:
            if new_review == '無' or None:
                sql = 'INSERT INTO books (name, author, year) VALUES ("%s", "%s", "%s");'\
                    % (new_name, new_author, new_year)
            else:
                sql = 'INSERT INTO books (name, author, year,review) VALUES ("%s", "%s", "%s", "%s");'\
                    % (new_name, new_author, new_year, new_review)
            cursor.execute(sql)
        connection.commit()
    finally:
        connection.close()

    print('書籍錄入成功！')


def index(request):
    return render(request, 'index.html')


def index_del(request):
    return render(request, 'index_del.html')


def index_update(request):
    return render(request, 'index_update.html')


def addreview(request):
    return render(request, 'index_review.html')


def resreview(request):
    return render(request, 'index_res.html')


def delreview(request):
    return render(request, 'index_delreview.html')


def wrong(request):
    return render(request, 'wrong.html')


def index_search(request):
    return render(request, 'index_search.html')


def index_regex(request):
    return render(request, 'index_regex.html')


def add_book(request):
    connection = pymysql.connect(
        host='localhost', port=3306, user=usr, password=pwd, database=db)
    cursor = connection.cursor()
    bookname = request.POST.get('bookname', '')
    authorname = request.POST.get('authorname', '')
    year = request.POST.get('year', '')
    bookreview = request.POST.get('bookreview', '')
    print(bookname, authorname, year, bookreview)
    if bookname == '' and authorname == '' and year == '':
        return render(request, 'wrong.html')

    try:
        with connection.cursor() as cursor:
            if bookreview == '無' or None:
                sql = 'INSERT INTO books (name, author, year) VALUES ("%s", "%s", "%s");'\
                    % (bookname, authorname, year)
            else:
                sql = 'INSERT INTO books (name, author, year,review) VALUES ("%s", "%s", "%s", "%s");'\
                    % (bookname, authorname, year, bookreview)
            cursor.execute(sql)
        connection.commit()
    finally:
        connection.close()
    return render(request, 'addbook.html')


def delete_book(request):
    connection = pymysql.connect(
        host='localhost', port=3306, user=usr, password=pwd, database=db)
    cursor = connection.cursor()

    del_name = request.POST.get('bookname', '')
    del_author = request.POST.get('authorname', '')
    del_year = request.POST.get('year', '')

    if del_name == '':
        return render(request, 'wrong.html')
    elif del_name == '' and del_author == '' and del_year == '':
        return render(request, 'wrong.html')

    try:
        with connection.cursor() as cursor:
            sql = 'DELETE FROM books WHERE name="%s" AND year= "%s" AND author="%s" '\
                % (del_name, del_year, del_author)
            cursor.execute(sql)
        connection.commit()
    finally:
        connection.close()

    return render(request, 'delbook.html')


def update_book(request):
    connection = pymysql.connect(
        host='localhost', port=3306, user=usr, password=pwd, database=db)
    cursor = connection.cursor()

    bname = request.POST.get('bookname', '')
    bauthor = request.POST.get('authorname', '')
    byear = request.POST.get('year', '')

    new_name = request.POST.get('new_name', '')
    new_author = request.POST.get('new_author', '')
    new_year = request.POST.get('new_year', '')
    # new_year=int(new_year)
    if new_name == '':
        new_name = bname
    if new_author == '':
        new_author = bauthor
    if new_year == '':
        new_year = byear

    try:
        with connection.cursor() as cursor:
            sql1 = 'UPDATE books SET name="%s",author="%s",year="%s" where name="%s" AND author="%s" AND year="%s";'\
                % (new_name, new_author, new_year, bname, bauthor, byear)
            cursor.execute(sql1)
            print(sql1)
        connection.commit()
    finally:
        connection.close()
    if (new_name == bname) and (new_author == bauthor) and (new_year == byear):
        return render(request, 'wrong.html')
    elif new_name == '' and new_author == '' and new_year == '':
        return render(request, 'wrong.html')
    else:
        print('書籍更新成功！')

    return render(request, 'updatebook.html')


def add_review(request):
    connection = pymysql.connect(
        host='localhost', port=3306, user=usr, password=pwd, database=db)
    cursor = connection.cursor()
    upre_name = request.POST.get('bookname', '')
    upre_author = request.POST.get('authorname', '')
    upre_year = request.POST.get('year', '')
    upre_review = request.POST.get('bookreview', '')

    try:
        with connection.cursor() as cursor:
            if upre_review == '' or None:
                print('心得內容不得為空')
                return render(request, 'wrong.html')
            if upre_name == '' or None:
                print('書本名稱不得為空')
                return render(request, 'wrong.html')
            else:
                if upre_name != '' and upre_author != '':
                    sql = 'UPDATE books SET review="%s" WHERE name="%s" AND author="%s";'\
                        % (upre_review, upre_name, upre_author,)
                elif upre_name != '' and upre_year != '':
                    sql = 'UPDATE books SET review="%s" WHERE name="%s" AND year="%s";'\
                        % (upre_review, upre_name, upre_year,)
                else:
                    sql = 'UPDATE books SET review="%s" WHERE name="%s" AND author="%s" AND year="%s";'\
                        % (upre_review, upre_name, upre_author, upre_year)
            print(sql)
            cursor.execute(sql)
        connection.commit()
    finally:
        connection.close()

    if upre_review == '':
        print('心得未新增成功')
    elif upre_name == '' and upre_author == '' and upre_year == '':
        print('心得未新增成功')
    else:
        print('心得更新成功！')
    return render(request, 'reviewbook.html')


def res_review(request):

    connection = pymysql.connect(
        host='localhost', port=3306, user=usr, password=pwd, database=db)
    cursor = connection.cursor()
    res_name = request.POST.get('bookname', '')
    res_author = request.POST.get('authorname', '')
    res_year = request.POST.get('year', '')

    res_review = request.POST.get('bookreview', '')

    if res_name == '' or res_author == '' or res_year == '':
        print('請完整提供書名/作者/年份')
        return render(request, 'wrong.html')
    elif res_review == '':
        return render(request, 'wrong.html')
    try:
        with connection.cursor() as cursor:

            sql2 = 'UPDATE books SET review="%s" WHERE name="%s" AND author="%s" AND year="%s";'\
                % (res_review, res_name, res_author, res_year)
            cursor.execute(sql2)

        connection.commit()

    finally:
        connection.close()
    return render(request, 'resreview.html')


def del_review(request):
    connection = pymysql.connect(
        host='localhost', port=3306, user=usr, password=pwd, database=db)
    cursor = connection.cursor()
    del_name = request.POST.get('bookname', '')
    del_author = request.POST.get('authorname', '')
    del_year = request.POST.get('year', '')

    if del_name == '' or del_author == '' or del_year == '':
        print('請完整提供書名/作者/年份')
        return render(request, 'wrong.html')

    connection = pymysql.connect(
        host='localhost', port=3306, user=usr, password=pwd, database=db)
    cursor = connection.cursor()

    with connection.cursor() as cursor:
        sql = "SELECT review FROM books WHERE name='%s' AND author='%s' AND year='%s';"\
            % (del_name, del_author, del_year,)
        print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            oldreview = row[0]
    connection.commit()

    try:
        with connection.cursor() as cursor:
            sql2 = 'UPDATE books SET review="%s" WHERE review="%s";'\
                % (None, oldreview)
            print(sql2)
            cursor.execute(sql2)
            print('心得已刪除')
        connection.commit()
        # 索取心得
    finally:
        # 關閉連接
        connection.close()

        return render(request, 'delreviewbook.html')


def select_author(request):
    connection = pymysql.connect(
        host='localhost', port=3306, user=usr, password=pwd, database=db)
    cursor = connection.cursor()
    re_author = request.POST.get('authorname', '')
    print('作者名='+re_author)
    if re_author == '':
        return render(request, 'wrong.html')
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM books WHERE author='%s' ;"\
                % (re_author)
            print(sql)
            cursor.execute(sql)
            results = cursor.fetchall()

            bname_l = []
            bauthor_l = []
            byear_l = []
            breview_l = []
            for row in results:
                bname = row[0]
                bauthor = row[1]
                byear = row[2]
                breview = row[3]
                bname_l.append(bname)
                bauthor_l.append(bauthor)
                byear_l.append(byear)
                breview_l.append(breview)
            df = pd.DataFrame(

                {'name': bname_l,
                 'author': bauthor_l,
                 'year': byear_l,
                 'review': breview_l
                 }

            )
            all = {"df": df}

        connection.commit()
    finally:
        connection.close()
        return render(request, 'searchauthor.html', context=all)


def orderby_a_y(request):
    connection = pymysql.connect(
        host='localhost', port=3306, user=usr, password=pwd, database=db)
    cursor = connection.cursor()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM books ORDER BY year, author  ;"
            cursor.execute(sql)
            results = cursor.fetchall()
            bname_l = []
            bauthor_l = []
            byear_l = []
            breview_l = []
            for row in results:
                bname = row[0]
                bauthor = row[1]
                byear = row[2]
                breview = row[3]
                bname_l.append(bname)
                bauthor_l.append(bauthor)
                byear_l.append(byear)
                breview_l.append(breview)
            df = pd.DataFrame(

                {'name': bname_l,
                 'author': bauthor_l,
                 'year': byear_l,
                 'review': breview_l
                 }

            )
            all = {"df": df}
    finally:
        # 關閉連接
        connection.close()
        return render(request, 'orderby_a_y.html', context=all)


def desc_a_y(request):
    connection = pymysql.connect(
        host='localhost', port=3306, user=usr, password=pwd, database=db)
    cursor = connection.cursor()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM books ORDER BY year DESC, author DESC ;"
            cursor.execute(sql)
            results = cursor.fetchall()
            bname_l = []
            bauthor_l = []
            byear_l = []
            breview_l = []
            for row in results:
                bname = row[0]
                bauthor = row[1]
                byear = row[2]
                breview = row[3]
                bname_l.append(bname)
                bauthor_l.append(bauthor)
                byear_l.append(byear)
                breview_l.append(breview)
            df = pd.DataFrame(

                {'name': bname_l,
                 'author': bauthor_l,
                 'year': byear_l,
                 'review': breview_l
                 }

            )
            all = {"df": df}
    finally:
        # 關閉連接
        connection.close()
        return render(request, 'desc_a_y.html', context=all)


def regex_search(request):
    connection = pymysql.connect(
        host='localhost', port=3306, user=usr, password=pwd, database=db)
    cursor = connection.cursor()

    regex = request.POST.get('bookname', '')

    try:
        with connection.cursor() as cursor:
            sql = "SELECT name FROM books WHERE name LIKE '%%%s%%';" \
                % (regex)
            print(sql)
            cursor.execute(sql)
            results = cursor.fetchall()
            bname_l = []
            for row in results:
                bname = row[0]
                bname_l.append(bname)
            df = pd.DataFrame(

                {'name': bname_l,
                 }

            )
            all = {"df": df}
    finally:
        # 關閉連接
        connection.close()
        return render(request, 'regex_search.html', context=all)
