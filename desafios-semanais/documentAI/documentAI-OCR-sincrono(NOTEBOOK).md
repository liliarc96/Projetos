
# Document AI


### Formulário em chamadas sincronas usando Python
1. Habilitar o Document AI em: APIs & Services -> Library -> Cloud Document AI API;  <br>

2. Criar um processor tipo OCR em: Document AI -> Overview -> Explore Processors -> Form Parser;  <br>

3. Escolher um nome e uma região para o processor;  <br>

4. Após a criação salvar o ID do processor para uso futuro;  <br>

5. Clique em "Upload Test Document" e escolha uma formulário para teste;  <br>

6. Crie um bucket para armazenar os documentos a serem usados em: Vertex AI -> Workbench -> New Instance; <br>

7. Clique em Open JupyterLab, depois em Terminal e use ` gsutil cp gs://cloud-training/gsp925/documentai-sync.ipynb . `; <br>

8. Ainda no terminal digite o comando `gsutil cp gs://[ENDEREÇO DO BUCKET CRIADO ANTERIORMENTO]`; <br>

10. Abra o arquivo **documentai-sync.ipynb** que foi baixado anteriormente;

11. Nas linhas com comentários com **Replace** insira: <br>
	`location = [REGIÃO DO PROCESSADOR]` <br>
	`file_path = [NOME DO DOCUMENTO]` <br>
	`processor_id = [ID DO PROCESSADOR]` <br>

12. Mude "mime_type": [TIPO DE DOCUMENTO]; <br>

12. Execute todas as células do notebook; <br>
_____

