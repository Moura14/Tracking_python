Documentação do Código de Rastreamento de Objetos em Vídeo


Este documento fornece uma visão geral do código Python que implementa o rastreamento de objetos em um vídeo usando a biblioteca OpenCV. O código utiliza algoritmos de rastreamento disponíveis no OpenCV para acompanhar um objeto selecionado no vídeo.


Requisitos

Certifique-se de ter a biblioteca OpenCV instalada. Você pode instalá-la usando o seguinte comando:

Pip install opencv-python


Visão Geral do Código

O código apresenta as seguintes etapas:
- Importação de Bibliotecas: Importa as bibliotecas necessárias, incluindo cv2 para OpenCV, sys para operações do sistema e randint para geração de cores aleatórias.
- Definição do Tipo de Rastreador: Define o tipo de rastreador a ser utilizado, selecionando um dos algoritmos de rastreamento disponíveis. Os algoritmos de rastreamento suportados são 'BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'MOSSE' e 'CSRT'.
- Criação do Rastreador: Dependendo da versão do OpenCV, cria um objeto de rastreamento correspondente ao tipo selecionado.
- Abertura do Vídeo: Carrega um vídeo a partir do caminho especificado e verifica se foi aberto com sucesso.
- Inicialização do Rastreamento: Lê o primeiro quadro do vídeo e permite que o usuário selecione a região de interesse (ROI) para rastrear. - Inicializa o rastreador com a ROI selecionada.
- Loop de Rastreamento: Entra em um loop para ler cada quadro do vídeo. Para cada quadro, atualiza o rastreador para calcular a nova posição da ROI. - Se o rastreamento for bem-sucedido, desenha um retângulo na posição da ROI, redimensiona a ROI e a salva como uma imagem. Caso contrário, exibe uma mensagem de falha.
- Exibição do Resultado: Exibe o quadro do vídeo com a ROI rastreada, o tipo de rastreador utilizado e a taxa de quadros por segundo (FPS). O loop de exibição pode ser interrompido pressionando a tecla 'Esc'.
- Liberação de Recursos: Após a conclusão do rastreamento, o vídeo é liberado e todas as janelas são fechadas.


Executando o Código

Certifique-se de ter um vídeo válido no caminho 'videos/video_10.mp4'.
Execute o script Python contendo o código fornecido.
Uma janela de visualização aparecerá exibindo o vídeo com o rastreamento da região de interesse selecionada.
Pressione a tecla 'Esc' para encerrar a exibição do vídeo e encerrar o programa.


Conclusão

O código fornece uma estrutura básica para rastreamento de objetos em um vídeo usando diferentes algoritmos disponíveis no OpenCV. Ele demonstra como inicializar o rastreador, acompanhar uma região de interesse ao longo do vídeo e exibir resultados visuais em tempo real. Certifique-se de ajustar as configurações e parâmetros conforme necessário para atender às suas necessidades específicas
