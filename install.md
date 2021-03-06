# Journey DB平台安装步骤
## 环境准备
python 3.6+
mysql 5.6+
## 安装步骤
1. 克隆代码
```bash
cd /tmp/
git clone https://github.com/guyage/Journey.git
mkdir -p /app/
将后端Django程序拷贝至单独目录
mv /tmp/Journey/backend /app/Journey
或者直接下载zip包，上传到创建目录
```
2. 安装项目后端依赖包
```bash
cd /app/Journey/backend
pip install -r requirements.txt
```
3. 创建项目数据库及用户(项目所需MySQL数据库)
安装MySQL后，进入MySQL命令行
创建数据库
```bash
create database journey;
```
创建用户
```
grant all privileges on journey.* to journey@'项目后端Django服务所在IP' identified by 'journey';
```
4. 配置配置文件
```bash
cd /app/Journey
vim Journey.conf
```
配置文件说明如下：
```ini
# 项目访问地址：可自定义(需注意，自定义修改前端项目配置文件对应域名，Journey/frontend/config/下env.js文件)
[domain_name]                            
domain = journey.xs.jf                    
# 后端服务MySQL连接信息
[db]
host = X.X.X.X                            
port = 3306
user = journey
password = journey
database = journey
 # 邮件服务器连接信息
[mail]
mail_host = smtp.163.com
mail_user = XX
mail_pass = XX
mail_postfix = 163.com
# 创建用户默认密码，现已修改为随机密码
[userinfo]
default_passwd = aaa111
 # MySQL查询默认limit
[sqllimit]
limit = 100
# LDAP认证信息
[ldap]
ldap_uri = ldap://X.X.X.X:389             # LDAP服务连接地址及端口
ldap_base_dn = OU=X,DC=X,DC=com           # LDAP base_dn
ldap_bind_dn = CN=X                       # LDAP查找用户(可为LDAP任意用户，建议单独创建一个用户)
ldap_bind_passwd = X                      # LDAP查找用户密码
# soar执行文件信息
[soar]
soar_path = /app/soar/soar
soar_log = /app/soar/soar.log
soar_file_tmp = /app/soar/sqltempfile/
```
5. 配置gunicorn
```bash
cd /app/Journey/Journey
vim gunicorn_config.py
```
gunicorn配置文件如下：
```ini
import multiprocessing

bind = "0.0.0.0:8888"  
workers = 8
errorlog = '/logs/Journey/gunicorn.error.log'
accesslog = '/logs/Journey/gunicorn.access.log'
#loglevel = 'debug'
proc_name = 'Journey'
```
6. 启动后端Django服务，确认是否启动成功
这里测试的时候可以通过python manage.py runserver 0.0.0.0:8888启动，生产建议用下面方式启动
```bash
cd /app/Journey
gunicorn Journey.wsgi:application -c ./Journey/gunicorn_config.py
```
通过访问http://xxx.xxx.xxx.xxx:8888/ 确认是否安装成功
7. 前端项目
这里需要node环境，先安装node
### 开发模式下：
需注意，前端项目服务器需要配置hosts，解析journey.api(可修改，前端项目config下dev.env.js文件中)域名到后端Django实际ip
127.0.0.1(后端Django实际ip) journey.api
```bash
这里需要注意一点，需要
cd /tmp/Journey/frontend
npm install
npm run dev
然后访问http://xxx.xxx.xxx.xxx:8080/
```
### 生产模式下：
生产模式需要先部署nginx
```bash
打包前端vue项目
cd /tmp/Journey/frontend
npm install
npm run build
将生成dist文件夹，拷贝到/app/Journey下
cp -rf dist /app/Journey/
```
配置nginx：
```ini
server {
        # 项目访问域名，需与配置文件中一致，还有前端项目config下prod.env.js中域名一致
        server_name  journey.xs.jf; 
        listen 80;
        access_log /logs/nginx/journey.access.log main;
        error_log  /logs/nginx/journey.error.log;

        location /api {
            # 配置后端Django服务访问地址
            proxy_pass http://X.X.X.X:8888;
            # 此为upstream配置方式，需添加upstream配置文件
            #proxy_pass http://journey.api;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

        location / {
            root /app/Journey/dist;  # 注意此项，前端开发完成后，会做打包处理，此文件夹为打包后的文件夹
            index index.html;
        }

        location ~.*\.(js|css|png|jpg)$ {
            root /app/Journey/dist;
            expires 3h;
        }
}
```
配置完后，启动nginx
访问http://journey.xs.jf

