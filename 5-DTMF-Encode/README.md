# Frequências dos Tons
Os tons do DTMF são formados pela composição de duas senoides em diferentes frequências, uma com frequência baixa (< 941 Hz) e outra com frequência alta (> 1209 Hz).

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

# Documentação - Must Have
- Descrever a geração dos tons
- Descrever as frequências que compõem cada tom
- Plotar e comentar os gráficos de cada tom com o do gerado e recebido.
