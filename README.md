# Sistema de Recepção Enfermagem

Sistema Django para gestão hospitalar com foco em enfermagem, controle de cirurgias seguras e tratamentos quimioterápicos.

## 🚀 Deploy

### Requisitos
- Docker
- Docker Compose
- Git

### Deploy Local

1. Clone o repositório:
```bash
git clone https://github.com/LeonardoVieiraGuimaraes/hospital-enfermagem-django.git
cd hospital-enfermagem-django
```

2. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

3. Execute o deploy:
```bash
./deploy.sh
```

Ou manualmente:
```bash
docker compose up -d --build
```

### Deploy em Produção

O sistema está configurado para deploy automático via GitHub Actions para o servidor em `recepcao-enfermagem-django/`.

#### Configurações necessárias no servidor:

1. **Nginx Configuration** (exemplo):
```nginx
server {
    listen 80;
    server_name seu-dominio.com;
    
    location / {
        proxy_pass http://localhost:8003;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    location /static/ {
        alias /home/leonardovieiraxy/projetos/recepcao-enfermagem-django/staticfiles/;
    }
}
```

2. **Estrutura de pastas no servidor**:
```
/home/leonardovieiraxy/projetos/
└── recepcao-enfermagem-django/
    ├── manage.py
    ├── docker-compose.yaml
    ├── Dockerfile-python-gunicorn
    └── ...
```

## 🔧 Desenvolvimento

### Comandos úteis:
```bash
# Executar migrações
docker compose exec recepcao-enfermagem python manage.py migrate

# Criar superusuário
docker compose exec recepcao-enfermagem python manage.py createsuperuser

# Visualizar logs
docker compose logs -f recepcao-enfermagem

# Reiniciar apenas a aplicação
docker compose restart recepcao-enfermagem
```

## 📊 Monitoramento

- **URL**: http://localhost:8003
- **Admin**: http://localhost:8003/admin
- **Healthcheck**: Configurado no docker-compose

## 🛠️ Tecnologias

- **Backend**: Django 4.2.3
- **Frontend**: Bootstrap 5, Select2
- **Database**: SQLite3 (desenvolvimento)
- **Server**: Gunicorn
- **Containerização**: Docker + Docker Compose
- **Deploy**: GitHub Actions + Cloudflare Tunnel

## 📁 Estrutura do Projeto

```
hospital-enfermagem-django/
├── hospital/           # Configurações Django
├── main/              # App principal
├── usuario/           # Gestão de usuários
├── questionario/      # Questionários e formulários
├── templates/         # Templates HTML
├── static/           # Arquivos estáticos
└── .github/workflows/ # CI/CD
```