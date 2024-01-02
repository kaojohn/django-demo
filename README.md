# 版本檢視
- git --version

### 建立全域端使用者
- git config --global user.name your-name
- git config --global user.email your-email

### 檢視git config
- git config --list

### VSCODE
- ctrl+shift+p (開啟設定)
- Default (Terminal cmd)

### 控管專案
- git init

### 檔案加入控管 (確認修改)
- git add <filename> ((( U變A (U為未控管)(A為控管)(M為控管後修改過)
- git add . (((全控管 (確認全修改

### 檢視控管狀態
- git status

### 檢視物件內容
- git cat-file -t 2+4(看型態) ex: d67e9b 
- git cat-file -p 2+4(看內容) ex: d67e9b

### 確定修改
- git add filename

### 反悔修改
- git restore filename

### 檢視暫存區 內容
- git ls-files -s

## 紀錄至倉庫
- git commit -m "紀錄內容"	
- git commit -am "紀錄內容"
                  add+m=am

### 檢視目前commit
- git log
### 濃縮至一行
- git log --oneline

## 開啟linx內建筆記本
- git commit
  - i (開始輸入)
  - esc+ : wq (儲存離開)
  - esc+ : q!(強制離開不儲存)

### 合併(修改)上一次commit
- git commit --amend

### 指令刪除
- git rm -f filename
 - git restore --staged filename(恢復)

## 移出控管 A=>U
- git rm -cached filename

### 檢視分支
- git branch
- git branch 新分支名稱(新增)

## 切換分支
- git checkout 分支名稱

## 合併分支
- git checkout master(主分支名稱)
 -git merge 分支名稱

## 刪除分支
- git branch -D 分支名稱

## 新增+切換
- git checkout -b 分支名稱

## 合併衝突
- 3 選一 
- git merge --abort(反悔合併)

## 切換至其他commit
- git checkout 2+4
- 回到最新位子
- git checkout master

## 真正回到過去(重置指令)
- git reset 2+4 (混和模式(沒真正刪) U=>A)
- git reset --hard 2+4(全刪)
- git reset --heard HEAD (重置到最新commit)
- git reset ORIG_HEAD (恢復)

## 檢視所有歷程
- git reflog

### github
- echo "# django-demo" >> README.md
- git init
- git add README.md
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/kaojohn/django-demo.git
- git push -u origin main

### 綁定雲端倉庫
- git remote add origin https://github.com/kaojohn/django-demo.git
- git remote -v (檢視綁定倉庫)


### 本地同步雲端
- git push
- git push -u origin master(首次)(master為主分支名稱)

### 複製專案
- 資料夾 右鍵 open git bash here
- git clone 網址(ex:https://github.com/kaojohn/django-demo).git

## 每新增/刪除/修改
- git add .
- git commit -m "資訊"
- git push
