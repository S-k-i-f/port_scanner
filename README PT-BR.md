# Scanner de Portas

Uma ferramenta educacional de segurança de redes desenvolvida em Python para varredura de portas. Este projeto demonstra o reconhecimento de rede ao implementar um scanner TCP _dual-stack_ que consulta portas administrativas e de serviços padrão no intervalo de $1$ até $1024$.

---
## 1. Lógica de Reconhecimento

Para otimizar o desempenho e a confiabilidade em ambientes de rede modernos, o script opera sob os seguintes mecanismos:

- **Resolução Dual-Stack:** Antes de iniciar a varredura, o programa realiza uma validação automática da versão do _Internet Protocol_ (IP). Ele vincula dinamicamente a configuração correta do socket (`socket.AF_INET` ou `socket.AF_INET6`) com base no formato do endereço de destino, sem necessidade de intervenção manual do usuário.
- **Varredura da Conexão TCP:** O script realiza o _handshake_ de três vias do protocolo TCP utilizando a biblioteca nativa `socket` do Python. Ele tenta se conectar a cada porta designada no intervalo estabelecido para determinar o seu estado atual.

### 1.1 Funcionamento Técnico e Matemático

O scanner utiliza o método de baixo nível `socket.connect_ex()` para realizar a tentativa de conexão. O programa não utiliza tratamento de exceções em caso de falhas, este método retorna um código de erro numérico:

- Um código de retorno igual a $0$ indica uma conexão bem-sucedida, significando que a porta de destino está ativa e aberta.
- Qualquer valor de retorno diferente de zero indica uma falha de conexão, sinalizando que a porta está fechada ou bloqueada.

Durante as tentativas de conexão, o laço de repetição `for port in range(1, 1025)` define o subconjunto de portas a serem testadas. O método `range` gera um intervalo semiaberto:

$$P = \{x \in \mathbb{Z} \mid 1 \le x < 1025\}$$

- $P = 1024$ representa a cardinalidade de conjunto de intervalos em portas conhecidas, reservadas para serviços essenciais da web.

Para otimizar a velocidade de varredura e evitar que o programa fique travado indefinidamente ao encontrar portas com pacotes descartados ou protegidas por sistemas de segurança, um tempo limite rígido ($T$) de conexão é aplicado:
$$T = 0.5 \text{ segundos}$$

Isso garante que o tempo total de varredura das portas permaneça previsível e altamente eficiente.

---
## 2. Recursos

- **Linha de Comando Estilizada:** Utiliza a biblioteca externa `pyfiglet` para customizar a interface de linha de comando (CLI).
- **Sanitização Robusta de Entrada:** Utiliza a biblioteca nativa `ipaddress` para validar o formato do IP do alvo antes de iniciar conexões de rede, evitando falhas de execução por tipos de endereço.
- **Sem Dependências de Rede Externas:** Construído inteiramente sobre a biblioteca padrão de redes do Python, garantindo uma execução leve e segura.

---
## 3. Pré-requisitos

Para executar este script, é necessário o **Python 3.10** ou versões mais recentes instalado em sua máquina devido ao uso da estrutura de controle de fluxo `match-case`.

- **Instalação de Dependências:** A única dependência externa necessária é a biblioteca `pyfiglet`. Instale-as executando o comando abaixo no seu terminal:
    - `pip install pyfiglet`.
- **Execução:** Clone o repositório ou faça o download do arquivo `port_scanner.py`. Em seguida, navegue até a pasta do arquivo pelo terminal e execute:
	- `python port_scanner.py`.

### 3.1 Isenção de Responsabilidade

Esta ferramenta foi desenvolvida exclusivamente para fins **educacionais, de pesquisa e de conscientização sobre segurança**.

- A varredura de redes ou sistemas sem autorização prévia e explícita do proprietário da infraestrutura pode ser considerada uma atividade maliciosa e é ilegal em diversas jurisdições.
- O autor deste software não se responsabiliza por quaisquer danos, incidentes de segurança ou consequências legais decorrentes do uso inadequado ou malicioso desta ferramenta.
- Use com responsabilidade e apenas em redes ou ambientes de sua propriedade ou nos quais possua autorização expressa de teste.
