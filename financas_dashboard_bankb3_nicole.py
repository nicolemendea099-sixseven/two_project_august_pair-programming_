import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

# ------------------------------------------------------------------
# 1. Paleta de Cores - Identidade B3
# ------------------------------------------------------------------
COLOR_BG            = "#0B2340"  # azul-marinho profundo (fundo geral)
COLOR_HEADER        = "#0A1F38"  # azul quase preto (header/topo)
COLOR_CARD          = "#FFFFFF"  # branco (cartões de conteúdo)
COLOR_CARD_ALT      = "#F4F6F9"  # cinza muito claro (linhas alternadas)
COLOR_AZUL_MED      = "#12406B"  # azul médio (bordas, textos secundários)
COLOR_AZUL_CLARO    = "#1E88C7"  # azul vivo (destaques, seleção)
COLOR_DOURADO       = "#D4AF37"  # dourado B3 (aba ativa, destaque cripto)
COLOR_DOURADO_ESC   = "#B8932E"  # dourado escuro (hover do dourado)
COLOR_VERDE         = "#2E9E5B"  # verde (entrada/sucesso)
COLOR_VERDE_ESC     = "#237A46"  # verde hover
COLOR_VERMELHO      = "#C0392B"  # vermelho (saída/alerta)
COLOR_VERMELHO_ESC  = "#9B2F22"  # vermelho hover
COLOR_TEXTO_ESC     = "#1B2A3B"  # texto escuro principal
COLOR_TEXTO_MUTED   = "#6B7A8F"  # texto secundário / cinza-azulado

FONT_TITULO   = ("Segoe UI", 16, "bold")
FONT_SUBTITULO = ("Segoe UI", 10)
FONT_LABEL    = ("Segoe UI", 11)
FONT_LABEL_B  = ("Segoe UI", 12, "bold")
FONT_SALDO    = ("Segoe UI", 20, "bold")
FONT_BTN      = ("Segoe UI", 10, "bold")
FONT_MONO     = ("Consolas", 10)

# ------------------------------------------------------------------
# 2. Variáveis Globais de Estado
# ------------------------------------------------------------------
saldo = 1000.00
cripto_btc = 0.0
COTACAO_BTC = 300000.0
historico = []  # cada item: (data, descricao, valor_str, tipo)


def _agora():
    return datetime.now().strftime("%d/%m %H:%M")


historico.append((_agora(), "Saldo inicial depositado", "+R$ 1000.00", "in"))


# ------------------------------------------------------------------
# 3. Funções de Atualização da Interface
# ------------------------------------------------------------------
def atualizar_extrato():
    tree_extrato.delete(*tree_extrato.get_children())
    for i, (data, desc, valor, tipo) in enumerate(reversed(historico)):
        tag = "par" if i % 2 == 0 else "impar"
        cor_tag = "in" if tipo == "in" else "out"
        tree_extrato.insert(
            "", tk.END, values=(data, desc, valor), tags=(tag, cor_tag)
        )


def atualizar_tudo():
    lbl_saldo_valor.config(text=f"R$ {saldo:,.2f}".replace(",", "."))
    lbl_btc_valor.config(text=f"{cripto_btc:.6f} BTC")
    lbl_btc_equiv.config(text=f"≈ R$ {cripto_btc * COTACAO_BTC:,.2f}".replace(",", "."))
    atualizar_extrato()


# ------------------------------------------------------------------
# 4. Funções das Operações Financeiras
# ------------------------------------------------------------------
def creditar():
    global saldo
    try:
        v = float(ent_valor_conta.get().replace(",", "."))
        if v <= 0:
            messagebox.showwarning("Aviso", "Digite um valor positivo.")
            return
        saldo += v
        historico.append((_agora(), "Depósito em conta", f"+R$ {v:.2f}", "in"))
        ent_valor_conta.delete(0, tk.END)
        atualizar_tudo()
    except ValueError:
        messagebox.showerror("Erro", "Valor inválido.")


def debitar():
    global saldo
    try:
        v = float(ent_valor_conta.get().replace(",", "."))
        if v <= 0:
            messagebox.showwarning("Aviso", "Digite um valor positivo.")
            return
        if v <= saldo:
            saldo -= v
            historico.append((_agora(), "Saque / Pagamento", f"-R$ {v:.2f}", "out"))
            ent_valor_conta.delete(0, tk.END)
            atualizar_tudo()
        else:
            messagebox.showwarning("Erro", "Saldo insuficiente.")
    except ValueError:
        messagebox.showerror("Erro", "Valor inválido.")


def comprar_btc():
    global saldo, cripto_btc
    custo = 100.00
    if saldo >= custo:
        saldo -= custo
        qtd = custo / COTACAO_BTC
        cripto_btc += qtd
        historico.append(
            (_agora(), f"Compra de Criptoativo ({qtd:.6f} BTC)", "-R$ 100.00", "out")
        )
        atualizar_tudo()
    else:
        messagebox.showwarning(
            "Erro", "Saldo insuficiente para comprar R$ 100,00 em BTC."
        )


# ------------------------------------------------------------------
# 5. Helpers de UI (botão com hover, cartão)
# ------------------------------------------------------------------
def criar_botao(parent, texto, bg, bg_hover, fg="white", **kwargs):
    btn = tk.Button(
        parent,
        text=texto,
        bg=bg,
        fg=fg,
        activebackground=bg_hover,
        activeforeground=fg,
        font=FONT_BTN,
        relief="flat",
        bd=0,
        cursor="hand2",
        padx=14,
        pady=8,
        **kwargs,
    )
    btn.bind("<Enter>", lambda e: btn.config(bg=bg_hover))
    btn.bind("<Leave>", lambda e: btn.config(bg=bg))
    return btn


def criar_card(parent, **kwargs):
    """Cartão branco com leve 'sombra' (moldura externa mais escura)."""
    wrapper = tk.Frame(parent, bg=COLOR_AZUL_MED)
    card = tk.Frame(wrapper, bg=COLOR_CARD, **kwargs)
    card.pack(padx=1, pady=1, fill="both", expand=True)
    return wrapper, card


# ------------------------------------------------------------------
# 6. Janela Principal e Estilização
# ------------------------------------------------------------------
janela = tk.Tk()
janela.title("Simulador Financeiro — Padrão B3")
janela.geometry("640x560")
janela.minsize(560, 480)
janela.configure(bg=COLOR_BG)

style = ttk.Style()
style.theme_use("default")

# --- Notebook (abas) ---
style.configure("TNotebook", background=COLOR_BG, borderwidth=0)
style.configure(
    "TNotebook.Tab",
    background=COLOR_AZUL_MED,
    foreground="#D7E3F0",
    padding=[18, 10],
    font=("Segoe UI", 10, "bold"),
    borderwidth=0,
)
style.map(
    "TNotebook.Tab",
    background=[("selected", COLOR_DOURADO)],
    foreground=[("selected", COLOR_TEXTO_ESC)],
    expand=[("selected", [0, 0, 0, 0])],
)
style.layout("TNotebook.Tab", [
    ("Notebook.tab", {"sticky": "nswe", "children": [
        ("Notebook.padding", {"side": "top", "sticky": "nswe", "children": [
            ("Notebook.label", {"side": "top", "sticky": ""})
        ]})
    ]})
])

# --- Treeview (extrato) ---
style.configure(
    "Extrato.Treeview",
    background=COLOR_CARD,
    fieldbackground=COLOR_CARD,
    foreground=COLOR_TEXTO_ESC,
    rowheight=28,
    font=FONT_MONO,
    borderwidth=0,
)
style.configure(
    "Extrato.Treeview.Heading",
    background=COLOR_AZUL_MED,
    foreground="white",
    font=("Segoe UI", 9, "bold"),
    relief="flat",
)
style.map("Extrato.Treeview.Heading", background=[("active", COLOR_AZUL_CLARO)])
style.map("Extrato.Treeview", background=[("selected", COLOR_AZUL_CLARO)],
          foreground=[("selected", "white")])

# ------------------------------------------------------------------
# 7. Header Superior
# ------------------------------------------------------------------
header = tk.Frame(janela, bg=COLOR_HEADER, height=72)
header.pack(fill="x")
header.pack_propagate(False)

faixa_dourada = tk.Frame(header, bg=COLOR_DOURADO, height=3)
faixa_dourada.pack(side="bottom", fill="x")

header_inner = tk.Frame(header, bg=COLOR_HEADER)
header_inner.pack(expand=True, fill="both", padx=20)

selo = tk.Label(
    header_inner, text="●", font=("Segoe UI", 22), fg=COLOR_DOURADO, bg=COLOR_HEADER
)
selo.pack(side="left", pady=10)

titulo_box = tk.Frame(header_inner, bg=COLOR_HEADER)
titulo_box.pack(side="left", padx=10, pady=10)

lbl_titulo = tk.Label(
    titulo_box,
    text="B3 · SIMULADOR FINANCEIRO",
    font=FONT_TITULO,
    fg="white",
    bg=COLOR_HEADER,
)
lbl_titulo.pack(anchor="w")

lbl_subtitulo = tk.Label(
    titulo_box,
    text="Conta corrente, criptoativos e extrato — ambiente simulado",
    font=FONT_SUBTITULO,
    fg="#9FB3C8",
    bg=COLOR_HEADER,
)
lbl_subtitulo.pack(anchor="w")

# ------------------------------------------------------------------
# 8. Estrutura de Abas (Notebook)
# ------------------------------------------------------------------
notebook_wrap = tk.Frame(janela, bg=COLOR_BG)
notebook_wrap.pack(fill="both", expand=True, padx=16, pady=16)

notebook = ttk.Notebook(notebook_wrap)
notebook.pack(fill="both", expand=True)

aba_conta = tk.Frame(notebook, bg=COLOR_BG)
aba_cripto = tk.Frame(notebook, bg=COLOR_BG)
aba_extrato = tk.Frame(notebook, bg=COLOR_BG)

notebook.add(aba_conta, text="  Conta Corrente  ")
notebook.add(aba_cripto, text="  Criptoativos  ")
notebook.add(aba_extrato, text="  Extrato  ")

# ------------------------------------------------------------------
# --- Aba 1: Conta Corrente ---
# ------------------------------------------------------------------
conta_pad = tk.Frame(aba_conta, bg=COLOR_BG)
conta_pad.pack(fill="both", expand=True, padx=14, pady=14)

card_saldo_wrap, card_saldo = criar_card(conta_pad)
card_saldo_wrap.pack(fill="x", pady=(0, 16))

saldo_inner = tk.Frame(card_saldo, bg=COLOR_CARD)
saldo_inner.pack(fill="x", padx=24, pady=20)

tk.Label(
    saldo_inner, text="SALDO DISPONÍVEL", font=("Segoe UI", 9, "bold"),
    fg=COLOR_TEXTO_MUTED, bg=COLOR_CARD,
).pack(anchor="w")

lbl_saldo_valor = tk.Label(
    saldo_inner, text=f"R$ {saldo:,.2f}".replace(",", "."),
    font=FONT_SALDO, fg=COLOR_AZUL_MED, bg=COLOR_CARD,
)
lbl_saldo_valor.pack(anchor="w", pady=(2, 0))

card_op_wrap, card_op = criar_card(conta_pad)
card_op_wrap.pack(fill="x")

op_inner = tk.Frame(card_op, bg=COLOR_CARD)
op_inner.pack(fill="x", padx=24, pady=20)

tk.Label(
    op_inner, text="Valor da operação (R$)", font=FONT_LABEL,
    fg=COLOR_TEXTO_ESC, bg=COLOR_CARD,
).pack(anchor="w", pady=(0, 6))

ent_valor_conta = tk.Entry(
    op_inner,
    font=("Segoe UI", 12),
    relief="flat",
    bd=0,
    highlightthickness=1,
    highlightbackground="#D6DEE8",
    highlightcolor=COLOR_AZUL_CLARO,
    bg="#F7F9FC",
    fg=COLOR_TEXTO_ESC,
    insertbackground=COLOR_TEXTO_ESC,
)
ent_valor_conta.pack(fill="x", ipady=8)

btn_frame = tk.Frame(op_inner, bg=COLOR_CARD)
btn_frame.pack(pady=(16, 0), anchor="w")

btn_entrada = criar_botao(btn_frame, "↑  Entrada", COLOR_VERDE, COLOR_VERDE_ESC, command=creditar)
btn_entrada.grid(row=0, column=0, padx=(0, 10))

btn_saida = criar_botao(btn_frame, "↓  Saída", COLOR_VERMELHO, COLOR_VERMELHO_ESC, command=debitar)
btn_saida.grid(row=0, column=1)

# ------------------------------------------------------------------
# --- Aba 2: Criptoativos ---
# ------------------------------------------------------------------
cripto_pad = tk.Frame(aba_cripto, bg=COLOR_BG)
cripto_pad.pack(fill="both", expand=True, padx=14, pady=14)

card_cripto_wrap, card_cripto = criar_card(cripto_pad)
card_cripto_wrap.pack(fill="both", expand=True)

cripto_inner = tk.Frame(card_cripto, bg=COLOR_CARD)
cripto_inner.pack(fill="both", expand=True, padx=24, pady=24)

topo_cripto = tk.Frame(cripto_inner, bg=COLOR_CARD)
topo_cripto.pack(fill="x")

tk.Label(
    topo_cripto, text="₿", font=("Segoe UI", 22, "bold"), fg=COLOR_DOURADO, bg=COLOR_CARD,
).pack(side="left")

txt_topo = tk.Frame(topo_cripto, bg=COLOR_CARD)
txt_topo.pack(side="left", padx=10)

tk.Label(
    txt_topo, text="Mercado Digital — Bitcoin (simulado)",
    font=FONT_LABEL_B, fg=COLOR_TEXTO_ESC, bg=COLOR_CARD,
).pack(anchor="w")

tk.Label(
    txt_topo, text=f"Cotação fixa: 1 BTC = R$ {COTACAO_BTC:,.2f}".replace(",", "."),
    font=("Segoe UI", 9, "italic"), fg=COLOR_TEXTO_MUTED, bg=COLOR_CARD,
).pack(anchor="w")

ttk.Separator(cripto_inner, orient="horizontal").pack(fill="x", pady=18)

saldo_btc_box = tk.Frame(cripto_inner, bg=COLOR_CARD_ALT)
saldo_btc_box.pack(fill="x", pady=(0, 20))

saldo_btc_inner = tk.Frame(saldo_btc_box, bg=COLOR_CARD_ALT)
saldo_btc_inner.pack(padx=18, pady=16, fill="x")

tk.Label(
    saldo_btc_inner, text="SEU SALDO EM BTC", font=("Segoe UI", 9, "bold"),
    fg=COLOR_TEXTO_MUTED, bg=COLOR_CARD_ALT,
).pack(anchor="w")

lbl_btc_valor = tk.Label(
    saldo_btc_inner, text=f"{cripto_btc:.6f} BTC",
    font=("Segoe UI", 18, "bold"), fg=COLOR_DOURADO_ESC, bg=COLOR_CARD_ALT,
)
lbl_btc_valor.pack(anchor="w")

lbl_btc_equiv = tk.Label(
    saldo_btc_inner, text=f"≈ R$ {cripto_btc * COTACAO_BTC:,.2f}".replace(",", "."),
    font=("Segoe UI", 10), fg=COLOR_TEXTO_MUTED, bg=COLOR_CARD_ALT,
)
lbl_btc_equiv.pack(anchor="w", pady=(2, 0))

btn_comprar_btc = criar_botao(
    cripto_inner, "Comprar R$ 100,00 em BTC", COLOR_DOURADO, COLOR_DOURADO_ESC,
    fg=COLOR_TEXTO_ESC, command=comprar_btc,
)
btn_comprar_btc.pack(anchor="w")

# ------------------------------------------------------------------
# --- Aba 3: Extrato ---
# ------------------------------------------------------------------
extrato_pad = tk.Frame(aba_extrato, bg=COLOR_BG)
extrato_pad.pack(fill="both", expand=True, padx=14, pady=14)

card_extrato_wrap, card_extrato = criar_card(extrato_pad)
card_extrato_wrap.pack(fill="both", expand=True)

extrato_inner = tk.Frame(card_extrato, bg=COLOR_CARD)
extrato_inner.pack(fill="both", expand=True, padx=4, pady=4)

cols = ("data", "descricao", "valor")
tree_extrato = ttk.Treeview(
    extrato_inner, columns=cols, show="headings", style="Extrato.Treeview"
)
tree_extrato.heading("data", text="Data")
tree_extrato.heading("descricao", text="Descrição")
tree_extrato.heading("valor", text="Valor")
tree_extrato.column("data", width=90, anchor="center")
tree_extrato.column("descricao", width=300, anchor="w")
tree_extrato.column("valor", width=110, anchor="e")

scroll_extrato = ttk.Scrollbar(extrato_inner, orient="vertical", command=tree_extrato.yview)
tree_extrato.configure(yscrollcommand=scroll_extrato.set)

tree_extrato.pack(side="left", fill="both", expand=True, padx=(12, 0), pady=12)
scroll_extrato.pack(side="right", fill="y", pady=12, padx=(0, 12))

tree_extrato.tag_configure("par", background=COLOR_CARD)
tree_extrato.tag_configure("impar", background=COLOR_CARD_ALT)
tree_extrato.tag_configure("in", foreground=COLOR_VERDE_ESC)
tree_extrato.tag_configure("out", foreground=COLOR_VERMELHO_ESC)

# ------------------------------------------------------------------
# 9. Inicialização
# ------------------------------------------------------------------
atualizar_tudo()

# Loop Principal
janela.mainloop()