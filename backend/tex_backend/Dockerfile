
FROM python:3.8-alpine
LABEL maintainer = "kushal@thirdeyedata.io"
RUN apk add --no-cache python3-dev py3-setuptools\
   # && apk add --no-cache --update python3 \
    && apk add --no-cache jpeg-dev zlib-dev \
    && apk add --no-cache --virtual .build-deps build-base linux-headers \
    && apk add --no-cache py3-pip \
    && pip3 install --upgrade pip \
    && pip3 install --upgrade pillow \
    && apk add mysql-client\
    && apk add --no-cache default-libmysqlclient-dev
   # && pip3 install --upgrade setuptools 
    # && apk add gcc 
    # && apk add libc-dev 
    # && apk add linux-headers
#RUN apk update \
 #   && apk add --virtual build-deps gcc python3-dev musl-dev \
  #  && pip3 install psycopg2 \
   # && apk add jpeg-dev zlib-dev libjpeg \
   # && pip3 install Pillow \
   # && apk del build-deps
    
# RUN mkdir /usr/local/app/
ARG USER_HOME=/usr/local/app/
WORKDIR ${USER_HOME}
COPY . ${USER_HOME}
RUN apk add --update --no-cache g++ gcc libxslt-dev
RUN pip3 --no-cache-dir install -r requirements.txt
# RUN pip install mysqlclient  
# RUN apk del build-deps
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
ENTRYPOINT ["python3","manage.py","runserver", "0.0.0.0:8000"]
EXPOSE 8000