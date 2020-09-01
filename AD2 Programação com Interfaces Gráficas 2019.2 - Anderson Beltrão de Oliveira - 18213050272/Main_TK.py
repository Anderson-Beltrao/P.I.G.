from tkinter import *
from SocialGraph import SocialGraph

class IG(Frame):
    def __init__(self,master=None):
        super().__init__()
        self.frame0 = Frame(master)
        self.frame0.pack()
        self.lab0 = Label(self.frame0, text="Insira o nome do arquivo com sua extensão")
        self.lab0.pack()
        self.e0 = Entry(self.frame0)
        self.e0.pack()
        self.b0 = Button(self.frame0, text="Inserir", width = 11, command = self.destruicaoEchamada)
        self.b0.pack()


    def inico(self, master=None):
        self.frame1 = Frame(master)
        self.frame1.pack()
        self.label = Label(self.frame1, text = "Insira o nome do usuário para ver seus respectivos amigos.")
        self.label.pack(anchor = W)
        self.label1 = Label(self.frame1, text= self.listaK)
        self.label1.pack(anchor = W)
        self.label2 = Label(self.frame1, text = "Sempre apague o grafo anterior antes de ver um novo grafo!")
        self.label2.pack(anchor = W)
        self.entrada = Entry(self.frame1)
        self.entrada.pack(anchor = W)
        self.envia = Button(self.frame1, text="Mostrar grafo", width = 11, command = self.action)
        self.envia.pack(anchor = W)
        self.apaga = Button(self.frame1, text = "Apagar grafo", width = 11, command = self.destruir)
        self.apaga.pack(anchor = W)
        self.label3 = Label(self.frame1, text = "Para modificar/criar um grafo insira abaixo os novos comandos - Ex: add Usuário Amigo 1")
        self.label3.pack(anchor=W)
        self.label4 = Label(self.frame1, text = "Depois clique novamente no botão acima para mostrar o novo grafo.")
        self.label4.pack(anchor = W)
        self.label5 = Label(self.frame1, text = "Caso o úsuario já tenha o amigo não adicione-o novamente!")
        self.label5.pack(anchor = W)
        self.novoEntrada = Entry(self.frame1)
        self.novoEntrada.pack(anchor = W)
        self.enviaComando = Button(self.frame1, text = "Aplicar", width = 11, command = self.novoComando)
        self.enviaComando.pack(anchor = W)
        self.frame2 = Frame(master)
        self.frame2.pack()


    def novoComando(self):
        classe2.inic(self.novoEntrada.get())
        AUXK2 = ""
        for i in classe2.classe1.grafo.keys():
            AUXK2 = AUXK2 + str(i) + " "
        self.listaK = "Escolha entre um dos usuários disponíveis até o momento: " + AUXK2
        self.label1.config(text = self.listaK)

    def destruicaoEchamada(self):
        Main(self.e0.get())

        AUXK = ""
        for i in classe2.classe1.grafo.keys():
            AUXK = AUXK + str(i) + " "
        self.listaK = "Escolha entre um dos usuários disponíveis até o momento: " + AUXK

        IG.inico(self)
        self.frame0.destroy()

    def destruir(self):
        self.frame2.destroy()
        self.frame2 = Frame(master=None)
        self.frame2.pack()


    def action(self):
        self.i = self.entrada.get()
        j = classe2.classe1.grafo[self.i]
        c = Canvas(self.frame2, width=300, height=300)
        c.pack()
        t = c.create_text(15, 195, text=self.i)
        c.create_oval(1, 200, 20, 290, outline="green", fill="black", width=5)  # criação do grafo inicial
        x1, y1, x2, y2 = 200, 1, 230, 20  # cordenadas variáveis
        vez = 0
        if j != "":
            if type(j) is str:
                peso = j.split(" ")
                circulo = c.create_oval(x1, y1, x2, y2, outline="black", fill="yellow")
                aresta = c.create_line(1, 215, x1, y1)
                mediaVetorx = (1 + x1) / 2
                mediaVetory = (215 + y1) / 2
                pesoVetor = c.create_text(mediaVetorx, mediaVetory + 3, text=peso[1])
                textoCirculo = c.create_text((x1 + x2) / 2, y2 + 5, text=peso[0])
            else:
                for i in j:
                    if vez == 0:
                        peso = i.split(" ")
                        circulo = c.create_oval(x1, y1, x2, y2, outline="black", fill="yellow")
                        aresta = c.create_line(1, 215, x1, y1)
                        mediaVetorx = (1 + x1) / 2
                        mediaVetory = (215 + y1) / 2
                        pesoVetor = c.create_text(mediaVetorx, mediaVetory + 3, text=peso[1])
                        textoCirculo = c.create_text((x1 + x2) / 2, y2 + 5, text=peso[0])
                        vez += 1
                    else:
                        peso = i.split(" ")
                        y1 += 30
                        y2 += 30
                        circulo = c.create_oval(x1, y1, x2, y2, outline="black", fill="yellow")
                        aresta = c.create_line(1, 215, x1, y1)
                        mediaVetorx = (1 + x1) / 2
                        mediaVetory = (215 + y1) / 2
                        pesoVetor = c.create_text(mediaVetorx, mediaVetory + 3, text=peso[1])
                        textoCirculo = c.create_text((x1 + x2) / 2, y2 + 5, text=peso[0])


#@ Programa Principal

def Main(infile):
    #@ def Main: A função lê o nome do arquivo texto de entrada e o abre, enviando os comandos lidos para a classe importada(SocialGraph)
    entrada = infile
    if entrada == "":
        print("Arquivo não inserido")
    else:
        arq = open(entrada, "r")
        for linha in arq:
            classe2.inic(linha)

classe2 = SocialGraph()
root = Tk()
IG(root)
root.geometry("520x520+100+100")
root.mainloop()
