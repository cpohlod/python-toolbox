# Python Toolbox

Coleção de ferramentas e utilitários em Python para manipulação de mídia, documentos e automações locais.

## 📁 Estrutura

```text
tools/         -> Scripts utilitários modulares (CLI)
data/          -> Diretório para insumos e arquivos de teste (ignorado pelo Git)
  ├── images/  -> Imagens para teste
  ├── videos/  -> Clipes para teste
  └── output/  -> Arquivos finais gerados
```

---
## 🛠️ Ferramentas Disponíveis

---

### 1. Compressor de Imagens e Gerador de PDF (`tools/comprimir_imagens.py`)

Lê imagens de um diretório, corrige a orientação fotográfica (baseada nas tags EXIF de celulares), converte perfis de cor, redimensiona, aplica compressão JPEG otimizada e compila todos os itens em um único arquivo PDF.

#### Parâmetros aceitos:
| Argumento | Flag Curta | Padrão | Descrição |
| :--- | :--- | :--- | :--- |
| `--input` | `-i` | `data/images` | Diretório de origem das imagens |
| `--output` | `-o` | `data/output` | Diretório onde os arquivos serão salvos |
| `--pdf` | `-p` | `documento_consolidado.pdf` | Nome do arquivo PDF gerado |
| `--quality` | `-q` | `75` | Qualidade JPEG (escala de 1 a 95) |
| `--max-dim` | | `1200` | Dimensão máxima (largura/altura em px) |

#### Exemplos de Uso:

* **Execução Padrão:**  
  Basta soltar suas imagens na pasta `data/images/` e executar:
  ```bash
  python tools/comprimir_imagens.py
  ```
  *O script lerá `data/images/`, salvará as cópias comprimidas em `data/output/` e criará `data/output/documento_consolidado.pdf`.*

* **Execução Customizada 1 (Documento em alta resolução para impressão):**
  ```bash
  python tools/comprimir_imagens.py -i "C:/Users/Usuario/Documentos/Contratos" -o "./saida_alta" -p "Contrato_Assinado.pdf" -q 85 --max-dim 1800
  ```

* **Execução Customizada 2 (Arquivo superleve para upload em formulários):**
  ```bash
  python tools/comprimir_imagens.py -i ./fotos_carteira -o ./envio -p "documentos_leves.pdf" -q 50 --max-dim 800
  ```

---

### 2. Concatenador de Vídeos com Abertura Animada (`tools/juntar_videos.py`)

Ajusta a proporção e resolução dos vídeos para Full HD (1920x1080 com recorte central inteligente), gera cartões de abertura animados com tipografia customizada, aplica transições em *fade* e renderiza um vídeo final compilado.

#### Parâmetros aceitos:
| Argumento | Flag Curta | Padrão | Descrição |
| :--- | :--- | :--- | :--- |
| `--intro` | `-i` | `data/videos/abertura.mp4` | Caminho do vídeo introdutório |
| `--main` | `-m` | `data/videos/execucao.mp4` | Caminho do vídeo principal/conteúdo |
| `--output` | `-o` | `data/output/video_final.mp4` | Caminho completo do arquivo de saída |
| `--title` | `-t` | `"ATIVIDADE PRÁTICA\nDE ATLETISMO"` | Texto principal do cartão de abertura |
| `--subtitle` | `-s` | `"Bacharel em Educação Física"` | Subtítulo do cartão de abertura |

#### Exemplos de Uso:

* **Execução Padrão:**  
  Coloque os arquivos `abertura.mp4` e `execucao.mp4` dentro de `data/videos/` e rode:
  ```bash
  python tools/juntar_videos.py
  ```
  *O resultado será renderizado em `data/output/video_final.mp4` com as legendas padrão.*

* **Execução Customizada 1 (Apresentação acadêmica ou trabalho escolar):**
  ```bash
  python tools/juntar_videos.py \
    -i ./gravacoes/vinheta_faculdade.mp4 \
    -m ./gravacoes/seminario_parte1.mp4 \
    -o ./entregas/Seminario_Final.mp4 \
    -t "SEMINÁRIO DE REDES II\nGRUPO 04" \
    -s "Ciência da Computação - 2026"
  ```

* **Execução Customizada 2 (Canal de tutoriais ou redes sociais):**
  ```bash
  python tools/juntar_videos.py -i intro_curta.mp4 -m gameplay.mp4 -o ep01_pronto.mp4 -t "TUTORIAL COMPLETO\nPYTHON PARA INICIANTES" -s "Episódio 01"
  ```

---