# 🌤️ Dashboard de Previsão do Tempo - Brasil

Um dashboard interativo em Python/Flask que exibe dados meteorológicos em tempo real para todos os estados do Brasil.

## 📋 Características

- **Interface moderna e responsiva** com design em gradiente
- **Dados em tempo real** usando a API Open-Meteo (gratuita)
- **Visualizações interativas** com Chart.js
- **Cobertura completa** dos 27 estados brasileiros
- **Previsão de 5 dias** para cada estado
- **Visão geral nacional** com estatísticas agregadas
- **Design mobile-friendly** que se adapta a diferentes telas

## 🚀 Funcionalidades

### 📊 Dados Meteorológicos
- Temperatura atual
- Umidade relativa
- Velocidade do vento
- Precipitação
- Descrição das condições climáticas

### 📈 Visualizações
- Cards individuais para cada estado
- Gráfico de barras comparativo (temperatura e umidade)
- Previsão estendida de 5 dias
- Estatísticas nacionais (média, máxima, mínima)

### 🎛️ Controles
- Seleção individual de estados
- Carregamento de todos os estados
- Botão de atualização dos dados
- Interface intuitiva e responsiva

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3.11, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Visualização**: Chart.js
- **API**: Open-Meteo (dados meteorológicos gratuitos)
- **Banco de dados**: SQLite (opcional, já configurado)

## 📦 Instalação

### Pré-requisitos
- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)

### Passos de instalação

1. **Clone ou baixe o projeto**
   ```bash
   # Se usando git
   git clone <url-do-repositorio>
   cd weather_dashboard
   ```

2. **Ative o ambiente virtual**
   ```bash
   source venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação**
   ```bash
   python src/main.py
   ```

5. **Acesse o dashboard**
   - Abra seu navegador
   - Vá para: `http://localhost:5000`

## 🎯 Como Usar

### Visualizar um Estado Específico
1. Selecione um estado no dropdown
2. Clique em "Carregar Estado"
3. Visualize os dados meteorológicos e previsão

### Visualizar Todos os Estados
1. Clique em "Carregar Todos os Estados"
2. Aguarde o carregamento (pode levar alguns segundos)
3. Explore a visão geral e os cards individuais

### Atualizar Dados
- Use o botão "🔄 Atualizar" para obter dados mais recentes

## 📁 Estrutura do Projeto

```
weather_dashboard/
├── src/
│   ├── main.py              # Arquivo principal da aplicação Flask
│   ├── routes/
│   │   ├── weather.py       # Rotas da API de clima
│   │   └── user.py          # Rotas de usuário (template)
│   ├── models/
│   │   └── user.py          # Modelos de banco de dados
│   ├── static/
│   │   └── index.html       # Interface do dashboard
│   └── database/
│       └── app.db           # Banco de dados SQLite
├── venv/                    # Ambiente virtual Python
├── requirements.txt         # Dependências do projeto
└── README.md               # Este arquivo
```

## 🔧 API Endpoints

### Estados
- `GET /api/states` - Lista todos os estados brasileiros

### Clima
- `GET /api/weather/<codigo_estado>` - Dados de um estado específico
- `GET /api/weather/all` - Dados de todos os estados

### Exemplo de Resposta
```json
{
  "success": true,
  "state": {
    "name": "São Paulo",
    "capital": "São Paulo",
    "lat": -23.5505,
    "lon": -46.6333
  },
  "weather": {
    "current": {
      "temperature": 23.6,
      "humidity": 60,
      "wind_speed": 5.4,
      "precipitation": 0.0,
      "description": "Céu limpo"
    },
    "forecast": [...]
  }
}
```

## 🌐 Fonte dos Dados

Os dados meteorológicos são obtidos da **Open-Meteo API**, uma API gratuita e confiável que fornece:
- Dados meteorológicos em tempo real
- Previsões precisas
- Cobertura global
- Sem necessidade de chave de API
- Atualizações regulares

## 🎨 Personalização

### Modificar Cores
Edite as variáveis CSS no arquivo `src/static/index.html`:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Adicionar Novos Estados/Cidades
Modifique o dicionário `BRAZILIAN_STATES` em `src/routes/weather.py`.

### Alterar Período de Previsão
Ajuste o parâmetro `forecast_days` na função `get_weather_data_openmeteo()`.

## 🚀 Deploy

### Opção 1: Servidor Local
```bash
python src/main.py
# Acesse: http://localhost:5000
```

### Opção 2: Servidor de Produção
Para produção, use um servidor WSGI como Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 src.main:app
```

## 🐛 Solução de Problemas

### Erro de Conexão com a API
- Verifique sua conexão com a internet
- A API Open-Meteo pode estar temporariamente indisponível

### Dados não Carregam
- Aguarde alguns segundos (a API pode demorar para responder)
- Tente atualizar a página
- Verifique o console do navegador para erros

### Erro de Dependências
```bash
# Reinstale as dependências
pip install -r requirements.txt --force-reinstall
```

## 📱 Compatibilidade

- **Navegadores**: Chrome, Firefox, Safari, Edge (versões recentes)
- **Dispositivos**: Desktop, tablet, smartphone
- **Sistemas**: Windows, macOS, Linux

## 🤝 Contribuição

Para contribuir com o projeto:
1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Implemente suas mudanças
4. Teste thoroughly
5. Envie um pull request

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

## 👨‍💻 Autor

Desenvolvido com ❤️ usando Python e Flask.

---

**Nota**: Este dashboard foi criado para fins educacionais e demonstrativos. Os dados meteorológicos são fornecidos pela Open-Meteo API e podem ter pequenas variações em relação a outras fontes.

