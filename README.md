# O chipeitor Tabajara
## Trabalho para a cadeira de projeto e otimização de algoritmos

### Enunciado

Você está dando uma ajuda para o pessoal da microeletrônica para posicionar componentes em um novo chip revolucionário. Eles já tem o projeto de uma série de componentes que devem ser posicionados em uma placa quadrada e para facilitar eles imaginam a placa com tamanho n * n e cada componente ocupando uma posição (i, j) na placa (portanto existem n^2 componentes), mas querem calcular a posição de cada um deles de forma que as conexões entre os componentes sejam as mais curtas possíveis. Mais especificamente, eles querem que a soma do comprimento das conexões seja o menor possível para usar o mínimo de espaço com conexões.

Eles fornecem a você arquivos descrevendo a placa e as ligações entre os componentes.

Nestes arquivos o primeiro número indica o tamanho n da placa e o segundo indica quantas conexões entre os componentes serão informadas. Depois deles segue o posicionamento atual dos componentes, numerados de 0 até n^2-1. No exemplo ao lado, os componentes estão na sua situação inicial, que vai ser alterada pelo seu programa otimizador de posicionamento.

EM seguida vem a lista de conexões entre os componentes, indicando quem liga com quem. Depois de conversar com os engenheiros, você completa suas informações com detalhes que podem ser importantes:

1. A distância usada para medição é a distância euclidiana.
2. A distância entre os elementos da linha l1 e da coluna c1 e da linha l2 e da coluna c2 é dada pela distancia entre (l1, c1) e (l2, c2).
3. É uma boa ideia que seu programa escreva o resultado atual à medida que progride.
4. É outra boa ideia fazer seu programa salvar o posicionamento à medida que faz a otimização, pois assim ele pode ser reiniciado mais tarde do ponto em que parou.

### Formato de input

3 18

0 1 2

3 4 5

6 7 8

0 3

1 4

4 0

4 2

4 3

5 4

5 0

5 2

6 5

6 0

4 6

2 6

6 1

3 6

6 7

7 0

5 7

4 8


Para o input acima, um algoritmo genético que tenta trocar os elementos de lugar pode resultar em:
3 6 2

0 4 5

1 7 8

que tem um comprimento total de ligações valendo 23.957 unidades.



## Como rodar

`python3 chip.py "nome do arquivo input"`


## Como gerar casos para a minha implementação:
`python3 gera_caso.py >> "arquivo"`

o comando >> salva o output do terminal em um arquivo. Tudo que for impresso na tela pelo
"gera_caso.py" vai ser salvo no arquivo.

Após rodar o comando acima, digite o valor de n (a matriz é n*n), aperte enter, e digite a
quantidade de fios que voce quer, e aperte enter.

Para a minha implementação, não é necessario ler a matriz no arquivo de input, já que eu crio ela.


