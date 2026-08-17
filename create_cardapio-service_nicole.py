import json
import os
import tkinter as tk
from datetime import datetime
from tkinter import filedialog, messagebox, ttk
 
PALETA_CLARA = {
    "fundo": "#f8f9fa", "painel": "#ffffff", "texto": "#212529", "subtexto": "#6c757d",
    "primaria": "#b45309", "verde": "#16a34a", "vermelho": "#dc2626", "amarelo": "#eab308",
    "borda": "#e5e7eb",
}
 
PALETA_ESCURA = {
    "fundo": "#121212", "painel": "#1e1e2e", "texto": "#ffffff", "subtexto": "#a1a1aa",
    "primaria": "#f59e0b", "verde": "#22c55e", "vermelho": "#ef4444", "amarelo": "#eab308",
    "borda": "#3f3f46",
}
 
cores = PALETA_CLARA
modo_escuro = False
 
CARDAPIO = {
    "🍞 Pães": [
        {"id": 101, "nome": "Pão Francês (unid.)", "preco": 0.9, "desc": "Pãozinho crocante por fora e macio por dentro, assado na hora.", "estoque": 100},
        {"id": 102, "nome": "Pão de Forma", "preco": 12.9, "desc": "Pão de forma tradicional, fatiado.", "estoque": 25},
        {"id": 103, "nome": "Pão Integral", "preco": 13.9, "desc": "Pão 100% integral, rico em fibras.", "estoque": 25},
        {"id": 104, "nome": "Pão de Queijo (unid.)", "preco": 3.5, "desc": "Pãozinho de queijo mineiro, quentinho e macio.", "estoque": 60},
        {"id": 105, "nome": "Baguete", "preco": 9.9, "desc": "Baguete francesa longa e crocante.", "estoque": 30},
        {"id": 106, "nome": "Brioche", "preco": 11.9, "desc": "Pão amanteigado, macio e levemente adocicado.", "estoque": 25},
    ],
    "🥐 Salgados": [
        {"id": 201, "nome": "Coxinha", "preco": 9.5, "desc": "Massa cremosa recheada com frango desfiado.", "estoque": 35},
        {"id": 202, "nome": "Esfiha", "preco": 8.5, "desc": "Massa fina aberta com recheio de carne temperada.", "estoque": 30},
        {"id": 203, "nome": "Empada", "preco": 9.9, "desc": "Massa amanteigada recheada com frango e catupiry.", "estoque": 20},
        {"id": 204, "nome": "Risole", "preco": 8.9, "desc": "Massa empanada recheada com presunto e queijo.", "estoque": 30},
        {"id": 205, "nome": "Quibe", "preco": 8.9, "desc": "Frito, recheado com carne moída temperada.", "estoque": 25},
        {"id": 206, "nome": "Enroladinho de Salsicha", "preco": 7.9, "desc": "Massa folhada enrolada com salsicha.", "estoque": 35},
    ],
    "🍰 Bolos e tortas": [
        {"id": 301, "nome": "Bolo de Chocolate (fatia)", "preco": 10.9, "desc": "Fatia generosa de bolo de chocolate com cobertura cremosa.", "estoque": 20},
        {"id": 302, "nome": "Bolo de Cenoura (fatia)", "preco": 10.5, "desc": "Clássico bolo de cenoura com calda de chocolate.", "estoque": 20},
        {"id": 303, "nome": "Bolo de Fubá (fatia)", "preco": 9.9, "desc": "Bolo caseiro de fubá, macio e levemente doce.", "estoque": 20},
        {"id": 304, "nome": "Torta de Limão (fatia)", "preco": 12.9, "desc": "Base crocante, creme de limão e merengue maçaricado.", "estoque": 15},
        {"id": 305, "nome": "Torta de Chocolate (fatia)", "preco": 13.5, "desc": "Fatia cremosa com base crocante e chocolate ao leite.", "estoque": 15},
        {"id": 306, "nome": "Cheesecake (fatia)", "preco": 14.9, "desc": "Base de biscoito, creme de queijo e calda de frutas vermelhas.", "estoque": 15},
    ],
    "🍮 Doces": [
        {"id": 401, "nome": "Brigadeiro (unid.)", "preco": 4.5, "desc": "Brigadeiro artesanal enrolado na hora.", "estoque": 60},
        {"id": 402, "nome": "Beijinho (unid.)", "preco": 4.5, "desc": "Docinho de coco enrolado na hora.", "estoque": 60},
        {"id": 403, "nome": "Pudim (fatia)", "preco": 8.9, "desc": "Pudim de leite condensado cremoso, com calda de caramelo.", "estoque": 20},
        {"id": 404, "nome": "Brownie (unid.)", "preco": 7.9, "desc": "Brownie de chocolate denso e úmido.", "estoque": 30},
        {"id": 405, "nome": "Cookie (unid.)", "preco": 6.5, "desc": "Cookie amanteigado com gotas de chocolate.", "estoque": 40},
        {"id": 406, "nome": "Sonho (unid.)", "preco": 7.9, "desc": "Massa fofinha frita, recheada com creme de confeiteiro.", "estoque": 25},
    ],
    "☕ Bebidas": [
        {"id": 501, "nome": "Café Expresso", "preco": 5.5, "desc": "Café expresso tradicional, servido na hora.", "estoque": 100},
        {"id": 502, "nome": "Café com Leite", "preco": 7.0, "desc": "Café coado com leite vaporizado.", "estoque": 100},
        {"id": 503, "nome": "Cappuccino", "preco": 8.5, "desc": "Café espresso, leite vaporizado e espuma cremosa.", "estoque": 100},
        {"id": 504, "nome": "Chocolate Quente", "preco": 9.5, "desc": "Bebida cremosa feita com chocolate meio amargo.", "estoque": 40},
        {"id": 505, "nome": "Suco de Laranja 400ml", "preco": 9.9, "desc": "Suco espremido na hora, sem açúcar.", "estoque": 30},
        {"id": 506, "nome": "Suco de Maracujá 400ml", "preco": 9.9, "desc": "Suco natural de maracujá, sem açúcar.", "estoque": 30},
        {"id": 507, "nome": "Refrigerante Lata 350ml", "preco": 6.5, "desc": "Lata gelada 350ml.", "estoque": 60},
        {"id": 508, "nome": "Água Mineral 500ml", "preco": 4.0, "desc": "Garrafa 500ml.", "estoque": 60},
    ],
}
 
qtd_variaveis = {}
cards_widgets = []
canvases = []
 
estoque_atual = {}
relatorio_vendas = {}
clientes_cadastrados = {}
 
spinboxes_por_item = {}
labels_estoque_por_item = {}
 
# ==================== PERSISTÊNCIA (ESTOQUE / RELATÓRIO / CLIENTES) ====================
def caminho_dados(nome_arquivo):
    pasta = os.path.join(os.getcwd(), "dados")
    os.makedirs(pasta, exist_ok=True)
    return os.path.join(pasta, nome_arquivo)
 
def carregar_estoque():
    caminho = caminho_dados("estoque.json")
    salvos = {}
    if os.path.exists(caminho):
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                salvos = json.load(f)
        except Exception:
            salvos = {}
    for itens in CARDAPIO.values():
        for item in itens:
            chave = str(item["id"])
            estoque_atual[item["id"]] = salvos.get(chave, item["estoque"])
    salvar_estoque()
 
def salvar_estoque():
    caminho = caminho_dados("estoque.json")
    dados = {str(k): v for k, v in estoque_atual.items()}
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
 
def carregar_relatorio():
    caminho = caminho_dados("relatorio.json")
    padrao = {
        "pedidos_realizados": 0,
        "produtos_vendidos": 0,
        "faturamento": 0.0,
        "vendas_por_item": {},
    }
    if os.path.exists(caminho):
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                padrao.update(json.load(f))
        except Exception:
            pass
    relatorio_vendas.update(padrao)
 
def salvar_relatorio():
    caminho = caminho_dados("relatorio.json")
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(relatorio_vendas, f, indent=4, ensure_ascii=False)
 
def carregar_clientes():
    caminho = caminho_dados("clientes.json")
    if os.path.exists(caminho):
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                clientes_cadastrados.update(json.load(f))
        except Exception:
            pass
 
def salvar_clientes():
    caminho = caminho_dados("clientes.json")
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(clientes_cadastrados, f, indent=4, ensure_ascii=False)
 
carregar_estoque()
carregar_relatorio()
carregar_clientes()
 
# ==================== CARRINHO ====================
def calcular_total():
    total = 0.0
    for categoria, itens in CARDAPIO.items():
        for item in itens:
            qtd = qtd_variaveis[item["id"]].get()
            total += qtd * item["preco"]
    lbl_total_valor.config(text=f"R$ {total:.2f}")
    return total
 
def zerar_quantidades():
    for var in qtd_variaveis.values():
        var.set(0)
    calcular_total()
 
def atualizar_widget_estoque(item_id):
    disponivel = estoque_atual[item_id]
    spn = spinboxes_por_item.get(item_id)
    lbl = labels_estoque_por_item.get(item_id)
    if spn is not None:
        spn.config(to=max(disponivel, 0))
        if qtd_variaveis[item_id].get() > disponivel:
            qtd_variaveis[item_id].set(0)
        spn.config(state="disabled" if disponivel <= 0 else "readonly")
    if lbl is not None:
        if disponivel <= 0:
            lbl.config(text="Esgotado", fg=cores["vermelho"])
        else:
            lbl.config(text=f"Estoque: {disponivel} unid.", fg=cores["subtexto"])
 
# ==================== RECIBO ====================
def gerar_texto_recibo(dados_pedido):
    largura = 34
    linhas = []
    linhas.append("=" * largura)
    linhas.append("PADARIA ARTES".center(largura))
    linhas.append("=" * largura)
 
    data_fmt = datetime.strptime(
        dados_pedido["data_pedido"], "%Y-%m-%d %H:%M:%S"
    ).strftime("%d/%m/%Y %H:%M")
    linhas.append(f"Data: {data_fmt}")
    if dados_pedido.get("cliente_nome"):
        linhas.append(f"Cliente: {dados_pedido['cliente_nome']}")
    linhas.append("-" * largura)
 
    for item in dados_pedido["itens"]:
        desc = f"{item['quantidade']}x {item['item']}"
        preco = f"R$ {item['subtotal']:.2f}"
        if len(desc) > largura - len(preco):
            desc = desc[: largura - len(preco) - 1]
        linhas.append(f"{desc:<{largura - len(preco)}}{preco}")
 
    linhas.append("-" * largura)
    total_txt = f"R$ {dados_pedido['total_pedido']:.2f}"
    linhas.append(f"{'TOTAL':<{largura - len(total_txt)}}{total_txt}")
    linhas.append(f"Pagamento: {dados_pedido['forma_pagamento']}")
 
    if dados_pedido.get("valor_recebido") is not None:
        linhas.append(f"Valor Recebido: R$ {dados_pedido['valor_recebido']:.2f}")
        linhas.append(f"Troco: R$ {dados_pedido['troco']:.2f}")
 
    linhas.append("=" * largura)
    linhas.append("Obrigado pela preferência!".center(largura))
    linhas.append("=" * largura)
    return "\n".join(linhas)
 
def mostrar_recibo(texto_recibo):
    dialogo = tk.Toplevel(janela)
    dialogo.title("🧾 Recibo")
    dialogo.geometry("380x500")
    dialogo.configure(bg=cores["painel"])
 
    txt = tk.Text(
        dialogo,
        font=("Consolas", 10),
        bg=cores["painel"],
        fg=cores["texto"],
        relief="flat",
        wrap="none",
    )
    txt.insert("1.0", texto_recibo)
    txt.config(state="disabled")
    txt.pack(fill="both", expand=True, padx=10, pady=10)
 
    tk.Button(
        dialogo,
        text="Fechar",
        command=dialogo.destroy,
        bg=cores["primaria"],
        fg="white",
        relief="flat",
        font=("Arial", 10, "bold"),
    ).pack(pady=(0, 10))
 
# ==================== RELATÓRIO DE VENDAS ====================
def mostrar_relatorio():
    dialogo = tk.Toplevel(janela)
    dialogo.title("📊 Relatório de Vendas")
    dialogo.geometry("360x340")
    dialogo.configure(bg=cores["painel"])
    dialogo.resizable(False, False)
 
    vendas_por_item = relatorio_vendas.get("vendas_por_item", {})
    if vendas_por_item:
        mais_vendido = max(vendas_por_item, key=vendas_por_item.get)
        qtd_mais_vendido = vendas_por_item[mais_vendido]
    else:
        mais_vendido = "-"
        qtd_mais_vendido = 0
 
    texto = (
        "📊 RELATÓRIO\n"
        f"{'=' * 28}\n\n"
        f"Pedidos realizados: {relatorio_vendas['pedidos_realizados']}\n"
        f"Produtos vendidos: {relatorio_vendas['produtos_vendidos']}\n"
        f"Faturamento: R$ {relatorio_vendas['faturamento']:.2f}\n\n"
        f"Mais vendido:\n{mais_vendido} ({qtd_mais_vendido} unid.)"
    )
    tk.Label(
        dialogo,
        text=texto,
        justify="left",
        anchor="w",
        bg=cores["painel"],
        fg=cores["texto"],
        font=("Consolas", 11),
        padx=15,
        pady=15,
    ).pack(fill="both", expand=True)
 
    tk.Button(
        dialogo,
        text="Fechar",
        command=dialogo.destroy,
        bg=cores["primaria"],
        fg="white",
        relief="flat",
        font=("Arial", 10, "bold"),
    ).pack(pady=10)
 
# ==================== CLIENTES ====================
def mostrar_clientes():
    dialogo = tk.Toplevel(janela)
    dialogo.title("👥 Clientes Cadastrados")
    dialogo.geometry("360x420")
    dialogo.configure(bg=cores["painel"])
 
    if not clientes_cadastrados:
        tk.Label(
            dialogo,
            text="Nenhum cliente cadastrado ainda.",
            bg=cores["painel"],
            fg=cores["texto"],
            font=("Arial", 11),
            padx=15,
            pady=15,
        ).pack()
    else:
        frame_lista = tk.Frame(dialogo, bg=cores["painel"])
        frame_lista.pack(fill="both", expand=True, padx=10, pady=10)
        for nome, dados in clientes_cadastrados.items():
            texto = (
                f"{nome}\n"
                f"Telefone: {dados.get('telefone') or '-'}\n"
                f"Pedidos realizados: {dados['pedidos']}\n"
                f"Total gasto: R$ {dados['total_gasto']:.2f}"
            )
            tk.Label(
                frame_lista,
                text=texto,
                justify="left",
                anchor="w",
                bg=cores["fundo"],
                fg=cores["texto"],
                font=("Arial", 9),
                padx=8,
                pady=6,
                relief="solid",
                bd=1,
            ).pack(fill="x", pady=4)
 
    tk.Button(
        dialogo,
        text="Fechar",
        command=dialogo.destroy,
        bg=cores["primaria"],
        fg="white",
        relief="flat",
        font=("Arial", 10, "bold"),
    ).pack(pady=10)
 
# ==================== PAGAMENTO ====================
def abrir_dialogo_pagamento(subtotal, itens_pedido):
    resultado = {"cancelado": True}
 
    dialogo = tk.Toplevel(janela)
    dialogo.title("Finalizar Pagamento")
    dialogo.geometry("420x560")
    dialogo.configure(bg=cores["fundo"])
    dialogo.resizable(False, False)
    dialogo.grab_set()
 
    frame_resumo = tk.Frame(dialogo, bg=cores["painel"], bd=1, relief="solid")
    frame_resumo.pack(fill="x", padx=10, pady=10)
    resumo_texto = "\n".join(
        f"{i['quantidade']}x {i['item']} - R$ {i['subtotal']:.2f}" for i in itens_pedido
    )
    tk.Label(
        frame_resumo,
        text=resumo_texto,
        justify="left",
        anchor="w",
        bg=cores["painel"],
        fg=cores["texto"],
        font=("Consolas", 9),
    ).pack(padx=8, pady=8, anchor="w")
 
    frame_cliente = tk.Frame(dialogo, bg=cores["fundo"])
    frame_cliente.pack(fill="x", padx=10, pady=(0, 8))
    tk.Label(
        frame_cliente, text="👤 Cliente (opcional):", bg=cores["fundo"], fg=cores["texto"]
    ).grid(row=0, column=0, sticky="w")
    entry_nome = tk.Entry(frame_cliente, width=25)
    entry_nome.grid(row=0, column=1, padx=5)
    tk.Label(
        frame_cliente, text="📞 Telefone:", bg=cores["fundo"], fg=cores["texto"]
    ).grid(row=1, column=0, sticky="w", pady=(4, 0))
    entry_telefone = tk.Entry(frame_cliente, width=25)
    entry_telefone.grid(row=1, column=1, padx=5, pady=(4, 0))
 
    frame_totais = tk.Frame(dialogo, bg=cores["fundo"])
    frame_totais.pack(fill="x", padx=10, pady=(0, 8))
    lbl_subtotal = tk.Label(
        frame_totais,
        text=f"Subtotal: R$ {subtotal:.2f}",
        bg=cores["fundo"],
        fg=cores["texto"],
        font=("Arial", 10),
    )
    lbl_subtotal.pack(anchor="e")
    lbl_total_final = tk.Label(
        frame_totais,
        text=f"Total: R$ {subtotal:.2f}",
        bg=cores["fundo"],
        fg=cores["primaria"],
        font=("Arial", 13, "bold"),
    )
    lbl_total_final.pack(anchor="e")
 
    estado = {"total_final": subtotal}
 
    def atualizar_troco(*_args):
        if metodo_var.get() != "Dinheiro":
            return
        try:
            valor_recebido = float(entry_valor_recebido.get().replace(",", "."))
        except ValueError:
            lbl_troco.config(text="Troco: R$ 0.00")
            return
        troco = valor_recebido - estado["total_final"]
        lbl_troco.config(text=f"Troco: R$ {max(troco, 0):.2f}")
 
    frame_pagamento = tk.Frame(dialogo, bg=cores["fundo"])
    frame_pagamento.pack(fill="x", padx=10, pady=(0, 4))
    tk.Label(
        frame_pagamento,
        text="Forma de Pagamento:",
        bg=cores["fundo"],
        fg=cores["texto"],
        font=("Arial", 10, "bold"),
    ).pack(anchor="w")
 
    metodo_var = tk.StringVar(value="Dinheiro")
    opcoes_pagamento = [
        ("💵 Dinheiro", "Dinheiro"),
        ("💳 Débito", "Débito"),
        ("💳 Crédito", "Crédito"),
        ("📱 Pix", "Pix"),
    ]
    frame_opcoes = tk.Frame(frame_pagamento, bg=cores["fundo"])
    frame_opcoes.pack(fill="x", pady=4)
 
    frame_dinheiro = tk.Frame(dialogo, bg=cores["fundo"])
    lbl_valor_recebido = tk.Label(
        frame_dinheiro, text="Valor Recebido: R$", bg=cores["fundo"], fg=cores["texto"]
    )
    lbl_valor_recebido.grid(row=0, column=0, sticky="w")
    entry_valor_recebido = tk.Entry(frame_dinheiro, width=12)
    entry_valor_recebido.grid(row=0, column=1, padx=5)
    lbl_troco = tk.Label(
        frame_dinheiro,
        text="Troco: R$ 0.00",
        bg=cores["fundo"],
        fg=cores["verde"],
        font=("Arial", 11, "bold"),
    )
    lbl_troco.grid(row=1, column=0, columnspan=2, sticky="w", pady=(4, 0))
 
    entry_valor_recebido.bind("<KeyRelease>", atualizar_troco)
 
    def alternar_campo_dinheiro():
        if metodo_var.get() == "Dinheiro":
            frame_dinheiro.pack(fill="x", padx=10, pady=(0, 8))
        else:
            frame_dinheiro.pack_forget()
        atualizar_troco()
 
    for i, (rotulo, valor) in enumerate(opcoes_pagamento):
        tk.Radiobutton(
            frame_opcoes,
            text=rotulo,
            variable=metodo_var,
            value=valor,
            bg=cores["fundo"],
            fg=cores["texto"],
            selectcolor=cores["painel"],
            activebackground=cores["fundo"],
            command=alternar_campo_dinheiro,
        ).grid(row=i // 2, column=i % 2, sticky="w", padx=5, pady=2)
 
    alternar_campo_dinheiro()
 
    frame_botoes = tk.Frame(dialogo, bg=cores["fundo"])
    frame_botoes.pack(fill="x", padx=10, pady=15)
 
    def confirmar():
        metodo = metodo_var.get()
        valor_recebido = None
        troco = None
        if metodo == "Dinheiro":
            try:
                valor_recebido = float(entry_valor_recebido.get().replace(",", "."))
            except ValueError:
                messagebox.showwarning("Valor Inválido", "Informe um valor recebido válido.")
                return
            if valor_recebido < estado["total_final"]:
                messagebox.showwarning(
                    "Valor Insuficiente", "O valor recebido é menor que o total do pedido."
                )
                return
            troco = valor_recebido - estado["total_final"]
 
        resultado.update(
            {
                "cancelado": False,
                "metodo": metodo,
                "total_final": estado["total_final"],
                "valor_recebido": valor_recebido,
                "troco": troco,
                "cliente_nome": entry_nome.get().strip(),
                "cliente_telefone": entry_telefone.get().strip(),
            }
        )
        dialogo.destroy()
 
    tk.Button(
        frame_botoes,
        text="✅ Confirmar Pagamento",
        bg=cores["verde"],
        fg="white",
        font=("Arial", 10, "bold"),
        relief="flat",
        cursor="hand2",
        command=confirmar,
    ).pack(side="right", padx=5)
    tk.Button(
        frame_botoes,
        text="✖ Cancelar",
        bg=cores["vermelho"],
        fg="white",
        font=("Arial", 10, "bold"),
        relief="flat",
        cursor="hand2",
        command=dialogo.destroy,
    ).pack(side="right", padx=5)
 
    janela.wait_window(dialogo)
    return resultado
 
# ==================== FINALIZAR PEDIDO ====================
def finalizar_pedido_json():
    itens_pedido = []
    subtotal = 0.0
 
    for categoria, itens in CARDAPIO.items():
        for item in itens:
            qtd = qtd_variaveis[item["id"]].get()
            if qtd > 0:
                item_subtotal = qtd * item["preco"]
                subtotal += item_subtotal
                itens_pedido.append(
                    {
                        "id": item["id"],
                        "item": item["nome"],
                        "categoria": categoria,
                        "quantidade": qtd,
                        "preco_unitario": item["preco"],
                        "subtotal": item_subtotal,
                    }
                )
 
    if not itens_pedido:
        messagebox.showwarning("Carrinho Vazio", "Selecione pelo menos um item para finalizar!")
        return
 
    for item_pedido in itens_pedido:
        disponivel = estoque_atual.get(item_pedido["id"], 0)
        if item_pedido["quantidade"] > disponivel:
            messagebox.showerror(
                "Estoque Insuficiente",
                f"'{item_pedido['item']}' possui apenas {disponivel} unidade(s) em estoque.\n"
                "Reduza a quantidade e tente novamente.",
            )
            return
 
    pagamento = abrir_dialogo_pagamento(subtotal, itens_pedido)
    if pagamento["cancelado"]:
        return
 
    for item_pedido in itens_pedido:
        item_id = item_pedido["id"]
        estoque_atual[item_id] -= item_pedido["quantidade"]
        atualizar_widget_estoque(item_id)
    salvar_estoque()
 
    dados_pedido = {
        "data_pedido": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cliente_nome": pagamento["cliente_nome"] or None,
        "cliente_telefone": pagamento["cliente_telefone"] or None,
        "subtotal": subtotal,
        "total_pedido": pagamento["total_final"],
        "forma_pagamento": pagamento["metodo"],
        "valor_recebido": pagamento["valor_recebido"],
        "troco": pagamento["troco"],
        "itens": itens_pedido,
    }
 
    relatorio_vendas["pedidos_realizados"] += 1
    relatorio_vendas["produtos_vendidos"] += sum(i["quantidade"] for i in itens_pedido)
    relatorio_vendas["faturamento"] += pagamento["total_final"]
    for item_pedido in itens_pedido:
        nome = item_pedido["item"]
        relatorio_vendas["vendas_por_item"][nome] = (
            relatorio_vendas["vendas_por_item"].get(nome, 0) + item_pedido["quantidade"]
        )
    salvar_relatorio()
 
    nome_cliente = pagamento["cliente_nome"]
    if nome_cliente:
        cliente = clientes_cadastrados.setdefault(
            nome_cliente, {"telefone": "", "pedidos": 0, "total_gasto": 0.0}
        )
        if pagamento["cliente_telefone"]:
            cliente["telefone"] = pagamento["cliente_telefone"]
        cliente["pedidos"] += 1
        cliente["total_gasto"] += pagamento["total_final"]
        salvar_clientes()
 
    nome_arquivo = f"pedido_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    nome_arquivo_recibo = nome_arquivo.replace(".json", "_recibo.txt")
 
    pasta_ticket = os.path.join(os.getcwd(), "ticket")
    os.makedirs(pasta_ticket, exist_ok=True)
 
    caminho_local_repo = os.path.join(pasta_ticket, nome_arquivo)
    caminho_recibo = os.path.join(pasta_ticket, nome_arquivo_recibo)
 
    try:
        with open(caminho_local_repo, "w", encoding="utf-8") as f:
            json.dump(dados_pedido, f, indent=4, ensure_ascii=False)
    except Exception as e_repo:
        messagebox.showerror("Erro", f"Falha ao salvar na pasta ticket do projeto: {e_repo}")
        return
 
    texto_recibo = gerar_texto_recibo(dados_pedido)
    try:
        with open(caminho_recibo, "w", encoding="utf-8") as f_recibo:
            f_recibo.write(texto_recibo)
    except Exception as e_recibo:
        print(f"Não foi possível salvar o recibo em .txt: {e_recibo}")
 
    caminho_copia_extra = filedialog.asksaveasfilename(
        initialdir=pasta_ticket,
        initialfile=nome_arquivo,
        defaultextension=".json",
        filetypes=[("Arquivos JSON", "*.json"), ("Todos os Arquivos", "*.*")],
        title="Salvar uma cópia extra do Pedido JSON (Opcional)",
    )
    if caminho_copia_extra:
        try:
            with open(caminho_copia_extra, "w", encoding="utf-8") as f_extra:
                json.dump(dados_pedido, f_extra, indent=4, ensure_ascii=False)
        except Exception as e_copia:
            print(f"Não foi possível salvar a cópia extra: {e_copia}")
 
    mostrar_recibo(texto_recibo)
    zerar_quantidades()
 
# ==================== TEMA / SCROLL ====================
def alternar_tema():
    global modo_escuro, cores
    modo_escuro = not modo_escuro
    cores = PALETA_ESCURA if modo_escuro else PALETA_CLARA
 
    janela.configure(bg=cores["fundo"])
    bar_topo.configure(bg=cores["fundo"])
    bar_ferramentas.configure(bg=cores["fundo"])
    lbl_titulo_app.configure(bg=cores["fundo"], fg=cores["texto"])
    frame_rodape.configure(bg=cores["painel"])
    lbl_total_texto.configure(bg=cores["painel"], fg=cores["texto"])
    lbl_total_valor.configure(bg=cores["painel"], fg=cores["primaria"])
 
    btn_tema.config(text="☀️ Modo Claro" if modo_escuro else "🌙 Modo Escuro")
 
    style.configure("TNotebook", background=cores["fundo"], borderwidth=0)
    style.configure(
        "TNotebook.Tab",
        background=cores["painel"],
        foreground=cores["texto"],
        padding=[10, 5],
    )
    style.map(
        "TNotebook.Tab",
        background=[("selected", cores["primaria"])],
        foreground=[("selected", "#ffffff")],
    )
 
    for cv in canvases:
        cv.configure(bg=cores["fundo"])
        cv.master.configure(bg=cores["fundo"])
 
    for card, frame in cards_widgets:
        frame.configure(bg=cores["fundo"])
        card.configure(bg=cores["painel"], highlightbackground=cores["borda"])
        for sub in card.winfo_children():
            if isinstance(sub, tk.Label):
                if sub.cget("fg") in [PALETA_CLARA["vermelho"], PALETA_ESCURA["vermelho"]]:
                    sub.configure(bg=cores["painel"], fg=cores["vermelho"])
                elif sub.cget("fg") in [PALETA_CLARA["subtexto"], PALETA_ESCURA["subtexto"]]:
                    sub.configure(bg=cores["painel"], fg=cores["subtexto"])
                elif sub.cget("fg") in [PALETA_CLARA["verde"], PALETA_ESCURA["verde"]]:
                    sub.configure(bg=cores["painel"], fg=cores["verde"])
                else:
                    sub.configure(bg=cores["painel"], fg=cores["texto"])
            elif isinstance(sub, tk.Spinbox):
                sub.configure(
                    bg=cores["fundo"],
                    fg=cores["texto"],
                    readonlybackground=cores["fundo"],
                    buttonbackground=cores["painel"],
                )
 
def _ao_rolar_mouse(event, canvas):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
 
# ==================== INTERFACE GRÁFICA ====================
janela = tk.Tk()
janela.title("Padaria Artes - Cardápio Digital")
janela.geometry("740x700")
janela.configure(bg=cores["fundo"])
 
style = ttk.Style()
style.theme_use("default")
style.configure("TNotebook", background=cores["fundo"], borderwidth=0)
style.configure(
    "TNotebook.Tab",
    background=cores["painel"],
    foreground=cores["texto"],
    padding=[10, 5],
)
style.map(
    "TNotebook.Tab",
    background=[("selected", cores["primaria"])],
    foreground=[("selected", "#ffffff")],
)
 
bar_topo = tk.Frame(janela, bg=cores["fundo"])
bar_topo.pack(fill="x", padx=15, pady=(10, 5))
 
lbl_titulo_app = tk.Label(
    bar_topo,
    text="🥖 Padaria Artes",
    font=("Arial", 16, "bold"),
    bg=cores["fundo"],
    fg=cores["texto"],
)
lbl_titulo_app.pack(side="left")
 
btn_tema = tk.Button(
    bar_topo,
    text="🌙 Modo Escuro",
    bg=cores["amarelo"],
    fg="black",
    font=("Arial", 9, "bold"),
    relief="flat",
    cursor="hand2",
    command=alternar_tema,
)
btn_tema.pack(side="right")
 
bar_ferramentas = tk.Frame(janela, bg=cores["fundo"])
bar_ferramentas.pack(fill="x", padx=15, pady=(0, 8))
 
btn_clientes = tk.Button(
    bar_ferramentas,
    text="👥 Clientes",
    bg=cores["primaria"],
    fg="white",
    font=("Arial", 9, "bold"),
    relief="flat",
    cursor="hand2",
    command=lambda: mostrar_clientes(),
)
btn_clientes.pack(side="right", padx=(5, 0))
 
btn_relatorio = tk.Button(
    bar_ferramentas,
    text="📊 Relatório",
    bg=cores["primaria"],
    fg="white",
    font=("Arial", 9, "bold"),
    relief="flat",
    cursor="hand2",
    command=lambda: mostrar_relatorio(),
)
btn_relatorio.pack(side="right")
 
notebook = ttk.Notebook(janela)
notebook.pack(fill="both", expand=True, padx=15, pady=(0, 10))
 
for categoria, itens in CARDAPIO.items():
    frame_aba = tk.Frame(notebook, bg=cores["fundo"])
    notebook.add(frame_aba, text=categoria)
 
    canvas = tk.Canvas(frame_aba, bg=cores["fundo"], highlightthickness=0)
    scrollbar = ttk.Scrollbar(frame_aba, orient="vertical", command=canvas.yview)
    frame_itens = tk.Frame(canvas, bg=cores["fundo"])
 
    def _ajustar_largura(e, c=canvas, f=frame_itens):
        c.itemconfig(c.find_withtag("win")[0], width=e.width)
 
    frame_itens.bind("<Configure>", lambda e, c=canvas: c.configure(scrollregion=c.bbox("all")))
    win_id = canvas.create_window((0, 0), window=frame_itens, anchor="nw", tags="win")
    canvas.bind("<Configure>", _ajustar_largura)
 
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
 
    canvases.append(canvas)
    frame_itens.bind_all("<MouseWheel>", lambda e, c=canvas: _ao_rolar_mouse(e, c))
 
    for item in itens:
        var_qtd = tk.IntVar(value=0)
        qtd_variaveis[item["id"]] = var_qtd
 
        card = tk.Frame(
            frame_itens,
            bg=cores["painel"],
            bd=1,
            relief="solid",
            highlightbackground=cores["borda"],
        )
        card.pack(fill="x", pady=5, ipady=4, ipadx=6, expand=True)
        card.columnconfigure(0, weight=1)
 
        cards_widgets.append((card, frame_itens))
 
        lbl_nome = tk.Label(
            card,
            text=item["nome"],
            font=("Arial", 11, "bold"),
            fg=cores["texto"],
            bg=cores["painel"],
        )
        lbl_nome.grid(row=0, column=0, sticky="w", padx=8, pady=(4, 0))
 
        lbl_desc = tk.Label(
            card,
            text=item["desc"],
            font=("Arial", 8),
            fg=cores["subtexto"],
            bg=cores["painel"],
            wraplength=380,
            justify="left",
        )
        lbl_desc.grid(row=1, column=0, sticky="w", padx=8, pady=(0, 2))
 
        disponivel_inicial = estoque_atual[item["id"]]
        lbl_estoque = tk.Label(
            card,
            text=(
                "Esgotado"
                if disponivel_inicial <= 0
                else f"Estoque: {disponivel_inicial} unid."
            ),
            font=("Arial", 8, "bold"),
            fg=cores["vermelho"] if disponivel_inicial <= 0 else cores["subtexto"],
            bg=cores["painel"],
        )
        lbl_estoque.grid(row=2, column=0, sticky="w", padx=8, pady=(0, 4))
        labels_estoque_por_item[item["id"]] = lbl_estoque
 
        lbl_preco = tk.Label(
            card,
            text=f"R$ {item['preco']:.2f}",
            font=("Arial", 11, "bold"),
            fg=cores["verde"],
            bg=cores["painel"],
        )
        lbl_preco.grid(row=0, column=1, rowspan=3, padx=10)
 
        spn_qtd = tk.Spinbox(
            card,
            from_=0,
            to=max(disponivel_inicial, 0),
            width=3,
            textvariable=var_qtd,
            font=("Arial", 10),
            command=calcular_total,
            state="readonly" if disponivel_inicial > 0 else "disabled",
            readonlybackground=cores["fundo"],
        )
        spn_qtd.grid(row=0, column=2, rowspan=3, padx=8)
        spinboxes_por_item[item["id"]] = spn_qtd
 
frame_rodape = tk.Frame(janela, bg=cores["painel"], bd=1, relief="raised")
frame_rodape.pack(fill="x", ipady=8, ipadx=10)
 
lbl_total_texto = tk.Label(
    frame_rodape,
    text="Total do Pedido:",
    font=("Arial", 11, "bold"),
    bg=cores["painel"],
    fg=cores["texto"],
)
lbl_total_texto.pack(side="left", padx=(15, 5))
 
lbl_total_valor = tk.Label(
    frame_rodape,
    text="R$ 0.00",
    font=("Arial", 14, "bold"),
    bg=cores["painel"],
    fg=cores["primaria"],
)
lbl_total_valor.pack(side="left")
 
btn_finalizar = tk.Button(
    frame_rodape,
    text="🛒 Exportar Pedido (JSON)",
    bg=cores["verde"],
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2",
    command=finalizar_pedido_json,
)
btn_finalizar.pack(side="right", padx=15)
 
btn_limpar = tk.Button(
    frame_rodape,
    text="🗑️ Limpar",
    bg=cores["vermelho"],
    fg="white",
    font=("Arial", 9, "bold"),
    relief="flat",
    cursor="hand2",
    command=zerar_quantidades,
)
btn_limpar.pack(side="right", padx=5)
 
janela.mainloop()
 