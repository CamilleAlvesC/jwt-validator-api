# 🔐 JWT Validator API (FastAPI)

Aplicação em **FastAPI** que valida um JWT conforme as regras do desafio:

* Deve ser um JWT válido (decodificável).
* Deve conter apenas 3 claims: `Name`, `Role`, `Seed`.

**Regras dos claims:**

* **Name**:

  * Não pode ter números.
  * Tamanho máximo: 256 caracteres.
* **Role**: deve ser um de: `Admin`, `Member`, `External`.
* **Seed**: deve ser um número primo.

**Saída esperada:**

```json
{"valido": true|false}
```

---

## 📖 Índice

* [Como rodar localmente](#-como-rodar-localmente)
* [Teste rápido (cURL)](#-teste-rápido-curl)
* [Endpoints](#-endpoints)
* [Testes](#-testes)
* [Requisitos](#-requisitos)
* [Infraestrutura / Deploy](#-infraestrutura--deploy)
* [CI/CD](#-cicd)
* [Observações](#-observações)
* [Commits](#-commits)

---

## 🚀 Como rodar localmente

### 1. Pré-requisitos

* Python 3.10+
* VS Code com extensões: **Python** e **Pylance**
* Docker (opcional para container)

### 2. Crie e ative um ambiente virtual

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash ou powershell
pip install -r requirements.txt
```

### 4. Suba o servidor

```bash ou powershell
uvicorn app.main:app --reload
```

A API estará disponível em:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## ✅ Teste rápido (cURL)

**Caso 1 → espera `true`:**

```bash
curl "http://127.0.0.1:8000/validate?token=eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJTZWVkIjoiNzg0MSIsIk5hbWUiOiJUb25pbmhvIEFyYXVqbyJ9.QY05sIjtrcJnP533kQNk8QXcaleJ1Q01jWY_ZzIZuAg"
```

**Caso 2 → espera `false`:**

```bash
curl "http://127.0.0.1:8000/validate?token=eyJhbGciOiJzI1NiJ9.dfsdfsfryJSr2xrIjoiQWRtaW4iLCJTZrkIjoiNzg0MSIsIk5hbrUiOiJUb25pbmhvIEFyYXVqbyJ9.QY05fsdfsIjtrcJnP533kQNk8QXcaleJ1Q01jWY_ZzIZuAg"
```

**Caso 3 → espera `false`:**

```bash
curl "http://127.0.0.1:8000/validate?token=eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiRXh0ZXJuYWwiLCJTZWVkIjoiODgwMzciLCJOYW1lIjoiTTRyaWEgT2xpdmlhIn0.6YD73XWZYQSSMDf6H0i3-kylz1-TY_Yt6h1cV2Ku-Qs"
```

**Caso 4 → espera `false`:**

```bash
curl "http://127.0.0.1:8000/validate?token=eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiTWVtYmVyIiwiT3JnIjoiQlIiLCJTZWVkIjoiMTQ2MjciLCJOYW1lIjoiVmFsZGlyIEFyYW5oYSJ9.cmrXV_Flm5mfdpfNUVopY_I2zeJUy4EZ4i3Fea98zvY"
```

---

## 🔎 Endpoints

* `GET /validate?token=<JWT>` → Retorna `{ "valido": true|false }`
* `GET /decode?token=<JWT>` → Retorna os claims em JSON (apenas para estudo)

---

## 🧪 Testes

Para rodar os testes unitários:

```bash ou powershell
pytest -v
```

---

## 🧰 Requisitos

* Python 3.10+
* fastapi
* uvicorn\[standard]
* pyjwt
* pytest
* Docker (opcional)

---

## 🏗 Infraestrutura / Deploy

* Aplicação containerizada com **Docker**.
* Deploy no **AWS ECS Fargate**.
* Terraform utilizado para provisionar **Cluster, Service e Task Definition**.
* Exemplo de IP público do ECS: `54.243.6.91`

---

## ⚙️ CI/CD

* Pipeline automatizado via **GitHub Actions** (ver `/.github/workflows/deploy.yml`)
* Build, teste e deploy da imagem Docker no ECS.
* Testes unitários executados antes do deploy.

---

## ⚠️ Observações

* Não validamos a assinatura do JWT porque a chave secreta não foi fornecida.
* O endpoint `/decode` é apenas didático → **não utilize em produção**.
* Observabilidade básica via logs Python (`logging.info`).
