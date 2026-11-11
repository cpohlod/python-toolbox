import argparse
import os
from moviepy import (
    VideoFileClip,
    ColorClip,
    TextClip,
    CompositeVideoClip,
    concatenate_videoclips
)
from moviepy.video.fx.FadeIn import FadeIn
from moviepy.video.fx.FadeOut import FadeOut

def obter_fonte(nome_preferido: str = "Arial") -> str:
    # Retorna o nome da fonte ou o caminho caso esteja no Windows
    if os.name == "nt":
        caminho_windows = f"C:/Windows/Fonts/{nome_preferido.lower()}.ttf"
        if os.path.exists(caminho_windows):
            return caminho_windows
    return nome_preferido

def renderizar_video(abertura_path: str, principal_path: str, saida_path: str, titulo_str: str, subtitulo_str: str):
    if not os.path.exists(abertura_path) or not os.path.exists(principal_path):
        print(f"[X] Erro: Certifique-se de que os arquivos de vídeo existem:\n - {abertura_path}\n - {principal_path}")
        return

    os.makedirs(os.path.dirname(saida_path) or ".", exist_ok=True)

    largura = 1920
    altura = 1080
    cor_fundo = (18, 26, 39)
    fonte_bold = obter_fonte("arialbd")
    fonte_regular = obter_fonte("arial")

    print("[*] Carregando e ajustando dimensões dos clipes base...")
    abertura = VideoFileClip(abertura_path).resized(height=altura)
    principal = VideoFileClip(principal_path).resized(height=altura)

    if abertura.w > largura:
        abertura = abertura.cropped(x_center=abertura.w / 2, width=largura)
    if principal.w > largura:
        principal = principal.cropped(x_center=principal.w / 2, width=largura)

    # 1. Tela de Título
    fundo_abertura = ColorClip(size=(largura, altura), color=cor_fundo, duration=4)
    clip_titulo = (
        TextClip(
            text=titulo_str,
            font=fonte_bold,
            font_size=80,
            color="white",
            text_align="center",
            method="caption",
            size=(1500, None)
        )
        .with_duration(4)
        .with_position(("center", "center"))
        .with_effects([FadeIn(1), FadeOut(1)])
    )
    clip_subtitulo = (
        TextClip(
            text=subtitulo_str,
            font=fonte_regular,
            font_size=38,
            color="lightgray",
            text_align="center",
            method="caption",
            size=(1200, None)
        )
        .with_duration(4)
        .with_position(("center", 720))
        .with_effects([FadeIn(1), FadeOut(1)])
    )
    tela_abertura = CompositeVideoClip([fundo_abertura, clip_titulo, clip_subtitulo], size=(largura, altura))

    # Transições
    abertura = abertura.with_effects([FadeIn(0.5), FadeOut(0.5)])
    principal = principal.with_effects([FadeIn(0.5), FadeOut(1.0)])

    print("[*] Concatenando linha do tempo...")
    video_final = concatenate_videoclips([tela_abertura, abertura, principal], method="compose")

    print(f"[*] Iniciando renderização em '{saida_path}'...")
    video_final.write_videofile(
        saida_path,
        codec="libx264",
        audio_codec="aac",
        fps=30,
        preset="medium"
    )
    print(f"[✓] Vídeo gerado com sucesso: {saida_path}")

def main():
    parser = argparse.ArgumentParser(description="Concatena vídeos com tela de abertura animada.")
    parser.add_argument("--intro", "-i", default="data/videos/abertura.mp4", help="Caminho do clipe de introdução")
    parser.add_argument("--main", "-m", default="data/videos/execucao.mp4", help="Caminho do clipe principal")
    parser.add_argument("--output", "-o", default="data/output/video_final.mp4", help="Caminho do arquivo final gerado")
    parser.add_argument("--title", "-t", default="ATIVIDADE PRÁTICA\nDE ATLETISMO", help="Texto do título principal")
    parser.add_argument("--subtitle", "-s", default="Bacharel em Educação Física", help="Texto do subtítulo")

    args = parser.parse_args()
    renderizar_video(args.intro, args.main, args.output, args.title, args.subtitle)

if __name__ == "__main__":
    main()