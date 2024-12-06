# Ativida_PLP_prolog


README - Sistema Especialista de Doação de Sangue
Este projeto demonstra uma interface gráfica simples construída em Python (usando PyQt5) que se comunica com um back-end em Prolog usando PySWIP, para consultar compatibilidade de doação de sangue entre indivíduos, bem como informações sobre tipos sanguíneos e fator Rh.

Pré-requisitos
SWI-Prolog
É necessário ter o SWI-Prolog instalado.

Windows: Baixe e instale a partir de https://www.swi-prolog.org/download/stable
sudo apt-get install swi-prolog

Instale o python caso não tenha

Bibliotecas Python Necessárias
PyQt5:
pip install pyqt5
PySWIP:
pip install pyswip

Proximos passos:

python -c "import PyQt5; import pyswip"

Arquivos do Projeto
base_sangue.pl:
Contém a base de regras Prolog para verificação de compatibilidade sanguínea, peso, idade e fator Rh.

gui.py:
Fornece a interface gráfica e faz as consultas ao Prolog usando PySWIP.

Estrutura recomendada:

meu_projeto/
    base_sangue.pl
    gui.py
Como Executar
No terminal, vá até o diretório do projeto:

cd caminho/para/meu_projeto
Execute o script Python:

python gui.py

A janela da interface gráfica será aberta. Agora você pode:

Verificar se um doador pode doar para um receptor (inserindo os nomes e clicando no botão).
Consultar quem pode doar para uma pessoa ou para quem essa pessoa pode doar.
Obter listas de pessoas de um determinado tipo sanguíneo ou fator Rh.
Solução de Problemas
