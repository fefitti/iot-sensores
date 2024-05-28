Detecção de Áreas com Desmatamento usando YOLO
Este projeto tem como objetivo detectar áreas com desmatamento em imagens de satélite utilizando o modelo YOLO (You Only Look Once) para detecção de objetos.

Visão Geral
A detecção de áreas com desmatamento é de extrema importância para monitorar e combater a devastação das florestas, fornecendo informações valiosas para a conservação ambiental e o manejo sustentável dos recursos naturais. Este projeto utiliza técnicas de visão computacional e aprendizado profundo para identificar áreas onde houve supressão de vegetação em imagens de alta resolução.

Funcionamento
O código-fonte fornecido utiliza o modelo YOLOv3 para detectar objetos em imagens digitais, sendo customizado para detectar apenas árvores. A ausência de detecções de árvores com alta confiança em uma determinada região é interpretada como uma área com desmatamento. O processo de detecção é realizado de forma automatizada em lotes de imagens, possibilitando o monitoramento contínuo de extensas áreas florestais.

Pré-requisitos
Python 3.x
Biblioteca ImageAI
Modelo YOLOv3 pré-treinado
Como Usar
Instale as dependências necessárias:
Copiar código
pip install imageai
Baixe o modelo YOLOv3 pré-treinado.

Organize suas imagens de satélite na pasta input/.

Execute o script de detecção de desmatamento:

Copiar código
python detecao_desmatamento.py
Os resultados serão salvos na pasta output/, onde as imagens com áreas detectadas como desmatadas serão destacadas.
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar pull requests com melhorias ou novos recursos.
