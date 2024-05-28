from imageai.Detection import ObjectDetection
import os

# Definindo os diretórios de entrada e saída
input_path = "input/"
output_path = "output/"
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Carregando o modelo YOLO pré-treinado
detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(
    "path_to_your_pretrained_model", "yolo.h5"))
detector.loadModel()

# Definindo as classes que serão detectadas (nesse caso, apenas "tree" para árvores)
detector.detectObjectsCustom = ["tree"]

# Detectando objetos em cada imagem na pasta de entrada e salvando as saídas
for image in os.listdir(input_path):
    image_path = os.path.join(input_path, image)
    detections = detector.detectObjectsFromImage(
        input_image=image_path, output_image_path=os.path.join(output_path, "detected_" + image))
    
    # Verificando se árvores foram detectadas
    trees_detected = False
    for detection in detections:
        if detection["name"] == "tree" and detection["percentage_probability"] > 50:
            trees_detected = True
            break
    
    # Se não houver detecção de árvores, considera-se uma área com desmatamento
    if not trees_detected:
        print("Área com desmatamento detectada na imagem", image)
    else:
        print("Não há áreas com desmatamento na imagem", image)
