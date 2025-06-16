#!/bin/bash
set -e

DB_HOST=${DB_HOST:-db}
DB_PORT=${DB_PORT:-5432}

echo "🟦 Aguardando o banco de dados em $DB_HOST:$DB_PORT..."
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
done
echo "✅ Banco de dados disponível!"

# Remover essa etapa — o projeto já deve estar criado antes
# if [ ! -d "chat_project" ]; then
#     echo "🚀 Criando o projeto Django..."
#     django-admin startproject chat_project .
# else
#     echo "📁 Projeto Django já existe. Pulando criação."
# fi

echo "⚙️ Aplicando migrações..."
python manage.py migrate --noinput

echo "📜 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "🔐 Corrigindo permissões de arquivos..."
chown -R 1000:1000 /app

echo "🚀 Iniciando servidor ASGI com Daphne na porta 8000..."
daphne -b 0.0.0.0 -p 8000 chat_project.asgi:application
