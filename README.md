# library_
個⼈書籍管理系統

-----
## 目的說明

1. 使⽤者可新增書籍以及為該書籍建立書籍資訊，書籍資訊⾄少需包括作者、出版年份、書名
2. 使⽤者可以刪除書籍
3. 使⽤者可以編輯書籍資訊
4. 使⽤者可以為某⼀本書籍新增、刪除、編輯閱讀⼼得
5. 使⽤者可以篩選出同個作者的書籍列表
6. 使⽤者可以依照作者與出版年排列書籍列表
7. 使⽤者可以透過關鍵字在書名欄位中搜尋，找到他們要找的書籍
-----

### 使用環境

`Python 3.11.0`

`Django 4.1.4`

`pandas `

-----

### 執行方式

```
請先安裝上述使用環境
並到MYSQL資料夾內依照步驟創建資料庫後建立表格

接著進入Library資料夾後打開terminal 
輸入python manage.py runserver 啟動Django

```

### 雲端佈署

作品有放上google cloud engine
可輸入網址查看
```
1. 新增書本：
http://34.80.25.94:8000/index/

- 會透過使用者輸入的 書名/作者/年份/心得，
帶入參數，確認存入mysql後，會跳轉頁面書本新增成功


2. 刪除書本：
http://34.80.25.94:8000/index_del/

- 會透過使用者輸入的 書名/作者/年份，
帶入參數，從db刪除該筆資料後，會跳轉頁面書本刪除成功

- 若使用者書名/作者/年份，皆未輸入則會跳轉至wrong錯誤頁面，顯示資料不齊全。

3. 修改書本：
http://34.80.25.94:8000/index_update/

- 會透過使用者輸入的 書名/作者/年份, 欲修改的書名/作者/年份，
帶入參數，從db修改該筆資料後，會跳轉頁面書本修改成功

- 若使用者書名/作者/年份，任一未輸入則會跳轉至wrong錯誤頁面，顯示資料不齊全。
或者舊的資料與新的資料完全一致，也會跳轉致錯誤頁面。

4. 新增心得：
http://34.80.25.94:8000/index_review/

- 會透過使用者輸入的 書名/作者/年份/心得, 到資料庫篩選出該筆資料，
接著經由心得欄位得到的資料，新增書本的心得，接著跳轉頁面新增心得成功

- 若使用者書名/心得，任一未輸入則會跳轉至wrong錯誤頁面，顯示資料不齊全。
- 若使用者書名/作者/年份皆為空，也會跳轉至wrong錯誤頁面，顯示資料不齊全。

5. 修改心得：
http://34.80.25.94:8000/index_res/

- 會透過使用者輸入的 書名/作者/年份/舊心得/要修改的心得, 到資料庫篩選出該筆資料，
接著經由4項參數篩選出書本的心得，接著跳轉頁面心得修改成功。

- 若使用者書名/作者/年份，任一未輸入則會跳轉至wrong錯誤頁面，顯示資料不齊全。
- 若使用者欲修改的心得為空，也會跳轉至wrong錯誤頁面，顯示資料不齊全。

6. 刪除心得：
http://34.80.25.94:8000/index_delreview/

- 會透過使用者輸入的 書名/作者/年份, 到資料庫篩選出該筆資料，
接著刪除書本的心得，跳轉頁面心得刪除成功。

- 若使用者書名/作者/年份，任一未輸入則會跳轉至wrong錯誤頁面，顯示資料不齊全。

7. 篩選作者：
http://34.80.25.94:8000/index_search/

- 會透過使用者者輸入的 作者名，到資料庫篩選出符合該作者寫的書本，跳轉至呈現的畫面。
- 若使用者作者未輸入則會跳轉至wrong錯誤頁面，顯示資料不齊全。

8. 依照年份、作者 降冪：
http://34.80.25.94:8000/desc_a_y/

- 使用者不需輸入參數，會直接將資料庫資料排序回傳資料產出呈現在頁面。

9. 依照年份、作者 升冪：
http://34.80.25.94:8000/orderby_a_y/

- 使用者不需輸入參數，會直接將資料庫資料排序回傳資料產出呈現在頁面。

10. 關鍵字搜尋：
http://34.80.25.94:8000/index_regex/

- 會透過使用者者輸入的 書名關鍵字，到資料庫篩選出相似的書本，跳轉至呈現的畫面。

11. 錯誤畫面：
http://34.80.25.94:8000/wrong/

```


