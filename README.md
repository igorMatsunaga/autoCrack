<h1>AutoCrack - Aircrack-ng automatizado</h1>

<!-- wp:tadv/classic-paragraph -->
<p style="text-align: justify;">O autocrack é um simples script desenvolvido em Python, com a finalidade de automatizar ataques a redes wireless WPA/WPA2 utilizando o aircrack-ng e o crunch no Kali Linux.</p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:tadv/classic-paragraph -->
<h3>Clonar o autoCrack</h3>
<p style="text-align: justify;">Você pode realizar o download diretamente no <a href="https://github.com/igorMatsunaga/autoCrack">github</a> ou realizar o clone diretamente do terminal.</p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>git clone https://github.com/igorMatsunaga/autoCrack</code></pre>
<!-- /wp:code -->

<!-- wp:tadv/classic-paragraph -->
<p style="text-align: justify;">Todas as ferramentas necessárias para utilização vem por padrão no Kali Linux. Se você utiliza maquina virtual será necessário o uso de um <a href="https://loja.nsworld.com.br/collections/wi-fi/products/alfa-usb-awus036nh-3070l-ralink-chipset-2000-mw-wireless-n-adaptador-usb-wifi-150-mbps-usb-wifi-placa-de-rede-sem-fio-1-pc-por-conjunto">adaptador wireless.</a></p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:tadv/classic-paragraph -->
<h3>Utilização</h3>
<p>Após o download acesse a pasta onde foi baixado o script.&nbsp;</p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>cd autoCrack
python autoCrack.py</code></pre>
<!-- /wp:code -->

<!-- wp:image {"id":3010} -->
<figure class="wp-block-image"><img src="https://nsworld.com.br/wp-content/uploads/2019/06/autocrack1.png" alt="" class="wp-image-3010"/></figure>
<!-- /wp:image -->

<!-- wp:tadv/classic-paragraph -->
<p style="text-align: justify;">Após iniciar o script, uma mensagem com um aviso e dado, e apenas um lembrete para que você analise se sua placa suporta modo monitoramento e injeção. Para continuar o ataque digite 'c' se quiser sair digite 's'.</p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:tadv/classic-paragraph -->
<p style="text-align: justify;">A segunda pergunta pede que você insira a interface de rede que será usada. Caso não saiba sua interface utilize o comando "wiconfig" ou "ifconfig", lembrando que o ataque deve ser realizado utilizando uma placa de rede wireless ou adaptador de rede USB.</p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:tadv/classic-paragraph -->
<p style="text-align: justify;">A terceira pergunta refere-se aos processos de rede que podem bloquear o ataque, caso utilize a própria placa da maquina muitas vezes ocorrem erros devido a esses processos, caso utilize um adaptador USB não será necessário matar os processos.</p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:image {"id":3011} -->
<figure class="wp-block-image"><img src="https://nsworld.com.br/wp-content/uploads/2019/06/autoCrack2.png" alt="" class="wp-image-3011"/></figure>
<!-- /wp:image -->

<!-- wp:tadv/classic-paragraph -->
<p style="text-align: justify;">Um novo terminal será aberto onde pode ser visto todas as redes que estão no alcance. O terminal principal pegunta qual o canal da rede. Observe no novo terminal o 'ch' da rede escolhida e o insira no terminal principal.</p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:image {"id":3013} -->
<figure class="wp-block-image"><img src="https://nsworld.com.br/wp-content/uploads/2019/06/autocrack1-1.png" alt="" class="wp-image-3013"/><figcaption> canais de rede em destaque</figcaption></figure>
<!-- /wp:image -->

<!-- wp:tadv/classic-paragraph -->
<p>Iinforme o BSSID<span>(Basic Service Set Identifier)da rede escolhida.</span></p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:image {"id":3014} -->
<figure class="wp-block-image"><img src="https://nsworld.com.br/wp-content/uploads/2019/06/bssid.png" alt="" class="wp-image-3014"/></figure>
<!-- /wp:image -->

<!-- wp:tadv/classic-paragraph -->
<p>A próxima pergunta solicita o ESSID<span>(Extended Service Set Identifier) da rede escolhida.</span></p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:image {"id":3015} -->
<figure class="wp-block-image"><img src="https://nsworld.com.br/wp-content/uploads/2019/06/essid.png" alt="" class="wp-image-3015"/></figure>
<!-- /wp:image -->

<!-- wp:tadv/classic-paragraph -->
<p><span> Depois requer o MAC (Media Access Control) e por ultimo o nome de saída que você escolher.</span></p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:image {"id":3016} -->
<figure class="wp-block-image"><img src="https://nsworld.com.br/wp-content/uploads/2019/06/mac.png" alt="" class="wp-image-3016"/></figure>
<!-- /wp:image -->

<!-- wp:image {"id":3021} -->
<figure class="wp-block-image"><img src="https://nsworld.com.br/wp-content/uploads/2019/06/mats.png" alt="" class="wp-image-3021"/></figure>
<!-- /wp:image -->

<!-- wp:tadv/classic-paragraph -->
<p>Automaticamente o script irá tentar realizar o handshake abrindo amais alguns terminais, caso o ataque pare antes da captura, o termina principal lhe oferece a opção de atacar novamente (r) caso o handshake tenha sido capturado escolha a opção 'c'.</p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:image {"id":3017} -->
<figure class="wp-block-image"><img src="https://nsworld.com.br/wp-content/uploads/2019/06/hand.png" alt="" class="wp-image-3017"/><figcaption>Novo terminal onde você saberá se o handshake foi realizado com sucesso.</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"id":3018} -->
<figure class="wp-block-image"><img src="https://nsworld.com.br/wp-content/uploads/2019/06/hacap.png" alt="" class="wp-image-3018"/><figcaption>Repita o ataque ou avance</figcaption></figure>
<!-- /wp:image -->

<!-- wp:tadv/classic-paragraph -->
<p>O próximo passo solicitado refere-se a uso de uma wordlist própria ou utilizar a opção de criação de uma nova wordlist.</p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:image {"id":3019} -->
<figure class="wp-block-image"><img src="https://nsworld.com.br/wp-content/uploads/2019/06/list.png" alt="" class="wp-image-3019"/></figure>
<!-- /wp:image -->

<!-- wp:tadv/classic-paragraph -->
<h3>WordList Pessoal</h3>
<p>Caso queira utilizar sua própria lista de palavras insira a opção 'p'. Será perguntado qual o caminho da lista, caso a lista esteja na mesma pasta que o autoCrack basta inserir o nome da lista.</p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:image {"id":3020} -->
<figure class="wp-block-image"><img src="https://nsworld.com.br/wp-content/uploads/2019/06/lista.png" alt="" class="wp-image-3020"/></figure>
<!-- /wp:image -->

<!-- wp:tadv/classic-paragraph -->
<h3>Criação de WorldList </h3>
<p style="text-align: justify;">Para desenvolver uma lista de palavras utilizando o autoCrack escolha a opção 'd'.</p>
<p style="text-align: justify;">Para a criação da lista serão necessários 3 informações.</p>
<ol>
<li style="text-align: justify;">O minimo de caracteres utilizados, por exemplo caso escolha o minimo de 2, sua lista começara com 2 dígitos(ex: aa, ab, ac...).</li>
<li style="text-align: justify;">O máximo de caracteres utilizados, seguindo o exemplo acima caso escolha 4 a lista começaria com 2 digitos e terminaria com 4 digitos (aa..., zzzz).</li>
<li style="text-align: justify;">A ultima configuração a ser utilizada são os caracteres utilizados. Você tem liberdade de escolher todos os tipos de caracteres como caracteres especiais, números, letras são diferenciadas entre maiúsculas e minusculas, mas se lembre que a lista pode ficar gigantesca e necessitará de muito espaço em disco.</li>
</ol>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:image {"id":3022} -->
<figure class="wp-block-image"><img src="https://nsworld.com.br/wp-content/uploads/2019/06/cruch.png" alt="" class="wp-image-3022"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>O aircrack-ng irá realizar um ataque de força bruta, esse tipo de ataque pode demorar segundos caso a vítima possua uma senha fraca, por isso sempre utilize senhas fortes que contenham letras maiúsculas, minusculas, números e caracteres especiais.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":3023} -->
<figure class="wp-block-image"><img src="https://nsworld.com.br/wp-content/uploads/2019/06/crack.png" alt="" class="wp-image-3023"/></figure>
<!-- /wp:image -->

<!-- wp:tadv/classic-paragraph -->
<p>Que a segurança esteja com você!!! Bons estudos.</p>
<!-- /wp:tadv/classic-paragraph -->
