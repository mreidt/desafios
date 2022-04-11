# Desafio 2: Crawlers

Parte do trabalho na IDwall inclui desenvolver *crawlers/scrapers* para coletar dados de websites.
Como nós nos divertimos trabalhando, às vezes trabalhamos para nos divertir!

O Reddit é quase como um fórum com milhares de categorias diferentes. Com a sua conta, você pode navegar por assuntos técnicos, ver fotos de gatinhos, discutir questões de filosofia, aprender alguns life hacks e ficar por dentro das notícias do mundo todo!

Subreddits são como fóruns dentro do Reddit e as postagens são chamadas *threads*.

Para quem gosta de gatos, há o subreddit ["/r/cats"](https://www.reddit.com/r/cats) com threads contendo fotos de gatos fofinhos.
Para *threads* sobre o Brasil, vale a pena visitar ["/r/brazil"](https://www.reddit.com/r/brazil) ou ainda ["/r/worldnews"](https://www.reddit.com/r/worldnews/).
Um dos maiores subreddits é o "/r/AskReddit".

Cada *thread* possui uma pontuação que, simplificando, aumenta com "up votes" (tipo um like) e é reduzida com "down votes".

Sua missão é encontrar e listar as *threads* que estão bombando no Reddit naquele momento!
Consideramos como bombando *threads* com 5000 pontos ou mais.

## Entrada
- Lista com nomes de subreddits separados por ponto-e-vírgula (`;`). Ex: "askreddit;worldnews;cats"

### Parte 1
Gerar e imprimir uma lista contendo a pontuação, subreddit, título da thread, link para os comentários da thread e link da thread.
Essa parte pode ser um CLI simples, desde que a formatação da impressão fique legível.

### Parte 2
Construir um robô que nos envie essa lista via Telegram sempre que receber o comando `/NadaPraFazer [+ Lista de subrredits]` (ex.: `/NadaPraFazer programming;dogs;brazil`)

### Dicas
 - Use https://old.reddit.com/
 - Qualquer método para coletar os dados é válido. Caso não saiba por onde começar, procure por JSoup (Java), SeleniumHQ (Java), PhantomJS (Javascript) e Beautiful Soup (Python).

# Como utilizar
- Os requerimentos devem ser instalados utilizando o _pip_ (`pip install -r requirements.txt`);
- O projeto foi criado utilizando _Python 3.8.10_;

## Execução da parte 1 do desafio de crawler
- Para executar a primeira parte do desafio, rodar o arquivo `scrapper.py`;
- O arquivo executa como um script, por isso é possível utilizar parâmetros para sua execução;
- Os parâmetros para a execução encontram-se na tabela abaixo:

| Parâmetro  | Expandido       | Tipo        | Funcionalidade                                                  | 
|:-----------|:----------------|:------------|:----------------------------------------------------------------| 
| h          | help            | opcional    | exibe na tela o help do script                                  |
| subreddits | subreddits      | obrigatório | informa os subreddits em que se deseja executar o crawler, separados por `;`. ex.: `'askreddit;worldnews;cats'` |
| f          | output_filename | opcional    | informa um arquivo de saída para salvar o resultado do crawler  |

## Execução do bot do Telegram (parte 2 do desafio)
- Criar um bot seguindo a [documentação oficial do Telegram](https://core.telegram.org/bots#3-how-do-i-create-a-bot);
- O Telegram gerará uma chave para o seu bot criado;
- Utilize o comando abaixo no diretório do projeto para configurar a sua chave corretamente: `sed -i "s/INSERT-YOUR-KEY-HERE/CHAVE_GERADA_PELO_TELEGRAM/g" constants.py`, substituindo `CHAVE_GERADA_PELO_TELEGRAM` pela chave gerada pelo Telegram para o seu bot;
- Inicie a execução do bot com o comando `python telegram_bot.py`;
- No seu aplicativo Telegram, converse com o bot utilizando o comando `/NadaPraFazer [+ Lista de subrredits]` (ex.: `/NadaPraFazer programming;dogs;brazil`);
- Caso você envie o comando sem uma lista de subreddits, o bot irá procurar por threads em alta no `/r/random`;
- Para parar a execução do bot, utilizar `CTRL` + `C`;
