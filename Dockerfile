#基于的基础镜像
FROM 
python:3.7


#代码添加到code文件夹

ADD ./crawler/code


# 设置code文件夹是工作目录

WORKDIR /code


# 安装支持

RUN pip install -r requirements.txt


CMD ["python", "/code/MerInfoCrawler/start.py"]
