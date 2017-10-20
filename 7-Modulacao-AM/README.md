# Modulação
A modulação em amplitude (AM) é uma forma de modulação em que a amplitude de um sinal senoidal/cossenoidal varia em função do sinal principal.

Isto é, o sinal senoidal/cossenoidal é uma portadora (carry) que tem a frequência e a fase constantes. Aplicando a portadora em função do sinal principal (de interesse), há a modulação da amplitude deste sinal. Com isso, o sinal principal desloca-se na frequência, ocupando outra banda.

Isso permite que possamos transmitir mais de um sinal ao mesmo tempo, pelo mesmo meio, pois podemos transmitir diferentes sinais em bandas diferentes e aplicar a demodulação ao receber o sinal para recuperar os sinais de interesse em suas respectivas bandas.

### No projeto:
- Primeiro foi aplicado um filtro passa baixa de (4kHz) nos áudios a serem transmitidos. Isso diminuiu a banda dos sinais e fez com que a alocação de banda deles fosse mais fácil, diminuindo a interferência que um aplica no outro.
- Posteriormente os sinais a serem transmitidos foram multiplicados por portadoras de mesmo tamanho, sendo deslocados na frequência.
- Como os dois áudios deveriam ser mandados juntos, os dois áudios deslocados foram somados (tinham o mesmo tamanho) e transmitidos.

# Demodulação


# Frequências das portadoras utilizadas e bandas
As frequências das portadoras utilizadas foram 4kHz e 14kHZ, pois assim o sinal de um áudio não transpõem o sinal do outro áudio em outra banda. A banda ocupada pelo áudio 1 foi de 1kHz a 7kHz e a segunda banda, ocupada pelo segund áudio foi de 8kHz a 19kHz.

![](./img/transmitter_charts.png)
