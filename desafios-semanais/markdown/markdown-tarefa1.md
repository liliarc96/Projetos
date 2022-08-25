# Desafio: Google Cloud Storage

### No ambiente gráfico
1. Criação de dois buckets chamados *lilia_bucket1* e *lilia_bucket2* na região **us_central1** com classe *standard*;

2. Adicionar um arquivo tipo .jpg no bucket1 e um .txt no bucket2;

3. Criar um lilia_bucket3 e copiar os arquivos dos outros 2 buckets para o bucket3;

4. Conferir se os arquivos foram copiados;

5. Baixar os arquivos no computador;

6. Deletar os buckets;

7. Listar buckets para ver se foram excluídos.

_____

### Na linha de comando
1. Criação de dois buckets chamados lilia_bucket1 e lilia_bucket2 na região us_central1 com classe standard;

2. Adicionar um arquivo tipo .jpg no bucket1 e um .txt no bucket2;

3. Criar um lilia_bucket3 e copiar os arquivos dos outros 2 buckets para o bucket3;

4. Conferir se os arquivos foram copiados;

5. Baixar os arquivos no computador;

6. Deletar os buckets;

7. Listar buckets para ver se foram excluídos.


#### Comandos:

> `gsutil mb -l us-central1 gs://lilia_bucket1`
> `gsutil mb -l us-central1 gs://lilia_bucket2`
> 
> `gsutil cp C:/Users/lilia.cantalice_mult/Pictures/kitten.jpg gs://lilia_bucket1`
> `gsutil cp C:/Users/lilia.cantalice_mult/Pictures/metadados.txt gs://lilia_bucket2`
> 
> `gsutil mb -l us-central1 gs://lilia_bucket3`
> 
> `gsutil cp -p gs://lilia_bucket1/kitten.jpg gs://"lilia_bucket3/Copy of kitten.jpg"`
> `gsutil cp -p gs://lilia_bucket2/metadados.txt gs://"lilia_bucket3/Copy of Metadados.txt"`
> 
> `gsutil -m cp -r gs://lilia_bucket3 C:/Users/lilia.cantalice_mult/Pictures/`
> 
> `gsutil rm -r gs://lilia_bucket1/`
> `gsutil rm -r gs://lilia_bucket2/`
> `gsutil rm -r gs://lilia_bucket3/`
> 
> `gsutil ls`
