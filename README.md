# 💬 Chat Project com Django, DRF, GraphQL, OAuth e Celery

Projeto de chat em tempo real utilizando Django, Django Rest Framework, GraphQL, Channels, Redis, Celery e autenticação via Google OAuth.

## 🚀 Tecnologias Utilizadas

- 🐍 Django 4.2
- 🔗 Django Rest Framework (API REST)
- 🔥 Django Channels (WebSocket)
- 🌐 GraphQL (Graphene Django)
- 🗄️ PostgreSQL (Banco de Dados)
- ⚙️ Redis (Cache, Channels e Broker do Celery)
- 📦 Celery (Fila de tarefas assíncronas)
- 🌼 Flower (Monitoramento de tarefas Celery)
- 🔑 OAuth2 com django-allauth (Login social Google)
- 🐳 Docker e Docker Compose

---

## 📦 Estrutura do Projeto

infra/
│ ├── docker-compose.yml
chat_project/
│ ├── chat/ # App principal
│ ├── chat_project/ # Configurações do Django
│ ├── templates/ # Templates HTML
│ ├── staticfiles/ # Arquivos estáticos
│ ├── manage.py
├── Dockerfile
├── .env


---

## ⚙️ Configuração

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/reginaldo-castro/chat.git
cd /infra
docker-compose up --build
