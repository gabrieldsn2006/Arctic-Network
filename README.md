# Arctic Network

## Link do Problema

[Kattis - Arctic Network](https://open.kattis.com/problems/arcticnetwork)

## Integrantes do Grupo

* Gabriel de Sousa Nobre
* Victor Lins Gurgel do Amaral
* Lorenzo Barros Calheiros Pinheiro

## Linguagem Utilizada

* Python 3

## Como Executar a Solução

O projeto possui duas formas de execução localizadas no diretório `src/`:

1. **Execução com arquivo de dados local:**
Para testar a solução lendo os dados diretamente do arquivo `dados/entradas_do_problema.txt`:
```bash
python src/main.py

```


2. **Execução via Entrada Padrão (Ambiente Kattis):**
Para executar a solução simulando a submissão da plataforma, fornecendo os dados manualmente ou redirecionando a entrada via terminal:
```bash
python src/kattis.py

```



## Explicação da Modelagem

O problema foi modelado utilizando a teoria dos grafos através de um grafo completo e ponderado:

* **Vértices ($P$):** Representam os postos avançados localizados no norte do país, definidos por suas coordenadas cartesianas $(x, y)$.
* **Arestas:** Representam os canais de comunicação por rádio possíveis entre cada par de postos.
* **Pesos das Arestas:** Correspondem à distância euclidiana em quilômetros calculada entre os postos conectados.
* **Canais de Satélite ($S$):** Permitem que qualquer posto com essa tecnologia se comunique instantaneamente com outro que também a possua, independentemente da distância. Na prática, isso significa que os satélites eliminam a necessidade de conexões de rádio entre as componentes em que estão instalados. Assim, dispor de $S$ canais de satélite nos permite dividir o grafo em até $S$ componentes conexas independentes (uma floresta geradora), reduzindo a distância máxima de rádio necessária.

O objetivo central é minimizar a potência dos transceptores (alcance $D$). Logo, buscamos a menor distância máxima $D$ que consiga interconectar os postos de forma a restarem exatamente $S$ componentes no grafo.

## Algoritmo Utilizado

A estratégia adota o **Algoritmo de Kruskal** para a construção da floresta geradora mínima, apoiado pela estrutura de dados **Disjoint Set Union (DSU)**:

1. **Geração e Ordenação:** Calculamos as distâncias euclidianas para todos os pares de vértices possíveis e as ordenamos em ordem crescente de peso.
2. **Estrutura DSU:** Gerenciamos a conectividade e prevenimos a criação de ciclos usando um DSU otimizado com as técnicas de *Path Compression* (na busca) e *Union by Rank* (na união das componentes).
3. **Construção Gulosa:** Iteramos sobre a lista ordenada de arestas. Se os vértices de uma aresta pertencem a componentes diferentes, realizamos a união.
4. **Critério de Parada:** O processo é interrompido assim que realizamos exatamente $P - S$ uniões bem-sucedidas, garantindo que o grafo foi reduzido a exatamente $S$ componentes conexas. A última distância adicionada antes da interrupção determina o valor mínimo de $D$ procurado.

## Análise de Complexidade

* **Complexidade de Tempo:** $O(E \log E)$, onde $E$ representa o total de arestas. Como o grafo é completo, temos $E = \frac{P \times (P - 1)}{2}$, ou seja, $O(P^2)$ arestas. O cálculo de todas as distâncias leva tempo $O(P^2)$ e a ordenação das arestas consome $O(E \log E)$, que equivale a $O(P^2 \log P)$. As operações do DSU operam em tempo quase constante devido às otimizações aplicadas ($O(\alpha(P))$). Portanto, o processo de ordenação domina o tempo de execução.
* **Complexidade de Espaço:** $O(P^2)$ para armazenar a lista completa com todas as arestas geradas. As estruturas internas de controle do DSU (`parent` e `rank`) ocupam espaço linear $O(P)$.

## Evidência do Accepted

*(A imagem comprobatória da submissão bem-sucedida encontra-se arquivada no repositório sob o caminho `evidencias/accepted.png`)*