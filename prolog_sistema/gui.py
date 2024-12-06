import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QTabWidget, QFormLayout)
from pyswip import Prolog

class BloodDonationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        # Inicializa Prolog e carrega a base de conhecimento
        self.prolog = Prolog()
        self.prolog.consult("base_sangue.pl")
        
    def initUI(self):
        self.setWindowTitle("Sistema Especialista de Doação de Sangue")
        
        # Tabs
        self.tabs = QTabWidget()
        
        # Tab 1: Verificar se X pode doar para Y
        self.tab1 = QWidget()
        self.tabs.addTab(self.tab1, "Verificar doação")
        
        # Tab 2: Descobrir doadores para um indivíduo
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab2, "Quem pode receber/doar")
        
        # Tab 3: Consultas sobre tipo sanguíneo e fator Rh
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab3, "Consultas sobre tipos")

        self.initTab1()
        self.initTab2()
        self.initTab3()

        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        self.setLayout(layout)
        
    def initTab1(self):
        layout = QFormLayout()
        
        self.doadorInput = QLineEdit()
        self.receptorInput = QLineEdit()
        
        btn = QPushButton("Verificar se pode doar")
        btn.clicked.connect(self.verificarDoacao)
        
        self.resultTab1 = QTextEdit()
        self.resultTab1.setReadOnly(True)
        
        layout.addRow(QLabel("Doador:"), self.doadorInput)
        layout.addRow(QLabel("Receptor:"), self.receptorInput)
        layout.addRow(btn)
        layout.addRow(self.resultTab1)
        
        self.tab1.setLayout(layout)
        
    def initTab2(self):
        layout = QFormLayout()
        
        self.pessoaTab2 = QLineEdit()
        btnDoadores = QPushButton("Quem pode doar para esta pessoa?")
        btnDoadores.clicked.connect(self.quemDoaPara)
        
        btnReceptores = QPushButton("Para quem esta pessoa pode doar?")
        btnReceptores.clicked.connect(self.paraQuemDoador)
        
        self.resultTab2 = QTextEdit()
        self.resultTab2.setReadOnly(True)
        
        layout.addRow(QLabel("Pessoa:"), self.pessoaTab2)
        layout.addRow(btnDoadores)
        layout.addRow(btnReceptores)
        layout.addRow(self.resultTab2)
        
        self.tab2.setLayout(layout)
        
    def initTab3(self):
        layout = QFormLayout()
        
        self.tipoSanguineoInput = QLineEdit()
        btnTipo = QPushButton("Quem possui este tipo sanguíneo?")
        btnTipo.clicked.connect(self.quemTemTipo)
        
        self.fatorRhInput = QLineEdit()
        btnRh = QPushButton("Quem possui este fator RH?")
        btnRh.clicked.connect(self.quemTemRh)
        
        self.resultTab3 = QTextEdit()
        self.resultTab3.setReadOnly(True)
        
        layout.addRow(QLabel("Tipo Sanguíneo (a, b, ab, o):"), self.tipoSanguineoInput)
        layout.addRow(btnTipo)
        layout.addRow(QLabel("Fator RH (+ ou -):"), self.fatorRhInput)
        layout.addRow(btnRh)
        layout.addRow(self.resultTab3)
        
        self.tab3.setLayout(layout)
        
    def verificarDoacao(self):
        doador = self.doadorInput.text().strip().lower()
        receptor = self.receptorInput.text().strip().lower()
        
        if not doador or not receptor:
            self.resultTab1.setText("Por favor, insira o nome do doador e do receptor.")
            return
        
        # Consulta Prolog: podeDoar(doador, receptor)
        query = list(self.prolog.query(f"podeDoar({doador},{receptor})"))
        
        if query:
            self.resultTab1.setText(f"{doador.capitalize()} PODE doar para {receptor.capitalize()}.")
        else:
            self.resultTab1.setText(f"{doador.capitalize()} NÃO PODE doar para {receptor.capitalize()}.")
    
    def quemDoaPara(self):
        pessoa = self.pessoaTab2.text().strip().lower()
        if not pessoa:
            self.resultTab2.setText("Insira o nome da pessoa.")
            return
        
        # Consulta: podeDoar(X, pessoa)
        results = list(self.prolog.query(f"podeDoar(X,{pessoa})"))
        if results:
            doadores = [res['X'] for res in results]
            self.resultTab2.setText("Doadores: " + ", ".join([x.capitalize() for x in doadores]))
        else:
            self.resultTab2.setText("Ninguém pode doar para essa pessoa ou ela não existe na base.")
    
    def paraQuemDoador(self):
        pessoa = self.pessoaTab2.text().strip().lower()
        if not pessoa:
            self.resultTab2.setText("Insira o nome da pessoa.")
            return
        
        # Consulta: podeDoar(pessoa, Y)
        results = list(self.prolog.query(f"podeDoar({pessoa},Y)"))
        if results:
            receptores = [res['Y'] for res in results]
            self.resultTab2.setText("Esta pessoa pode doar para: " + ", ".join([x.capitalize() for x in receptores]))
        else:
            self.resultTab2.setText("Essa pessoa não pode doar para ninguém (ou não existe na base).")
    
    def quemTemTipo(self):
        tipo = self.tipoSanguineoInput.text().strip().lower()
        if tipo not in ["a", "b", "ab", "o"]:
            self.resultTab3.setText("Tipo inválido. Use a, b, ab ou o.")
            return
        
        results = list(self.prolog.query(f"tiposanguineo(X,{tipo})"))
        if results:
            pessoas = [res['X'] for res in results]
            self.resultTab3.setText(f"Pessoas com tipo {tipo.upper()}: " + ", ".join([x.capitalize() for x in pessoas]))
        else:
            self.resultTab3.setText(f"Ninguém possui tipo sanguíneo {tipo.upper()} na base.")
    
    def quemTemRh(self):
        rh = self.fatorRhInput.text().strip()
        if rh not in ["+", "-"]:
            self.resultTab3.setText("Fator Rh inválido. Use + ou -.")
            return
        
        results = list(self.prolog.query(f"fatorrh(X,{rh})"))
        if results:
            pessoas = [res['X'] for res in results]
            self.resultTab3.setText(f"Pessoas com fator Rh {rh}: " + ", ".join([x.capitalize() for x in pessoas]))
        else:
            self.resultTab3.setText(f"Ninguém possui fator Rh {rh} na base.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BloodDonationApp()
    window.show()
    sys.exit(app.exec_())
