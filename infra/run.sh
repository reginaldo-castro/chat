#!/bin/bash
set -e

# Espera o banco ficar disponível
echo "Esperando o banco iniciar..."
while ! nc -z db 5432; do
  sleep 1
done

echo "==> Verificando se o projeto Django já foi criado..."

if [ ! -d "chat_project" ]; then
    echo "==> Criando o projeto Django..."
    django-admin startproject chat_project .
else
    echo "==> Projeto já existe. Pulando criação."
fi

echo "==> Aplicando migrações iniciais..."
python manage.py migrate

echo "==> Corrigindo permissões de arquivos para UID 1000..."
chown -R 1000:1000 /app

# # echo "==> Iniciando servidor Django na porta 8000..."
# python manage.py runserver 0.0.0.0:8000
echo "==> Iniciando servidor ASGI com Daphne na porta 8000..."
daphne -b 0.0.0.0 -p 8000 chat_project.asgi:application