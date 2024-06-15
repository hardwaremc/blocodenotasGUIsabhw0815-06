import tkinter as tk
from tkinter import filedialog, messagebox

# Definindo a classe BlocoDeNotas
class BlocoDeNotas:
    # Método de inicialização da classe
    def __init__(self, root):
        self.root = root  # Referência à janela principal
        self.root.title("Bloco de Notas")  # Título da janela
        self.root.geometry("800x600")  # Tamanho da janela

        # Área de texto onde o usuário digitará o conteúdo
        self.text_area = tk.Text(self.root, wrap='word', font=('Arial', 12))
        self.text_area.pack(expand=True, fill='both')  # Preenche toda a janela e expande conforme a janela é redimensionada

        # Barra de menu da janela
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)  # Configura a janela para usar essa barra de menu

        # Menu de arquivo
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Arquivo", menu=self.file_menu)  # Adiciona o menu "Arquivo" na barra de menu
        self.file_menu.add_command(label="Novo", command=self.novo_arquivo)  # Adiciona a opção "Novo" no menu de arquivo
        self.file_menu.add_command(label="Abrir", command=self.abrir_arquivo)  
        self.file_menu.add_command(label="Salvar", command=self.salvar_arquivo)  # Adiciona a opção "Salvar" no menu de arquivo  
        self.file_menu.add_separator()  
        self.file_menu.add_command(label="Sair", command=self.root.quit)  

    # Método para criar um novo arquivo
    def novo_arquivo(self):
        self.text_area.delete(1.0, tk.END)  
    def abrir_arquivo(self):
        arquivo_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Todos os arquivos", "*.*"), ("Arquivos de texto" , "*.txt")])
        if arquivo_path:
          try:
            with open(arquivo_path, "r") as file:
              self.text_area.delete(1.0, tk.END)
              self.text_area.insert(tk.END, file.read())
          except Exception as e:
            messagebox.showerror("Errou", e)

    def salvar_arquivo(self):
      arquivo_path = filedialog.asksaveasfilename(defaultextension = ".txt", filetypes=[("Todos os arquivos", "*.*"), ("Arquivos de texto", "*.txt")])
      
if __name__ == "__main__":
  root = tk.Tk()
  app = BlocoDeNotas(root)
  root.mainloop()