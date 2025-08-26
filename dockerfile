# Imagem base
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia todos os arquivos para dentro do container
COPY ./ ./

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta da API
EXPOSE 8000

# Comando para rodar a API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
