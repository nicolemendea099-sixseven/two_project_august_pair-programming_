import tkinter as tk
from tkinter import messagebox

# Paleta de cores
COLOR_FUNDO   = "#10151c"  # Fundo da tela
COLOR_TEXTO   = "#e8edf2"  # Texto claro
COLOR_VERDE   = "#3ddc84"  # Botão Depositar
COLOR_ROSA    = "#ff5d73"  # Botão Sacar
COLOR_AMARELO = "#ffd166"  # Destaque do saldo
COLOR_AVISO   = "#8fa3b8"  # Texto do aviso (cinza-azulado, discreto)

# 1. Variável Global para controlar o saldo
saldo = 0.0

# 2. Funções auxiliares
def obter_valor():
    """Lê e valida o valor digitado, aceitando vírgula ou ponto decimal."""
    texto = ent_valor.get().strip().replace(",", ".")
    val = float(texto)  # pode lançar ValueError, tratado por quem chama
    if val <= 0:
        raise ValueError("valor deve ser maior que zero")
    return val

# 3. Funções de Manipulação do Saldo
def depositar():
    global saldo
    try:
        val = obter_valor()
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico maior que zero.")
        return
    saldo += val
    atualizar_saldo()

def sacar():
    global saldo
    try:
        val = obter_valor()
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico maior que zero.")
        return
    if val > saldo:
        messagebox.showwarning("Aviso", "Saldo insuficiente!")
    else:
        saldo -= val
        atualizar_saldo()

def atualizar_saldo():
    lbl_saldo.config(text=f"Saldo Atual: R$ {saldo:.2f}")
    ent_valor.delete(0, tk.END)
    ent_valor.focus()  # já deixa o campo pronto pra próxima digitação

# 4. Configuração da Janela Principal
janela = tk.Tk()
janela.title("Simulador de Rendas")
janela.geometry("380x330")
janela.configure(bg=COLOR_FUNDO)
janela.resizable(False, False)

# 5. Componentes da Interface (Visor de Saldo e Campo de Entrada)
lbl_saldo = tk.Label(
    janela,
    text="Saldo Atual: R$ 0.00",
    font=("Segoe UI", 16, "bold"),
    fg=COLOR_AMARELO,
    bg=COLOR_FUNDO,
)
lbl_saldo.pack(pady=20)

lbl_instrucao = tk.Label(
    janela, text="Valor da Operação (R$):", fg=COLOR_TEXTO, bg=COLOR_FUNDO
)
lbl_instrucao.pack()

ent_valor = tk.Entry(janela, font=("Segoe UI", 12), justify="center")
ent_valor.pack(pady=5)
ent_valor.focus()
ent_valor.bind("<Return>", lambda event: depositar())  # Enter = depositar

# 6. Painel de Botões
btn_frame = tk.Frame(janela, bg=COLOR_FUNDO)
btn_frame.pack(pady=15)

btn_depositar = tk.Button(
    btn_frame,
    text="Depositar (+)",
    bg=COLOR_VERDE,
    fg="#0b1f14",
    width=12,
    activebackground=COLOR_AMARELO,
    command=depositar,
)
btn_depositar.grid(row=0, column=0, padx=5)

btn_sacar = tk.Button(
    btn_frame,
    text="Sacar (-)",
    bg=COLOR_ROSA,
    fg="#2a0a0f",
    width=12,
    activebackground=COLOR_AMARELO,
    command=sacar,
)
btn_sacar.grid(row=0, column=1, padx=5)

# 7. Aviso de rodapé (estilo banco real)
lbl_aviso = tk.Label(
    janela,
    text="🔒 Nunca compartilhe sua senha ou dados bancários com terceiros.\nO banco nunca solicita isso por telefone ou mensagem.",
    font=("Segoe UI", 8),
    fg=COLOR_AVISO,
    bg=COLOR_FUNDO,
    wraplength=340,
    justify="center",
)
lbl_aviso.pack(side="bottom", pady=10)

# 8. Loop Principal
janela.mainloop()
activebackground=COLOR_AMARELO,
command=sacar,

btn_sacar.grid(row=0, column=1, padx=5)

# 7. Loop Principal
janela.mainloop()