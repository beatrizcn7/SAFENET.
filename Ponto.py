import requests
import os
from urllib.parse import unquote

def extrair_url_imagem(url):
    try:
        url_decoded = unquote(url)

        start = url_decoded.find("https://lh5.googleusercontent.com/")
        if start == -1:
            print("URL da imagem não encontrada no link fornecido.")
            return None

        end = url_decoded.find("!", start)
        if end == -1:
            end = len(url_decoded)

        image_url = url_decoded[start:end]
        return image_url

    except Exception as e:
        print(f"Erro ao extrair a URL da imagem: {e}")
        return None

def baixar_imagem(url, output_folder, image_name):
    try:
        image_url = extrair_url_imagem(url)

        if not image_url:
            print("Não foi possível extrair a URL da imagem.")
            return

        print("URL da imagem:", image_url)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'image/jpeg',
        }
        response = requests.get(image_url, headers=headers, timeout=10)
        response.raise_for_status()

        if response.status_code == 200:
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            image_path = os.path.join(output_folder, f"{image_name}.jpg")
            with open(image_path, 'wb') as f:
                f.write(response.content)

            print(f"Imagem salva em: {image_path}")
        else:
            print(f"Erro ao baixar a imagem. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Erro durante a requisição HTTP: {e}")

url = ("https://www.google.com/maps/@38.9574803,-8.5231671,3a,75y,197.08h,89.51t/data=!3m8!1e1!3m6!1sAF1QipNwFK6a7kSQacDntcfpVS6x-3tUU9jXINMNilMY!2e10!3e11!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipNwFK6a7kSQacDntcfpVS6x-3tUU9jXINMNilMY%3Dw900-h600-k-no-pi0.4902909982945971-ya244.08392550366034-ro0-fo90!7i10240!8i5120?coh=205410&entry=ttu")

output_folder = "Fotos"
image_name = ("574_1")

baixar_imagem(url, output_folder, image_name)
