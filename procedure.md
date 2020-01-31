# Dockerのコマンド

## ビルド

```cmd
docker-compose build
```

## 作成

```cmd
docker-compose create
```

## コンテナ開始

```cmd
docker-compose start
```

## コンテナたちを作成して開始(Create and Start)

```cmd
docker-compose up -d
```

### イメージ一覧

```cmd
docker-compose images
```

### コンテナ一覧

```cmd
docker-compose ps
```

### コンテナ内にログイン(以下からのコマンドは、コンテナで実行)

```cmd
docker container exec -it dev_docker_caitainer /bin/bash
```

