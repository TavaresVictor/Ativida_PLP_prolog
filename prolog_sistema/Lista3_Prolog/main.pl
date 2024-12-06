% main.pl

% Arquivo Principal para Consultas e Execução

% Carregar os Módulos
:- consult('base_de_conhecimento.pl').
:- consult('regras.pl').

% Consultas de Exemplo
:- initialization(main).

main :-
    writeln("Consultas Disponíveis:"),
    writeln("1. podedoar(X, Y): Determina se X pode doar para Y."),
    writeln("2. tiposanguineo(X, T): Verifica o tipo sanguíneo de X."),
    writeln("3. fatorrh(X, RH): Verifica o fator RH de X."),
    halt.
