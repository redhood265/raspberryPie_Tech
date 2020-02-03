# AlpineLinuxの最新版がインストールされる
FROM python:3.8.1-alpine

RUN apk update

# --no-cacheオプションを付けることで不要なキャッシュを削除できる
RUN apk add --no-cache curl bash bash-completion vim

RUN pip3 install --upgrade pip
RUN pip3 install flask 

WORKDIR /app

