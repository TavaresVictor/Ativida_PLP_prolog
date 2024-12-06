% regras.pl

% Fatos de compatibilidade de Tipos Sanguíneos
compativel(a, a).
compativel(a, ab).
compativel(b, b).
compativel(b, ab).
compativel(ab, ab).
compativel(o, a).
compativel(o, b).
compativel(o, ab).
compativel(o, o).


% Compatibilidade de Fator RH
rhcomp('+', '+').
rhcomp('-', '+').
rhcomp('-', '-').


% Regras, determinar se X pode doar para Y
podedoar(X, Y) :-
    tiposanguineo(X, TSX),
    tiposanguineo(Y, TSY),
    compativel(TSX, TSY),
    fatorrh(X, RHX),
    fatorrh(Y, RHY),
    rhcomp(RHX, RHY),
    idade(X, I), I >= 18, I =< 65,
    peso(X, P), P > 50.


% Perguntas
% ?- podedoar(joao, maria).
% ?- podedoar(Fulano, Y).
% ?- tiposanguineo(X, a).
% ?- fatorrh(X, '+').
