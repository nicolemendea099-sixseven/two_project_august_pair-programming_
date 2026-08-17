"""
Objetivo: Apresentar a história da primeira grande
investidora brasileira usando uma interface gráfica simples (tkinter).
 
Conceitos: História financeira do Brasil, diversificação
internacional no século XIX, interfaces visuais (GUI).
 
Dependências:
    pip install requests pillow
 
Paleta de cores — inspirada na Belle Époque parisiense que Eufrásia viveu:
    COLOR_FUNDO       = "#f4ede1"  # Creme / marfim (fundo da tela)
    COLOR_PAINEL      = "#fffdf8"  # Branco marfim (cartões e painéis)
    COLOR_TEXTO       = "#2c1a14"  # Marrom quase preto (texto principal)
    COLOR_VINHO       = "#7a1f2b"  # Vinho bordô (botões da linha do tempo)
    COLOR_VINHO_ESC   = "#5c1620"  # Vinho escuro (bordas / hover profundo)
    COLOR_DOURADO     = "#b8860b"  # Dourado envelhecido (destaques / hover)
    COLOR_AZUL_NOITE  = "#1d3557"  # Azul-marinho (botão de curiosidade)
    COLOR_BRANCO      = "#ffffff"
"""
 
import io
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox
 
 
def _instalar_dependencias(pacotes: list[str]) -> bool:
    """Tenta instalar pacotes ausentes usando o mesmo Python em execução."""
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", *pacotes]
        )
        return True
    except Exception as erro_instalacao:
        print(f"Falha ao instalar automaticamente: {erro_instalacao}")
        return False
 
 
try:
    import requests
    from PIL import Image, ImageTk
except ImportError:
    print("Dependências ausentes detectadas. Tentando instalar automaticamente...")
    print(f"Usando: {sys.executable}")
 
    sucesso = _instalar_dependencias(["requests", "pillow"])
 
    if sucesso:
        try:
            import requests
            from PIL import Image, ImageTk
            print("Dependências instaladas com sucesso!")
        except ImportError:
            sucesso = False
 
    if not sucesso:
        comando_manual = f"{sys.executable} -m pip install requests pillow"
        mensagem = (
            "Não foi possível instalar automaticamente as bibliotecas "
            "necessárias (requests e pillow).\n\n"
            "Abra o terminal e rode manualmente:\n\n"
            f"{comando_manual}\n\n"
            "Se o erro persistir, verifique sua conexão com a internet "
            "ou se o pip está atualizado (python -m pip install --upgrade pip)."
        )
        print("=" * 70)
        print(mensagem)
        print("=" * 70)
        try:
            _raiz_erro = tk.Tk()
            _raiz_erro.withdraw()
            messagebox.showerror("Dependência ausente", mensagem)
            _raiz_erro.destroy()
        except Exception:
            pass
        sys.exit(1)
 
# --------------------------------------------------------------------------
# Paleta de cores (centralizada para consistência em toda a interface)
# --------------------------------------------------------------------------
COLOR_FUNDO = "#f4ede1"
COLOR_PAINEL = "#fffdf8"
COLOR_TEXTO = "#2c1a14"
COLOR_VINHO = "#7a1f2b"
COLOR_VINHO_ESC = "#5c1620"
COLOR_DOURADO = "#b8860b"
COLOR_AZUL_NOITE = "#1d3557"
COLOR_BRANCO = "#ffffff"
 
URL_IMAGEM = (
    "https://upload.wikimedia.org/wikipedia/commons/4/40/"
    "Eufr%C3%A1sia_Teixeira_Leite_aos_30_anos_%282%29.jpg"
)
 
EVENTOS = {
    "1850 — Nascimento": (
        "Nasceu em Vassouras (RJ), no auge do ciclo do café, em uma das "
        "famílias mais ricas do Império."
    ),
    "1872 — Herança & Europa": (
        "Após perder os pais, mudou-se para Paris e assumiu a gestão da "
        "fortuna da família ainda jovem."
    ),
    "1873-1930 — Carteira Global": (
        "Investiu em títulos, ações e ferrovias em 13 países e 7 moedas "
        "diferentes, décadas antes do conceito de diversificação de "
        "carteira ser formalizado."
    ),
    "1899 — Perda da Irmã": (
        "Sua irmã e sócia de vida, Francisca Bernardina, faleceu em Paris. "
        "Eufrásia seguiu sozinha administrando a fortuna das duas."
    ),
    "1928 — Retorno ao Brasil": (
        "Depois de mais de 50 anos na Europa, voltou definitivamente ao "
        "Brasil, já reconhecida como uma das mulheres mais ricas do mundo."
    ),
    "1930 — Legado": (
        "Faleceu deixando parte de sua fortuna para causas sociais e "
        "educacionais no Brasil, incluindo bolsas de estudo para mulheres."
    ),
}
 
CURIOSIDADE_CASAMENTO = (
    "Eufrásia viveu por 14 anos um romance de idas e vindas com o "
    "abolicionista e escritor Joaquim Nabuco, chegando até a ficar noiva "
    "dele — mas nunca se casou.\n\n"
    "O motivo não foi falta de amor: pela lei brasileira da época, quando "
    "uma mulher se casava, a administração de todos os seus bens passava "
    "automaticamente para o marido. Como Eufrásia havia sido educada pelo "
    "próprio pai para gerir a fortuna da família, casar-se significaria "
    "perder o controle sobre tudo o que ela havia construído.\n\n"
    "Ela escolheu a independência financeira em vez do casamento — uma "
    "decisão rara e corajosa para uma mulher do século XIX."
)
 
 
class AppEufrasia:
    """Janela principal da apresentação sobre Eufrásia Teixeira Leite."""
 
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self._foto_referencia = None  # evita que o Tkinter descarte a imagem
 
        self._configurar_janela()
        self._montar_cabecalho()
        self._montar_imagem()
        self._montar_linha_do_tempo()
        self._montar_rodape()
 
    # ---------------------------------------------------------------- setup
    def _configurar_janela(self) -> None:
        self.root.title("História Financeira: Eufrásia Teixeira Leite")
        self.root.geometry("540x880")
        self.root.minsize(480, 700)
        self.root.configure(bg=COLOR_FUNDO)
 
    # ------------------------------------------------------------- widgets
    def _montar_cabecalho(self) -> None:
        frame = tk.Frame(self.root, bg=COLOR_FUNDO)
        frame.pack(fill="x", pady=(24, 4))
 
        tk.Label(
            frame,
            text="EUFRÁSIA TEIXEIRA LEITE",
            font=("Times New Roman", 24, "bold"),
            bg=COLOR_FUNDO,
            fg=COLOR_VINHO,
        ).pack()
 
        # Pequena linha decorativa dourada abaixo do título
        tk.Frame(frame, bg=COLOR_DOURADO, height=2, width=180).pack(pady=(6, 8))
 
        tk.Label(
            frame,
            text="A primeira investidora global do Brasil",
            font=("Georgia", 11, "italic"),
            bg=COLOR_FUNDO,
            fg=COLOR_TEXTO,
        ).pack()
 
    def _montar_imagem(self) -> None:
        moldura_externa = tk.Frame(self.root, bg=COLOR_DOURADO, padx=3, pady=3)
        moldura_externa.pack(pady=16)
 
        moldura_interna = tk.Frame(moldura_externa, bg=COLOR_PAINEL, padx=8, pady=8)
        moldura_interna.pack()
 
        foto = self._carregar_foto(URL_IMAGEM, tamanho=(150, 188))
 
        if foto is not None:
            self._foto_referencia = foto
            tk.Label(moldura_interna, image=foto, bg=COLOR_PAINEL).pack()
        else:
            tk.Label(
                moldura_interna,
                text="[Retrato indisponível\nsem conexão com a internet]",
                font=("Georgia", 9, "italic"),
                fg=COLOR_VINHO,
                bg=COLOR_PAINEL,
                width=22,
                height=9,
                justify="center",
            ).pack()
 
    def _montar_linha_do_tempo(self) -> None:
        tk.Label(
            self.root,
            text="LINHA DO TEMPO",
            font=("Georgia", 12, "bold"),
            bg=COLOR_FUNDO,
            fg=COLOR_VINHO,
        ).pack(pady=(6, 0))
 
        tk.Label(
            self.root,
            text="clique em um evento para saber mais",
            font=("Georgia", 9, "italic"),
            bg=COLOR_FUNDO,
            fg=COLOR_TEXTO,
        ).pack(pady=(0, 10))
 
        frame_botoes = tk.Frame(self.root, bg=COLOR_FUNDO)
        frame_botoes.pack(fill="x", padx=36)
 
        for data, detalhe in EVENTOS.items():
            btn = tk.Button(
                frame_botoes,
                text=data,
                font=("Georgia", 11, "bold"),
                bg=COLOR_VINHO,
                fg=COLOR_BRANCO,
                activebackground=COLOR_DOURADO,
                activeforeground=COLOR_TEXTO,
                relief="flat",
                bd=0,
                cursor="hand2",
                command=lambda d=detalhe, t=data: self._mostrar_fato(t, d),
            )
            btn.pack(fill="x", pady=5, ipady=7)
            self._aplicar_efeito_hover(btn, cor_normal=COLOR_VINHO)
 
        self._montar_botao_curiosidade(frame_botoes)
 
    def _montar_botao_curiosidade(self, frame_pai: tk.Frame) -> None:
        tk.Frame(frame_pai, bg=COLOR_DOURADO, height=1).pack(fill="x", pady=(14, 12))
 
        tk.Label(
            frame_pai,
            text="✦  CURIOSIDADE  ✦",
            font=("Georgia", 10, "bold"),
            bg=COLOR_FUNDO,
            fg=COLOR_DOURADO,
        ).pack(pady=(0, 6))
 
        btn_curiosidade = tk.Button(
            frame_pai,
            text="Por que ela nunca se casou no Brasil?",
            font=("Georgia", 11, "bold"),
            bg=COLOR_AZUL_NOITE,
            fg=COLOR_BRANCO,
            activebackground=COLOR_DOURADO,
            activeforeground=COLOR_TEXTO,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=lambda: self._mostrar_fato(
                "Por que ela nunca se casou?", CURIOSIDADE_CASAMENTO
            ),
        )
        btn_curiosidade.pack(fill="x", pady=5, ipady=8)
        self._aplicar_efeito_hover(btn_curiosidade, cor_normal=COLOR_AZUL_NOITE)
 
    def _montar_rodape(self) -> None:
        tk.Frame(self.root, bg=COLOR_DOURADO, height=1).pack(fill="x", side="bottom")
        tk.Label(
            self.root,
            text="Fonte: Wikipédia  •  Projeto de história financeira do Brasil",
            font=("Georgia", 8),
            bg=COLOR_FUNDO,
            fg=COLOR_TEXTO,
        ).pack(side="bottom", pady=8)
 
    # -------------------------------------------------------------- ações
    @staticmethod
    def _mostrar_fato(titulo: str, detalhe: str) -> None:
        messagebox.showinfo(f"Curiosidade — {titulo}", detalhe)
 
    @staticmethod
    def _aplicar_efeito_hover(botao: tk.Button, cor_normal: str) -> None:
        def ao_entrar(_evento):
            botao.configure(bg=COLOR_DOURADO, fg=COLOR_TEXTO)
 
        def ao_sair(_evento):
            botao.configure(bg=cor_normal, fg=COLOR_BRANCO)
 
        botao.bind("<Enter>", ao_entrar)
        botao.bind("<Leave>", ao_sair)
 
    @staticmethod
    def _carregar_foto(url: str, tamanho: tuple[int, int]):
        """Baixa e processa a imagem; retorna None em caso de falha."""
        try:
            headers = {
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36"
                )
            }
            resposta = requests.get(url, headers=headers, timeout=6)
            resposta.raise_for_status()
 
            imagem_pil = Image.open(io.BytesIO(resposta.content))
            imagem_pil = imagem_pil.resize(tamanho, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(imagem_pil)
 
        except Exception as erro:  # rede indisponível, URL inválida, etc.
            print(f"[Aviso] Não foi possível carregar a imagem: {erro}")
            return None
 
 
def main() -> None:
    janela = tk.Tk()
    AppEufrasia(janela)
    janela.mainloop()
 
 
if __name__ == "__main__":
    main()