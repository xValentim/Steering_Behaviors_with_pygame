# Steering Behaviors with pygame
Nesse projeto, fizemos a modelagem termodinâmica de uma xícara de café de vidro, com altura h de 7cm e raio R de 3.5cm (Depois de ler a conclusão 3, volte e consulte esse valor). Nesse cenário, tivemos 3 objetivos:
> 1) Determinar o tempo de resfriamento do café em função da variação da condutividade térmica da xícara e do calor sensível

> 2) Determinar o tempo de resfriamento do café em função da variação da altura h e do raio R da xícara

> 3) Determinar o tempo de resfriamento do café fixando o volume e variando o raio R

## Validação
Para fazermos a validação, utilizamos um arduino e dois sensores NTC10K para medir a temperatura da xícara e do café, para que no final plotássemos um gráfico de tal forma que fosse possível confrontar nossos dados do modelo com o dados reais (experimentais). O tempo de resfriamento (atingir 35°C) foi de 76.98 minutos.
### Gráfico de validação:
![img1](validacao.png)

## Conclusões
Tendo em vista que o nosso modelo é coerente com a realidade, é possível estabelecer conclusões a respeito dos nossos objetivos.

### Conclusão 1:

> "1) Determinar o tempo de resfriamento do café em função da variação da condutividade térmica da xícara e do calor sensível"

Acompanhe o gráfico conclusivo em 3 dimensões (O gradiente represente o teceiro eixo, que é o tempo de resfriamento em minutos):
![img1](varia_cr_kr2.png)

### Conclusão 2:

> "2) Determinar o tempo de resfriamento do café em função da variação da altura h e do raio R da xícara"

Acompanhe o gráfico conclusivo em 3 dimensões (O gradiente represente o teceiro eixo, que é o tempo de resfriamento em minutos):
![img1](varia_r_h.png)

### Conclusão 3:

> "3) Determinar o tempo de resfriamento do café fixando o volume e variando o raio R"

Acompanhe o gráfico que registra o tempo de resfriamento em minutos em função de R (mantendo constante o volume da xícara):
![img1](variaR_fixa_v0.png)

### Conclusão 3.1
Note que com o resultado da conclusão 3, é possível observar um valor ideal para as dimensões da xícara. Agora, consulte o valor das dimensões da xícara de vidro que usamos para fazer a validação do nosso modelo. São muito parecidas!
#### Dimensões da xícara real:
- Altura: h = 7 cm
- Raio: R = 3.5 cm
- Tempo de resfriamento: t = 76.98 minutos

#### Dimensões da xícara ideal:
- Altura: h = 6.62 cm
- Raio: R = 3.6 cm
- Tempo de resfriamento: t = 77.03 minutos

Note que o fabricante da xícara teve o cuidado de procurar dimensões que fossem razoáveis para a xícara, de tal forma que ela  prolongassem a temperatura do café.

## Tecnologias usadas nesse projeto

![Arduino](https://img.shields.io/badge/Arduino-007ACC?style=for-the-badge&logo=arduino&logoColor=white)
![Python](https://img.shields.io/badge/Python-2D7DB1?style=for-the-badge&logo=python&logoColor=yellow)