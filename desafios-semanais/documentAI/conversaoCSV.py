  from google.cloud import documentai_v1beta3 as documentai
  from google.cloud import storage
  from prettytable import PrettyTable
  from os.path import splitext
  from typing import List, Sequence

  import pandas as pd
  
  project_id = %system gcloud config get-value core/project
  project_id = project_id[0]
  location = 'us'           
  file_path = 'form.pdf'    
  
  processor_id = 'PROCESSOR_ID' # TODO: Replace with a valid Processor ID
  
  def process_document(project_id=project_id, location=location, processor_id=processor_id, file_path=file_path):
      # Instantiates a client
      client = documentai.DocumentProcessorServiceClient()
      # The full resource name of the processor, e.g.:
      # projects/project-id/locations/location/processor/processor-id
      # You must create new processors in the Cloud Console first
      name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"
      with open(file_path, "rb") as image:
          image_content = image.read()
      # Read the file into memory
      document = {"content": image_content, "mime_type": "application/pdf"}
      # Configure the process request
      request = {"name": name, "document": document}
      # Use the Document AI client to process the sample form
      result = client.process_document(request=request)
      return result.document

    document=process_document()
    # print all detected text. 
    # All document processors will display the text content
    print("Document processing complete.")
    print("Text: {}".format(document.text))
    
    def get_table_data(
      rows: Sequence[documentai.Document.Page.Table.TableRow], text: str) -> List[List[str]]:
      """
      Get Text data from table rows
      """
      all_values: List[List[str]] = []
      for row in rows:
          current_row_values: List[str] = []
          for cell in row.cells:
              current_row_values.append(text_anchor_to_text(cell.layout.text_anchor, text))
      all_values.append(current_row_values)
      return all_values


def text_anchor_to_text(text_anchor: documentai.Document.TextAnchor, text: str) -> str:
    """
    Document AI identifies table data by their offsets in the entirity of the
    document's text. This function converts offsets to a string.
    """
    response = ""
    # If a text segment spans several lines, it will
    # be stored in different text segments.
    for segment in text_anchor.text_segments:
        start_index = int(segment.start_index)
        end_index = int(segment.end_index)
        response += text[start_index:end_index]
    return response.strip().replace("\n", " ")
  
header_row_values: List[List[str]] = []
body_row_values: List[List[str]] = []
  
for page in document.pages:
    for index, table in enumerate(page.tables):
        header_row_values = get_table_data(table.header_rows, document.text)
        body_row_values = get_table_data(table.body_rows, document.text)

        # Create a Pandas Dataframe to print the values in tabular format.
        df = pd.DataFrame(
            data=body_row_values,
            columns=pd.MultiIndex.from_arrays(header_row_values),
        )

        print(f"Page {page.page_number} - Table {index}")
        print(df)

        # Save each table as a csv file
        output_filename = f"{output_file_prefix}_pg{page.page_number}_tb{index}.csv"
        df.to_csv(output_filename, index=False)
