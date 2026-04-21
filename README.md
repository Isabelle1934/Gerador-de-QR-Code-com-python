## Gerador-de-QR-Code-com-python

# Introdução
Você já se perguntou como funcionam os códigos QR ou como as imagens procedurais são geradas? Você já quis enviar um link para alguém de um site muito mais legal? Se você disse sim para alguma dessas perguntas, você está com sorte!

Neste tutorial do projeto, vamos aprender a criar um QR code em Python com qrcode, pillow e apenas cinco linhas de código.

Vamos lá!

Exemplo QR

# O que é um código QR?
O código QR, abreviação de Quick Response code, foi originalmente inventado em 1994 por uma empresa japonesa de tecnologia. É um código de barras 2D contendo padrões pretos sobre fundo branco. No entanto, isso não é um rabisco comum: códigos QR são capazes de armazenar enormes quantidades de dados em um espaço enganosamente pequeno. Esses retângulos pretos podem armazenar links, texto, basicamente qualquer coisa que você quiser... e pode ser acessado simplesmente escaneando de qualquer dispositivo móvel!

Um código QR é importante porque oferece aos usuários uma maneira simples de acessar algo em uma fonte não convencional (por exemplo, em um pedaço de papel). Colocar um QR code em um pedaço de papel é uma experiência muito melhor e mais rápida para o usuário do que colocar um link para um site. Por causa disso, os códigos QR estão se tornando mais usados do que os códigos de barras UPC e são encontrados em cardápios de restaurantes, cartões de visita e até em anúncios do Super Bowl!


Chega de QR codes, vamos aprender a criar um!

# Configuração
Primeiro, vá ao editor de código Python que você escolher (recomendamos o VS Code) e crie um novo arquivo chamado qr_code.py. É aqui que vamos escrever nosso código.

Nota: Você pode chamar seu arquivo de qualquer nome, menos qrcode.py. Isso porque qrcode.py é um arquivo que já existe como parte da biblioteca que vamos usar, e chamar seu arquivo, isso vai sobrescrever as funções da biblioteca.qrcode

Para começar, precisamos instalar as duas bibliotecas:

A biblioteca qrcode: Esta biblioteca nos permite realizar todas as nossas operações relacionadas a códigos QR.
A biblioteca de travesseiros: Essa biblioteca nos ajuda a processar e salvar imagens.
Para instalar e , execute este comando dentro do terminal VS Code:qrcodepillow

pip install qrcode pillow

Para este tutorial, estamos usando qrcode versão 7.3.1 e Pillow versão 9.2.0.

Em seguida, adicione esta linha de código à primeira linha de qr_code.py:

import qrcode

Essa linha de código garante que as duas bibliotecas possam ser usadas no restante do nosso código, já que o código Python é executado de cima a baixo em um arquivo. Só precisamos importar , porque é implicitamente importado.qrcodepillow

# Criando o Código QR
Primeiro, queremos um link que queremos mostrar. Vamos usar um vídeo clássico do YouTube.

Podemos armazenar essa URL do YouTube em uma variável chamada :website_link

website_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

Em seguida, queremos criar uma instância de . Como é uma biblioteca Python, podemos chamar o construtor do pacote para criar um objeto, personalizado de acordo com nossas especificações.qrcodeqrcode

Neste exemplo, vamos criar um código QR com uma versão de 1, e um tamanho de caixa e tamanho de borda de 5.

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)

O parâmetro é um inteiro de 1 a 40 que controla o tamanho do código QR.version
O parâmetro controla quantos pixels cada "caixa" do código QR tem.box_size
O parâmetro controla quantas caixas a borda deve ter de espessura.border
Como exercício, tente absorver esses parâmetros como entrada e explicar ao usuário como configurar isso, para que ele possa criar o código QR conforme suas próprias especificações.

Visite a documentação para mais informações sobre os parâmetros em .qrcode.QRCode(...)

Depois, os dados (especificamente, o link que especificamos antes) são adicionados ao código QR, usando . O código QR é então gerado usando:.add_data().make()

qr.add_data(website_link)
qr.make()

Por fim, salvamos esse código QR criado em um objeto travesseiro usando:imgqr.make_image()

img = qr.make_image(fill_color = 'black', back_color = 'white')

Definindo a cor da linha para preto.fill_color
Definindo a cor de fundo para branco.back_color
Por fim, precisamos armazenar e salvar o arquivo. Podemos fazer isso usando o comando do travesseiro. Especificamos o nome do arquivo entre parênteses, que é o caso nosso.save()youtube_qr.png

img.save('youtube_qr.png')

Agora terminamos! Aqui está o código completo:

import qrcode

website_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save('youtube_qr.png')

Você deve ver a imagem youtube_qr.png aparecer no lado esquerdo do VS Code, e pode abri-la para ver como ela é.

Exemplo QR

# Conclusão
Você pode adicionar este QR code em qualquer lugar que quiser, no seu site ou por e-mail!

## Melhorias
Para melhorar isso, poderíamos fazer algumas coisas:

Permita que o link do site seja digitado usando a função.input()
Permita que os usuários personalizem o código QR gerado.
Automatize o processo para criar múltiplos códigos QR.
Inclua mais funções (ou parâmetros de objeto) da biblioteca qrcode.
Tente mudar as cores e estilos dos QR codes gerados usando diferentes módulos de gaveta e cores de preenchimento.
Use uma biblioteca de aplicativos (como o Tkinter) para adicionar uma interface de usuário.
Confira outras bibliotecas de códigos QR como pyqrcode.
