import argparse
import os
from PIL import Image, ImageOps
import img2pdf

def processar_imagens(diretorio_entrada: str, diretorio_saida: str, nome_pdf: str, qualidade: int, max_dim: int):
    os.makedirs(diretorio_saida, exist_ok=True)
    extensoes_validas = ('.jpg', '.jpeg', '.png')
    
    arquivos = [f for f in os.listdir(diretorio_entrada) if f.lower().endswith(extensoes_validas)]
    arquivos.sort()

    if not arquivos:
        print(f"[!] Nenhuma imagem encontrada em '{diretorio_entrada}'.")
        return

    print(f"[*] Processando {len(arquivos)} imagens de '{diretorio_entrada}'...")
    imagens_comprimidas = []
    resolucao_maxima = (max_dim, max_dim)

    for arquivo in arquivos:
        caminho_entrada = os.path.join(diretorio_entrada, arquivo)
        nome_sem_ext = os.path.splitext(arquivo)[0]
        caminho_saida = os.path.join(diretorio_saida, f"{nome_sem_ext}_otimizada.jpg")

        try:
            with Image.open(caminho_entrada) as img:
                img = ImageOps.exif_transpose(img)
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                img.thumbnail(resolucao_maxima, Image.Resampling.LANCZOS)
                img.save(caminho_saida, "JPEG", quality=qualidade, optimize=True)
                
                imagens_comprimidas.append(caminho_saida)
                print(f"  -> Processada: {arquivo}")
        except Exception as e:
            print(f"  [X] Erro ao processar {arquivo}: {e}")

    if imagens_comprimidas:
        print("\n[*] Consolidando imagens no arquivo PDF...")
        caminho_pdf = os.path.join(diretorio_saida, nome_pdf)
        try:
            with open(caminho_pdf, "wb") as f:
                f.write(img2pdf.convert(imagens_comprimidas))
            tamanho_mb = os.path.getsize(caminho_pdf) / (1024 * 1024)
            print(f"[✓] Concluído com sucesso: '{caminho_pdf}' ({tamanho_mb:.2f} MB)")
        except Exception as e:
            print(f"[X] Falha na montagem do PDF: {e}")

def main():
    parser = argparse.ArgumentParser(description="Comprime imagens e gera um documento PDF único.")
    parser.add_argument("--input", "-i", default="data/images", help="Diretório contendo as imagens originais (default: data/images)")
    parser.add_argument("--output", "-o", default="data/output", help="Diretório de saída (default: data/output)")
    parser.add_argument("--pdf", "-p", default="documento_consolidado.pdf", help="Nome do arquivo PDF final (default: documento_consolidado.pdf)")
    parser.add_argument("--quality", "-q", type=int, default=75, help="Qualidade de compressão JPEG de 1 a 95 (default: 75)")
    parser.add_argument("--max-dim", type=int, default=1200, help="Dimensão máxima de largura/altura em pixels (default: 1200)")

    args = parser.parse_args()
    processar_imagens(args.input, args.output, args.pdf, args.quality, args.max_dim)

if __name__ == "__main__":
    main()