# Use uma imagem oficial do Python como base
FROM python:3.9-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o arquivo de dependências para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código fonte para o diretório de trabalho
COPY . .

# Torne a porta 5000 disponível para o mundo fora deste container
EXPOSE 5000

# Execute a aplicação
CMD ["python", "main.py"]
