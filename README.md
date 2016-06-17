# Proxysetter
Automatic proxysetter for Netease-musicbox
## 1.功能
自动为_命令行版本_的网易云音乐配置代理服务器地址，在海外也能使用网易云音乐。实时抓取服务器列表和速度，自动配置连接速度最快的服务器。
## 2.配置方法
1.下载程序，解压。

2.打开 ~/.bashrc 文件。

3.在alias位置加入一行： alias proxysetter=‘python3 path/to/unzipped/location/proxysetter.py'

4.退出，并执行. ~/.bashrc

## 3.使用方法
在运行musicbox之前，先输入$ proxysetter [arguments]。目前支持的arguments有：

$ proxysetter a 自动配置最快的代理服务器

$ proxysetter l [location] 自动配置所选地域最快的代理服务器，如'$ proxysetter l 北京' 自动选择北京的代理。

