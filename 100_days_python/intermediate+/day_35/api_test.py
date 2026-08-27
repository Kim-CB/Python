# OMDb Database - Qual era aquele filme mesmo?
import io
import tkinter as tk
from tkinter import messagebox, ttk

import requests
from PIL import Image, ImageTk

API_KEY = ""


class FilmesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OMDb - Qual era aquele filme mesmo?")
        self.root.geometry("700x450")
        self.root.configure(padx=20, pady=20)

        self.api_key = API_KEY
        self.base_url = "http://www.omdbapi.com/"

        self.setup_ui()

    def setup_ui(self):
        # -- SEARCH SECTION --
        search_frame = ttk.Frame(self.root)
        search_frame.pack(fill=tk.X, pady=(0, 20))

        ttk.Label(search_frame, text="Nome do Filme:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky=tk.W, pady=2)
        self.entry_nome = ttk.Entry(search_frame, width=30)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=2)

        self.entry_nome.bind("<Return>", lambda event:self.buscar_filme_lista())

        ttk.Label(search_frame, text="Ano (opcional):", font=("Arial", 10)).grid(row=1, column=0, sticky=tk.W, pady=2)
        self.entry_ano = ttk.Entry(search_frame, width=10)
        self.entry_ano.grid(row=1, column=1, sticky=tk.W, padx=10, pady=2)

        self.btn_search = ttk.Button(search_frame, text="Buscar", command=self.buscar_filme_lista)
        self.btn_search.grid(row=0, column=2, rowspan=2,sticky=tk.NSEW)

        content_frame = ttk.Frame(self.root)
        content_frame.pack(fill=tk.BOTH, expand=True)

        self.label_poster = ttk.Label(content_frame, text="Sem Imagem", background="#e0e0e0", anchor=tk.CENTER)
        # Espaço para o poster
        self.label_poster.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 20))
        self.label_poster.config(width=25)

        #info no lado direito
        info_frame = ttk.Frame(content_frame)
        info_frame.pack(side= tk.LEFT, fill=tk.BOTH, expand=True)

        # -- RESULT SECTION ---
        self.label_title = ttk.Label(info_frame, text="", font=("Arial", 16, "bold"), wraplength=400)
        self.label_title.pack(anchor=tk.W, pady=(0, 5))

        self.label_info = ttk.Label(info_frame, text="", font= ("Arial", 16, "italic"), foreground="gray", wraplength=450)
        self.label_info.pack(anchor=tk.W, pady=(0, 15))

        self.text_plot = tk.Text(info_frame, height=10, width=10, font=("Arial",11),
                                 wrap=tk.WORD, bg="#f0f0f0", relief=tk.FLAT)
        self.text_plot.pack(fill=tk.BOTH, expand=True)

        self.text_plot.config(state=tk.DISABLED)


    def buscar_filme_lista(self):
        nome = self.entry_nome.get().strip()
        ano = self.entry_ano.get().strip()

        if not nome:
            messagebox.showwarning("Aviso", "Por favor, digite o nome do filme.")
            return

        self.label_title.config(text="Buscando...")
        self.root.update()

        resultados_totais = []

        try:
            for pagina in range(1, 4):
                parametros = {
                    "apikey": self.api_key,
                    "s": nome,
                    "page": pagina
                }

                if ano:
                    parametros["y"] = ano

                response = requests.get(self.base_url, params=parametros)
                response.raise_for_status()
                data = response.json()

                if data.get("Response") == "True":
                    resultados_totais.extend(data.get("Search", []))
                else:

                    if pagina == 1:
                        messagebox.showinfo("Resultado", data.get("Error", "Título não encontrado"))
                        self.limpar_resultados()
                        return
                    break

            resultados_totais.sort(key=lambda x: x.get("Year", "0"), reverse=True)

            if len(resultados_totais) == 1:
                    self.buscar_detalhes_filme(resultados_totais[0]["imdbID"])
            else:
                    self.abrir_popup_selecao(resultados_totais)

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Erro de Conexão", f"Não foi possível conectar à API: \n{e}")
            self.limpar_resultados()

    def abrir_popup_selecao(self, resultados):
        # pop-up
        popup = tk.Toplevel(self.root)
        popup.title("Escolha o filme")
        popup.geometry("350x250")
        popup.grab_set()

        ttk.Label(popup, text="Foram encontrados mais de um filme. Escolha um:", font=("Arial", 10, "bold")).pack(pady=10)

        # Listbox e Scrollbar
        frame_lista = ttk.Frame(popup)
        frame_lista.pack(fill=tk.BOTH, expand=True, padx=10)

        scrollbar = ttk.Scrollbar(popup)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        lista_box = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set, font=("Arial", 10))
        lista_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=lista_box.yview)

        imdb_ids = []
        for filme in resultados:
            texto = f"{filme.get('Title')} ({filme.get('Year')})"
            lista_box.insert(tk.END, texto)
            imdb_ids.append(filme.get("imdbID"))

        def confirmar_selecao():
            selecao = lista_box.curselection() # Pega a tupla dos indices
            if not selecao: 
                messagebox.showwarning("Aviso", "Selecione um filme da lista.", parent= popup)
                return
            index_selecionado = selecao[0]
            id_escolhido = imdb_ids[index_selecionado]
            popup.destroy() # Fecha
            self.buscar_detalhes_filme(id_escolhido) # Fase 2

        btn_confirmar = ttk.Button(popup, text="Confirmar", command=confirmar_selecao)
        btn_confirmar.pack(pady=10)

        lista_box.bind("<Double-1>", lambda e: confirmar_selecao())

    # Fase 2
    def buscar_detalhes_filme(self, imdb_id):

        parametros = {
            "apikey":self.api_key,
            "i":imdb_id,
            "plot": "full"
        }
        try:
            self.label_title.config(text="Baixando sinopse...")
            self.root.update()

            response = requests.get(self.base_url, params=parametros)
            response.raise_for_status()
            data = response.json()

            self.mostrar_resultados(data)
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Erro", f"Falha ao buscar detalhes: \n{e}")
            self.limpar_resultados()


    def mostrar_resultados(self, data):
        # OMDb retorna {"Response": "False"} if the movie isn't found
        if data.get("Response") == "False":
            error_msg = data.get("Error", "Filme não encontrado.")
            messagebox.showinfo("Resultado", error_msg)
            self.limpar_resultados()
            return

        title = data.get("Title", "N/A")
        year = data.get("Year", "N/A")
        director = data.get("Director", "N/A")
        genre = data.get("Genre", "N/A")
        plot = data.get("Plot", "Sinopse não disponível.")
        poster_url = data.get("Poster", "N/A")

        # UI 
        self.label_title.config(text=f"{title} ({year})")
        self.label_info.config(text=f"Diretor: {director} | Gênero: {genre}")

        # Update widget
        self.text_plot.config(state=tk.NORMAL) #Enable temp to insert text
        self.text_plot.delete("1.0", tk.END)
        self.text_plot.insert(tk.END, plot)
        self.text_plot.config(state=tk.DISABLED) # Lock again

        if poster_url and poster_url != "N/A":
            self.carregar_poster(poster_url)
        else:
            self.label_poster.config(image='', text="Sem Imagem")
            self.photo_reference = None

    def carregar_poster(self, url):
        try:
            self.label_poster.config(text="Baixando\nPoster...", image='')
            self.root.update()

            response = requests.get(url)
            response.raise_for_status()
            image_data = response.content

            image = Image.open(io.BytesIO(image_data))

            image = image.resize((200, 300), Image.Resampling.LANCZOS)

            self.photo_reference = ImageTk.PhotoImage(image)
            self.label_poster.config(image=self.photo_reference, text="")

        except Exception as e:  # noqa: BLE001
            print(f"Erro ao baixar imagem: {e}")
            self.label_poster.config(image='', text="Erro na \nImagem")


    def limpar_resultados(self):
        self.label_title.config(text="")
        self.label_info.config(text="")
        self.text_plot.config(state=tk.NORMAL)
        self.text_plot.delete("1.0", tk.END)
        self.text_plot.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    # Add tema meio q clean
    style = ttk.Style()
    if "clam" in style.theme_names():
        style.theme_use("clam")


    app = FilmesApp(root)
    root.mainloop()