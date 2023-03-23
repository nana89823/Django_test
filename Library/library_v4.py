import pymysql

usr = 'root'
pwd = 'Aaa89823'
db = 'books'


connection = pymysql.connect(
    host='localhost', port=3306, user=usr, password=pwd, database=db)
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS books")
try:
    with connection.cursor() as cursor:
        # 建立 SQL 語句
        sql = """CREATE TABLE `books` (
                `name` char(25) NOT NULL,
                `author` char(25),
                `year` int(20),
                `review` varchar (3000)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

        # 執行 SQL 語句
        cursor.execute(sql)
    # 提交變更
    connection.commit()
except:
    pass
finally:
    # 關閉連接
    connection.close()


class Book:
    def __init__(self, name, author, year, review=None):
        self.name = name
        self.author = author
        self.year = year
        self.review = review

    def __str__(self):
        return '''書名：《%s》
                  作者：%s 
                  年份：%s 
                  心得：%s ''' % (self.name, self.author, self.year, self.review)


class BookManager:
    def __init__(self):
        self.books = []
        book1 = Book('灌籃高手新裝再編版', '井上雄彥', '1967')
        book2 = Book('如果30歲還是處男，似乎就能成為魔法師', '豊田悠', '2023')
        book3 = Book('鏈鋸人【1-11集第一部完】', '藤本樹', '2019')
        book4 = Book('小鎮醫生', '泰絲．格里森', '2023')
        book5 = Book('不便利的便利店', '金浩然', '2022')
        book6 = Book('手套與憐憫', '吉本芭娜娜 ', '2023')
        book7 = Book('餘生是你 晚點沒關係', '黃山料', '2022')
        book8 = Book('灌籃高手新裝再編版', '井上雄彥', '1967')
        book9 = Book('如果30歲還是處男，似乎就能成為魔法師', '豊田悠', '2023')
        book10 = Book('鏈鋸人【1-11集第一部完】', '藤本樹', '2019')
        book11 = Book('神明在看著呢：我的巫女日記（獨家作者親簽版）', '洪承喜 ', '2023')
        # for i in range(1,12):
        #     o_books='book'+str(i)
        #     self.books.append(o_books)

        self.books.append(book1)
        self.books.append(book2)
        self.books.append(book3)
        self.books.append(book4)
        self.books.append(book5)
        self.books.append(book6)
        self.books.append(book7)
        self.books.append(book8)
        self.books.append(book9)
        self.books.append(book10)
        self.books.append(book11)

    def check_book(self):
        connection = pymysql.connect(
            host='localhost', port=3306, user=usr, password=pwd, database=db)
        cursor = connection.cursor()

        try:
            with connection.cursor() as cursor:
                print(self.books)
                for book in self.books:
                    sql = 'INSERT INTO books (name, author, year ,review) VALUES ("%s", "%s", "%s" ,"%s");'\
                        % (book.name, book.author, book.year, book.review)
                    print(sql)
                    cursor.execute(sql)
            # 提交變更
            connection.commit()
        finally:
            # 關閉連接
            connection.close()
    # 0 首先會有三本書

    def select_book(self):
        connection = pymysql.connect(
            host='localhost', port=3306, user=usr, password=pwd, database=db)
        cursor = connection.cursor()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM books"
                cursor.execute(sql)
                results = cursor.fetchall()
                for row in results:
                    bname = row[0]
                    bauthor = row[1]
                    byear = row[2]
                    breview = row[3]
                    # print(bname,bauthor,byear,breview)
                    print('''書名：《%s》
                            作者：%s 
                            年份：%s 
                            心得：%s ''' % (bname, bauthor, byear, breview))
            # 提交變更
            connection.commit()
        finally:
            # 關閉連接
            connection.close()

    # 1 新增書籍
    def add_book(self):
        new_name = input('請輸入書籍名稱：')
        new_author = input('請輸入作者名稱：')
        new_year = input('請輸入書籍年份：')
        new_review = input('請輸入閱讀心得：(如未看過請填寫無)')
        # 獲取書籍相應資訊，賦值給屬性
        # new_book = Book(new_name, new_author, new_year,new_review)

        # 傳入引數，建立Book類範例new_book
        # self.books.append(new_book)
        # 將new_book新增到列表books裡
        connection = pymysql.connect(
            host='localhost', port=3306, user=usr, password=pwd, database=db)

        cursor = connection.cursor()
        try:
            with connection.cursor() as cursor:
                # 建立 SQL 語句
                if new_review == '無' or None:
                    sql = 'INSERT INTO books (name, author, year) VALUES ("%s", "%s", "%s");'\
                        % (new_name, new_author, new_year)
                else:
                    sql = 'INSERT INTO books (name, author, year,review) VALUES ("%s", "%s", "%s", "%s");'\
                        % (new_name, new_author, new_year, new_review)
                # 執行 SQL 語句
                cursor.execute(sql)
            # 提交變更
            connection.commit()
        finally:
            # 關閉連接
            connection.close()

        print('書籍錄入成功！')
    # 2 刪除書籍

    def delete_book(self):
        del_name = input('請輸入書籍名稱：')
        del_author = input('請輸入作者名稱：')
        del_year = input('請輸入書籍年份：')

        connection = pymysql.connect(
            host='localhost', port=3306, user=usr, password=pwd, database=db)

        cursor = connection.cursor()
        try:
            with connection.cursor() as cursor:
                # 建立 SQL 語句
                sql = 'DELETE FROM books WHERE name="%s" and year= "%s" '\
                    % (del_name, del_year)
                # 執行 SQL 語句
                cursor.execute(sql)
            # 提交變更
            connection.commit()
        finally:
            # 關閉連接
            connection.close()

        print('書籍刪除成功！')
    # 3 編輯書籍

    def update_book(self):
        bname = input('請輸入書籍名稱：')
        bauthor = input('請輸入作者名稱：')
        byear = input('請輸入書籍年份：')

        new_name = input('要改的書籍名稱是：')
        new_author = input('要改的作者名稱是：')
        new_year = input('要改的書籍年份是：')
        # new_year=int(new_year)
        if new_author != '':
            print('更新中')
        connection = pymysql.connect(
            host='localhost', port=3306, user='root', password='asd851216', database='libary')
        if bname == '' or bauthor == '' or byear == '':
            print('資料不正確')

        cursor = connection.cursor()
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
                # 建立 SQL 語句
                # if new_name != '':
                #     sql1 = 'UPDATE books SET name="%s" where name="%s" AND author="%s" AND year="%s";'\
                #         % (new_name,bname,bauthor,byear)
                #     cursor.execute(sql1)
                #     print(sql1)
                # if new_author != '':
                #     sql2 = 'UPDATE books SET author="%s" where name="%s" AND author="%s" AND year="%s";'\
                #         % (new_author,bname,bauthor,byear)
                #     cursor.execute(sql2)
                #     print(sql2)
                # if new_year != '':
                #     sql3 = 'UPDATE books SET year="%s" where name="%s" AND author="%s" AND year="%s";'\
                #         % (new_year,bname,bauthor,byear)
                #     cursor.execute(sql3)
                #     print(sql3)
                # 執行 SQL 語句
            # 提交變更
            connection.commit()
        finally:
            # 關閉連接
            connection.close()
        if (new_name == bname) and (new_author == bauthor) and (new_year == byear):
            print('書籍未更新')
        elif new_name == '' and new_author == '' and new_year == '':
            print('書籍未更新')
        else:
            print('書籍更新成功！')

    # 4 新增心得 使⽤者可以為某⼀本書籍新增、刪除、編輯閱讀⼼得

    def add_review(self):
        upre_name = input('請輸入書籍名稱：')
        upre_author = input('請輸入作者名稱：')
        upre_year = input('請輸入書籍年份：')
        upre_review = input('請寫下閱讀心得：')
        # 獲取書籍相應資訊，賦值給屬性

        connection = pymysql.connect(
            host='localhost', port=3306, user=usr, password=pwd, database=db)

        cursor = connection.cursor()
        try:
            with connection.cursor() as cursor:
                # 建立 SQL 語句
                if upre_review == '' or None:
                    print('心得內容不得為空')
                    return None
                if upre_name == '' or None:
                    print('書本名稱不得為空')
                    return None
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
                # 執行 SQL 語句
                print(sql)
                cursor.execute(sql)
            # 提交變更
            connection.commit()
        finally:
            # 關閉連接
            connection.close()

        if upre_review == '':
            print('心得未新增成功')
        elif upre_name == '' and upre_author == '' and upre_year == '':
            print('心得未新增成功')
        else:
            print('心得更新成功！')
    # 4 修改心得

    def res_review(self):
        res_name = input('請輸入要編輯的書籍名稱：')
        res_author = input('請輸入要編輯的作者名稱：')
        res_year = input('請輸入要編輯的書籍年份：')
        if res_name == '' or res_author == '' or res_year == '':
            print('請完整提供書名/作者/年份')
            return None

        connection = pymysql.connect(
            host='localhost', port=3306, user=usr, password=pwd, database=db)
        cursor = connection.cursor()

        with connection.cursor() as cursor:
            # 建立 SQL 語句
            sql = "SELECT review FROM books WHERE name='%s' AND author='%s' AND year='%s';"\
                % (res_name, res_author, res_year)
            # 執行 SQL 語句
            print(sql)
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                oldreview = row[0]
                # print(bname,bauthor,byear,breview)
                print('舊心得：%s' % (oldreview))
        connection.commit()
        # 索取心得

        try:
            with connection.cursor() as cursor:
                res_review = input('請輸入要修改的閱讀心得：')
                sql2 = 'UPDATE books SET review="%s" WHERE name="%s" AND author="%s" AND year="%s";'\
                    % (res_review, res_name, res_author, res_year)
                cursor.execute(sql2)
                if res_review == '':
                    print('心得未修改成功')
                elif res_name == '' and res_author == '' and res_year == '':
                    print('心得未修改成功')
                else:
                    print('心得更新成功！'+res_review)
            connection.commit()
            # 索取心得

        finally:
            # 關閉連接
            connection.close()
    # 刪除心得

    def del_review(self):
        del_name = input('請輸入要刪除的書籍名稱：')
        del_author = input('請輸入要刪除的作者名稱：')
        del_year = input('請輸入要刪除的書籍年份：')
        connection = pymysql.connect(
            host='localhost', port=3306, user=usr, password=pwd, database=db)
        cursor = connection.cursor()

        with connection.cursor() as cursor:
            # 建立 SQL 語句
            sql = "SELECT review FROM books WHERE name='%s' AND author='%s' AND year='%s';"\
                % (del_name, del_author, del_year,)
            # 執行 SQL 語句
            print(sql)
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                print(row)
                oldreview = row[0]
                # print(bname,bauthor,byear,breview)
                print('請確認欲刪除的心得是否為：%s' % (oldreview))
        connection.commit()
        # 索取心得

        con = 0
        while con == 0:
            answer = input('若要繼續刪除請回覆(Y/n)')
            if answer == 'n':
                print('刪除作業取消')
                con += 1
                return False
            elif answer != 'Y':
                print('輸入錯誤,請輸入Y/n')
                return None
            elif answer == 'Y':
                con += 2
                print('刪除中...')

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
    # 5  使⽤者可以篩選出同個作者的書籍列表

    def select_author(self):
        connection = pymysql.connect(
            host='localhost', port=3306, user=usr, password=pwd, database=db)
        cursor = connection.cursor()
        re_author = input('請輸入要找的作者：')
        if re_author == '':
            print('請輸入正確的作者名：')
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM books WHERE author='%s' ;"\
                    % (re_author)
                print(sql)
                cursor.execute(sql)
                results = cursor.fetchall()
                print(results)
                for row in results:
                    bname = row[0]
                    bauthor = row[1]
                    byear = row[2]
                    breview = row[3]
                    # print(bname,bauthor,byear,breview)
                    print('''書名：《%s》
                            作者：%s 
                            年份：%s 
                            心得：%s ''' % (bname, bauthor, byear, breview))
            # 提交變更
            connection.commit()
        finally:
            # 關閉連接
            connection.close()

    def desc_author(self):
        connection = pymysql.connect(
            host='localhost', port=3306, user=usr, password=pwd, database=db)
        cursor = connection.cursor()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM books ORDER BY author DESC ;"
                cursor.execute(sql)
                results = cursor.fetchall()
                for row in results:
                    bname = row[0]
                    bauthor = row[1]
                    byear = row[2]
                    breview = row[3]
                    # print(bname,bauthor,byear,breview)
                    print('''書名：《%s》
                            作者：%s 
                            年份：%s 
                            心得：%s ''' % (bname, bauthor, byear, breview))
        finally:
            # 關閉連接
            connection.close()

    def orderby_author(self):
        connection = pymysql.connect(
            host='localhost', port=3306, user=usr, password=pwd, database=db)
        cursor = connection.cursor()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM books ORDER BY author ;"
                cursor.execute(sql)
                results = cursor.fetchall()
                for row in results:
                    bname = row[0]
                    bauthor = row[1]
                    byear = row[2]
                    breview = row[3]
                    # print(bname,bauthor,byear,breview)
                    print('''書名：《%s》
                            作者：%s 
                            年份：%s 
                            心得：%s ''' % (bname, bauthor, byear, breview))
        finally:
            # 關閉連接
            connection.close()

    def desc_year(self):
        connection = pymysql.connect(
            host='localhost', port=3306, user=usr, password=pwd, database=db)
        cursor = connection.cursor()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM books ORDER BY year DESC ;"
                cursor.execute(sql)
                results = cursor.fetchall()
                for row in results:
                    bname = row[0]
                    bauthor = row[1]
                    byear = row[2]
                    breview = row[3]
                    # print(bname,bauthor,byear,breview)
                    print('''書名：《%s》
                            作者：%s 
                            年份：%s 
                            心得：%s ''' % (bname, bauthor, byear, breview))
        finally:
            # 關閉連接
            connection.close()

    def orderby_year(self):
        connection = pymysql.connect(
            host='localhost', port=3306, user=usr, password=pwd, database=db)
        cursor = connection.cursor()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM books ORDER BY year  ;"
                cursor.execute(sql)
                results = cursor.fetchall()
                for row in results:
                    bname = row[0]
                    bauthor = row[1]
                    byear = row[2]
                    breview = row[3]
                    # print(bname,bauthor,byear,breview)
                    print('''書名：《%s》
                            作者：%s 
                            年份：%s 
                            心得：%s ''' % (bname, bauthor, byear, breview))
        finally:
            # 關閉連接
            connection.close()
    # 使用者可以透過關鍵字在書名欄位中搜尋,找到他們要找的書籍

    def regex_search(self):
        connection = pymysql.connect(
            host='localhost', port=3306, user=usr, password=pwd, database=db)
        cursor = connection.cursor()

        con = 0
        while con == 0:
            regex = input('請輸入關鍵字')
            if regex == '':
                print('請確實輸入內容')
                # return None
            else:
                con += 1

        try:
            with connection.cursor() as cursor:
                sql = "SELECT name FROM books WHERE name LIKE '%%%s%%';" \
                    % (regex)
                print(sql)
                cursor.execute(sql)
                results = cursor.fetchall()
                for row in results:
                    bname = row[0]
                    print('書名：'+'《'+bname+'》')
        finally:
            # 關閉連接
            connection.close()

    def manu(self):
        print('進入圖書館囉')
        while True:
            choice = int(input('''歡迎使用本圖書館借閱系統！請選擇您需要的服務：
                        0.顯示圖書館書籍
                        1.新增書本
                        2.刪除書本
                        3.更新書庫
                        4.新增心得 
                        5.修改心得
                        6.刪除心得
                        7.搜尋作者作品
                        8.依照作者升冪
                        9.依照年份升冪
                        10.依照作者降冪
                        11.依照年份降冪
                        12.關鍵字搜尋
                        13.退出系統
                        請輸入阿拉伯數字選擇對應的功能：
         '''))
            if choice == 0:
                self.select_book()  # 顯示書庫
                # 顯示每本書的資訊
            elif choice == 1:
                self.add_book()  # 新增書本
            elif choice == 2:
                self.delete_book()  # 刪除書本
            elif choice == 3:
                self.update_book()  # 更新書庫
            elif choice == 4:
                self.add_review()  # 新增心得
            elif choice == 5:
                self.res_review()  # 修改心得
            elif choice == 6:
                self.del_review()  # 刪除心得
            elif choice == 7:
                self.select_author()  # 搜尋作者作品
            elif choice == 8:
                self.desc_author()  # 依照作者升冪
            elif choice == 9:
                self.desc_year()  # 依照年份升冪
            elif choice == 10:
                self.orderby_author()  # 依照作者降冪
            elif choice == 11:
                self.orderby_year()  # 依照年份降冪
            elif choice == 12:
                self.regex_search()  # 關鍵字搜尋
            elif choice == 13:
                print('感謝使用本系統')
                break


manager = BookManager()
manager.check_book()
manager.manu()
