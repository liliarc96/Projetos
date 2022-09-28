
# Document AI


### Formulário em chamadas sincronas usando Python
1. Habilitar o Document AI em: APIs & Services -> Library -> Cloud Document AI API;  <br>

2. Criar um processor tipo OCR em: Document AI -> Overview -> Explore Processors -> Form Parser;  <br>

3. Escolher um nome e uma região para o processor;  <br>

4. Após a criação salvar o ID do processor para uso futuro;  <br>

5. Clique em "Upload Test Document" e escolha uma formulário para teste;  <br>

6. Crie um bucket para armazenar os documentos a serem usados em: Vertex AI -> Workbench -> New Instance; <br>

7. Clique em Open JupyterLab, depois em Terminal e use ` gsutil cp gs://cloud-training/gsp925/documentai-async.ipynb . `; <br>

10. Abra o arquivo **documentai-async.ipynb** que foi baixado anteriormente;

11. Nas linhas seguintes insira: <br>
	`location = [REGIÃO DO PROCESSADOR]` <br>
	`file_path = [NOME DO DOCUMENTO]` <br>
	`processor_id = [ID DO PROCESSADOR]` <br>
	`gcs_input_bucket  = [NOME DO BUCKET SEM gs://]` <br>
    	`gcs_input_prefix  = [NOME DA PASTA NO BUCKET ONDE SE ENCONTRAM OS DOCUMENTOS]` <br>
    	`gcs_output_bucket = [NOME DO BUCKET SEM gs://]` <br>
    	`gcs_output_prefix = [NOME DA PASTA NO BUCKET ONDE AS DETECÇÕES SERÃO SALVAS]` <br>

12. Mude "mime_type": [TIPO DE DOCUMENTO]; <br>

12. Execute todas as células do notebook; <br>
_____

