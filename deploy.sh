#!/bin/bash

echo "🚀 Iniciando deploy da Recepção Enfermagem..."

# Parar containers existentes
echo "⏹️  Parando containers existentes..."
docker compose down

# Limpar cache do Docker se necessário
echo "🧹 Limpando cache..."
docker system prune -f

# Build e iniciar
echo "🔨 Construindo e iniciando containers..."
docker compose up -d --build

# Aguardar inicialização
echo "⏳ Aguardando inicialização..."
sleep 10

# Verificar status
echo "📊 Status dos containers:"
docker compose ps

# Teste de conectividade
echo "🔍 Testando conectividade..."
if curl -s -o /dev/null -w "%{http_code}" http://localhost:8010 | grep -q "200\|302\|403"; then
  echo "✅ Recepção Enfermagem está rodando em http://localhost:8010"
else
  echo "❌ Erro na inicialização. Verificando logs:"
  docker compose logs --tail=20
fi

echo "🏁 Deploy concluído!"