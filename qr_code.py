import qrcode

website_link = 'https://github.com/Isabelle1934'

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
#O parâmetro é um inteiro de 1 a 40 que controla o tamanho do código QR.version
#O parâmetro controla quantos pixels cada "caixa" do código QR tem.box_size
#O parâmetro controla quantas caixas a borda deve ter de espessura.border

qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color = 'black', back_color = 'white')
#Definindo a cor da linha para preto.fill_color
#Definindo a cor de fundo para branco.back_color

