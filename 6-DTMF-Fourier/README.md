# Frequências dos Tons
Os tons do *Dual tone multi frequency* (DTMF) são formados pela composição de duas senoides em diferentes frequências, uma com frequência baixa (< 941 Hz) e outra com frequência alta (> 1209 Hz).

|            | 	1209 Hz    | 1336 Hz	 | 1477 Hz	   |
|------------|-------------|-------------|-------------|
| **697 Hz**	 | **1**       | **2**       | **3**       |
| **770 Hz**	 | **4**       | **5**       | **6**       |
| **852 Hz**	 | **7**       | **8**       | **9**       |
| **941 Hz**	 | **X**       | **0**       | **#**       |


#  Geração de tons

A geração de sons foi feita a partir do `encoderDTMF.py`, que utiliza dos pacotes numpy e sounddevice para respectivamente, gerar ondas senoidais e tocá-las como audios.

**obs:** O *sounddevice* pode ser instalado pelo: `pip install sounddevice`

As ondas dos tons são criadas a partir da "soma" de senoidais como no código abaixo:
```python
import numpy as np
import math

onda_do_tom = np.sin(2 * math.pi * x * lower) + np.sin(2 * math.pi * x * higher)
```

# Recepção de tons

A recepção de sons foi feita pelo arquivo `decoderDTMF.py`, que utiliza o pacote `sounddevice` e o `soundfile` para receber os sinais e gravar em um arquivo .wav. Ele grava os sinais emitidos pelo `encoderDTMF.py` através de múltiplos steps de gravação. Em cada step, ele grava o microfone do computador por um tempo pré-determinado, salva e plota o sinal.

**obs:** O *sounddevice* pode ser instalado pelo: `pip install soundfile`

# Gráficos dos tons gerados
- [Tom 0](https://github.com/martimfj/mpmf/blob/master/5-DTMF-Encode/doc/gerado/tom_0.png)
- [Tom 1](https://github.com/martimfj/mpmf/blob/master/5-DTMF-Encode/doc/gerado/tom_1.png)
- [Tom 2](https://github.com/martimfj/mpmf/blob/master/5-DTMF-Encode/doc/gerado/tom_2.png)
- [Tom 3](https://github.com/martimfj/mpmf/blob/master/5-DTMF-Encode/doc/gerado/tom_3.png)
- [Tom 4](https://github.com/martimfj/mpmf/blob/master/5-DTMF-Encode/doc/gerado/tom_4.png)
- [Tom 5](https://github.com/martimfj/mpmf/blob/master/5-DTMF-Encode/doc/gerado/tom_5.png)
- [Tom 6](https://github.com/martimfj/mpmf/blob/master/5-DTMF-Encode/doc/gerado/tom_6.png)
- [Tom 7](https://github.com/martimfj/mpmf/blob/master/5-DTMF-Encode/doc/gerado/tom_7.png)
- [Tom 8](https://github.com/martimfj/mpmf/blob/master/5-DTMF-Encode/doc/gerado/tom_8.png)
- [Tom 9](https://github.com/martimfj/mpmf/blob/master/5-DTMF-Encode/doc/gerado/tom_9.png)
- [Tom *](https://github.com/martimfj/mpmf/blob/master/5-DTMF-Encode/doc/gerado/tom_A.png)
- [Tom HashTag](https://github.com/martimfj/mpmf/blob/master/5-DTMF-Encode/doc/gerado/tom_H.png)

# Gráficos dos tons recebidos
- [Tom 0](https://github.com/martimfj/mpmf/blob/master/5-DTMF-Encode/doc/recebido/tom_0.png)
- [Tom 1](https://github.com/martimfj/mpmf/blob/master/5-DTMF-Encode/doc/recebido/tom_1.png)
- [Tom 2](https://github.com/martimfj/mpmf/blob/master/5-DTMF-Encode/doc/recebido/tom_2.png)
- [Tom 3](https://github.com/martimfj/mpmf/blob/master/5-DTMF-Encode/doc/recebido/tom_3.png)
- [Tom 4](https://github.com/martimfj/mpmf/blob/master/5-DTMF-Encode/doc/recebido/tom_4.png)
- [Tom 5](https://github.com/martimfj/mpmf/blob/master/5-DTMF-Encode/doc/recebido/tom_5.png)
- [Tom 6](https://github.com/martimfj/mpmf/blob/master/5-DTMF-Encode/doc/recebido/tom_6.png)
- [Tom 7](https://github.com/martimfj/mpmf/blob/master/5-DTMF-Encode/doc/recebido/tom_7.png)
- [Tom 8](https://github.com/martimfj/mpmf/blob/master/5-DTMF-Encode/doc/recebido/tom_8.png)
- [Tom 9](https://github.com/martimfj/mpmf/blob/master/5-DTMF-Encode/doc/recebido/tom_9.png)
- [Tom *](https://github.com/martimfj/mpmf/blob/master/5-DTMF-Encode/doc/recebido/tom_ask.png)
- [Tom HashTag](https://github.com/martimfj/mpmf/blob/master/5-DTMF-Encode/doc/recebido/tom_hash.png)


# Documentação - Must Have
- Descrever a geração dos tons
- Descrever as frequências que compõem cada tom
- Plotar e comentar os gráficos de cada tom com o do gerado e recebido.
