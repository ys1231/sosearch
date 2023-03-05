# sosearch

**so字符串搜索工具**

# 使用教程

`./sosearch -f armeabi-v7a/librtmp-jni.so -s Java -i 0 -o a.log`
```shell
usage: sosearch [-h] -f SOFILEPATH -s SEARCH [-i IGNORECASE] [-o OUTPUT]

so文件字符串搜索

options:
  -h, --help            show this help message and exit
  -f SOFILEPATH, --sofilepath SOFILEPATH
                        so文件或目录路径
  -s SEARCH, --search SEARCH
                        需要搜索的字符串
  -i IGNORECASE, --ignorecase IGNORECASE
                        忽略大小写 type(1|0) 默认为1忽略
  -o OUTPUT, --output OUTPUT
                        参数 保存到文件
```