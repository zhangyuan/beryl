# 运行示例

## 下载安装 Python

## 安装 behave 和 python-selenium

    pip install -r requirements.txt

## 下载安装 selenium 

下载地址 <http://www.seleniumhq.org/download/> 默认只支持 Firefox，可以下载安装其他的浏览器驱动。

可以直接下载 <http://selenium-release.storage.googleapis.com/2.48/selenium-server-standalone-2.48.2.jar>

## 运行测试

### 启动待测试网站

### 启动selenium server

    java -jar selenium-server-standalone-2.48.2.jar

从命令行进入 ./public 目录，执行 
    
    python -m SimpleHTTPServer

### 运行测试

在项目根目录执行

    behave

# 文档

docs 目录下有 behave 和 selenium 文档。文档从对应的源码生成。