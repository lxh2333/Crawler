#���ڵĻ�������
FROM 
python:3.7


#������ӵ�code�ļ���

ADD ./crawler/code


# ����code�ļ����ǹ���Ŀ¼

WORKDIR /code


# ��װ֧��

RUN pip install -r requirements.txt


CMD ["python", "/code/MerInfoCrawler/start.py"]
