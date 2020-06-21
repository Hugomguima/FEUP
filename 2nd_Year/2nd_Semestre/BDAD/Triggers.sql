Drop trigger if EXISTS R1;

CREATE trigger R1
after insert on Reparacao
WHEN new.idCliente is null
BEGIN
    update Reparacao
    set idCliente = (SELECT idCliente
                     FROM Carro
                     WHERE idCarro = new.idCarro)
    WHERE idCarro == new.idCarro;
End;


Drop trigger if EXISTS R3;
Create trigger R3
After insert on ReparacaoPeca
Begin
    Update Peca
    Set quantidade = quantidade - new.quantidade
    Where idPeca = new.idPeca;
End;
