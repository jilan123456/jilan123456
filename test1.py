 Linux期末作业
第一题：
在Linux下，安装git，使用git管理大作业相关的代码、配置文件等，要求有能反映大作业过程的git提交记录
安装giti
        yum install git //root用户才有权限
获取ssh密钥
        ssh-keygen -t rsa -C "xxxxxxxxxx@qq.com" //使用自己的邮箱
查看git版本
        git version
进入.ssh查看公钥
        cd /root/.ssh/
        ls
        vi id_rsa.pub //查看公钥
将公钥添加到Github中，使得Linux与Github相联系
在Github中打开Settings，点击SSH and GPG keys，再点New SSH key，把上面查看到的公钥粘贴进去，最后>点击Add SSH key
Linux与Github的连接配置成功
        ssh git@github.com //在.ssh中配置
        
新建目录并绑定git用户
        mkdir test
        cd test/
        git config --global user.name "xxxx" //自己的用户名
        git config --global user.email "xxxxxxxxxx@qq.com" //自己的邮箱
把test目录变成Git管理的仓库
        git init
将准备好的文件复制到git副本目录
        git add test1.py
        git status
提交到本地git仓库
        git commit -m "tests"
在Github上新建仓库，得到的SSH协议关联远程仓库
        git remote add origin git@github.com:xxxx/tests.git
将本地仓库内容传送到远程仓库
        git push -u origin master
文件成功上传
