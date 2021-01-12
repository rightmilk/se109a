# 課程:軟體工程與演算法 -- git/github 心得報告
## git簡介
### 使用數據庫管理歷史記錄
數據庫 (Repository) 是記錄檔案或目錄狀態的地方，儲存內容的修改歷史記錄。在數據庫的管理下除了儲存修改歷史記錄外，還可以追蹤內容的狀態和版本喔。
### 記錄修改的提交

若想把變更與新增的檔案/目錄儲存到數據庫中，您需要執行提交（Commit）。

執行提交後，數據庫裡會產生上次提交的狀態與現在狀態的差異記錄（也被稱為Revision）。

如下圖，提交是以時間順序排列狀態被儲存到數據庫中的。憑藉該提交和最新的檔案狀態，就可以知道過去的修改記錄以及內容。

## 指令
### Git設定
```
git config --global user.name <username>
git config --global user.email <mailaddress>  ##設定用戶名稱電子郵件
```
### 基礎指令
```
git clone <url>  ##複製一份專案到本地端
git add -A
git commit -m "<pattern>"
git push origin  ##將檔案推回至github
git pull  ##將檔案從github拉出
```
### 操作分支
```
git branch  ##顯示分支清單
git branch <branchname>  ##建立分支
git branch -m <oldbranch> <newbranch>  ##修改分支名稱
git branch -d <branchname>  ##刪除分支
git checkout <branch>  ##切換分支
git merge <branch>  ##合併分支
```
### 操作提交紀錄
```
git commit --amend  ##修改最近的提交紀錄
git commit --amend  ##只修改最近的提交記錄的註解
git rebase -i <commit>
git commit --amend
git rebase --continue  ##修改過去的提交記錄
git log --grep "<pattern>" ##尋找包含特定註解的提交
```
## 心得
透過不同的github教學網站學習，才知道原來有那麼多種git指令，不然以前永遠只會把自己的知道推上去。