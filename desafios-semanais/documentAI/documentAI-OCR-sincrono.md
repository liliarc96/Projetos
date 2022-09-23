
# Document AI


### OCR por linha de comando e chamadas sincronas usando Python
1. Habilitar o Document AI em: APIs & Services -> Library -> Cloud Document AI API;  <br>

2. Criar um processor tipo OCR em: Document AI -> Overview -> Explore Processors -> Document OCR;  <br>

3. Escolher um nome e uma região para o processor;  <br>

4. Após a criação salvar o ID do processor para uso futuro;  <br>

5. Clique em "Upload Test Document" e escolha uma imagem para teste;  <br>

6. Crie um bucket para armazenar os documentos a serem usados em: Cloud Storage -> Buckets -> Create;

7. Crie uma VM que tenha acesso as APIs necessárias em: Compute Engine -> VM Instances;  <br>

8. Após a VM ser criada conecte com SSH e digite os comandos.  <br>
_____

#### Comandos:

~~~
export PROJECT_ID=$(gcloud config get-value core/project)

gcloud config set project $PROJECT_ID

export PROCESSOR_ID=[PROCESSOR ID]

export SA_NAME="document-ai-service-account"

gcloud iam service-accounts create $SA_NAME --display-name $SA_NAME

gcloud iam service-accounts keys create key.json \
--iam-account=$SA_NAME@${PROJECT_ID}.iam.gserviceaccount.com

export GOOGLE_APPLICATION_CREDENTIALS="$PWD/key.json"

gcloud auth application-default print-access-token

gsutil cp gs://[BUCKET]/[DOCUMENTO] .

echo '{"inlineDocument": {"mimeType": ["image/jpg" ou "application/pdf" ou "image/png"],"content": "' > temp.json
base64 [DOCUMENTO] >> temp.json
echo '"}}' >> temp.json
cat temp.json | tr -d \\n > request.json

export LOCATION="us"
curl -X POST \
-H "Authorization: Bearer "$(gcloud auth application-default print-access-token)" \
-H "Content-Type: application/json; charset=utf-8" \
-d @request.json \
https://${LOCATION}-documentai.googleapis.com/v1/projects/${PROJECT_ID}/locations/${LOCATION}/processors/${PROCESSOR_ID}:process > output.json

sudo apt install jq

cat output.json | jq -r ".document.text"

gsutil cp gs://cloud-training/gsp924/synchronous_doc_ai.py .

python3 -m pip install --upgrade google-cloud-documentai google-cloud-storage

import argparse
from google.cloud import documentai
from google.cloud import storage

parser = argparse.ArgumentParser()
parser.add_argument("-P", "--project_id", help="Google Cloud Project ID")
parser.add_argument("-D", "--processor_id", help="Document AI Processor ID")
parser.add_argument("-F", "--file_name", help="Input file name", default="file.[EXTENSÃO DO ARQUIVO]")
parser.add_argument("-L", "--location", help="Processor Location", default="us")
args = parser.parse_args()

def process_document(project_id, location, processor_id, file_path ):
    # Instantiates a client
    client = documentai.DocumentProcessorServiceClient()
	
    # The full resource name of the processor, e.g.:
    # projects/project-id/locations/location/processor/processor-id
	
    # You must create new processors in the Cloud Console first
    name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"
	
    # Read the file into memory
    with open(file_path, "rb") as image:
        image_content = image.read()
		
    # Create the document object 
    document = {"content": image_content, "mime_type": ["image/jpg" ou "image/png" ou "application/pdf"]}
	
    # Configure the process request
    request = {"name": name, "document": document}
	
    # Use the Document AI client synchronous endpoint to process the request
    result = client.process_document(request=request)
    return result.document
	
	print("Document processing complete.")
	print("Text: {}".format(document.document_text))
			
export PROJECT_ID=$(gcloud config get-value core/project)
export GOOGLE_APPLICATION_CREDENTIALS="$PWD/key.json"

python3 synchronous_doc_ai.py \
--project_id=$PROJECT_ID \
--processor_id=$PROCESSOR_ID \
--location=us \
--file_name=[NOME DO ARQUIVO] | tee results.txt
~~~
