# Script de Deploy - Recepção Enfermagem
# Para executar: .\deploy.ps1

Write-Host "🚀 Iniciando deploy da Recepção Enfermagem..." -ForegroundColor Green

# Parar containers existentes
Write-Host "⏹️  Parando containers existentes..." -ForegroundColor Yellow
docker compose down

# Limpar volumes se necessário
Write-Host "🧹 Limpando volumes antigos..." -ForegroundColor Yellow
docker volume prune -f

# Build e iniciar
Write-Host "🔨 Construindo e iniciando containers..." -ForegroundColor Yellow
docker compose up -d --build

# Aguardar inicialização
Write-Host "⏳ Aguardando inicialização..." -ForegroundColor Yellow
Start-Sleep -Seconds 15

# Verificar status
Write-Host "📊 Status dos containers:" -ForegroundColor Cyan
docker compose ps

# Teste de conectividade
Write-Host "🔍 Testando conectividade..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8010" -UseBasicParsing -TimeoutSec 10
    if ($response.StatusCode -in @(200, 302, 403)) {
        Write-Host "✅ Recepção Enfermagem está rodando em http://localhost:8010" -ForegroundColor Green
    }
} catch {
    Write-Host "❌ Erro na inicialização. Verificando logs:" -ForegroundColor Red
    docker compose logs --tail=20
}

Write-Host "🏁 Deploy concluído!" -ForegroundColor Green
Write-Host "🌐 Acesse: http://localhost:8010" -ForegroundColor Cyan