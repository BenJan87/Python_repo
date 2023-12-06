import fitz  # PyMuPDF

def crop_pdf(input_pdf, output_pdf, start_page, end_page):
    try:
        # Open the PDF file
        pdf_document = fitz.open(input_pdf)
        
        # Create a new PDF document to store the cropped pages
        cropped_pdf = fitz.open()

        # Iterate through the specified range of pages
        for page_num in range(start_page - 1, min(end_page, pdf_document.page_count)):
            # Get the page
            page = pdf_document[page_num]

            # Add the page to the new PDF document
            cropped_pdf.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)

        # Save the cropped PDF to the output file
        cropped_pdf.save(output_pdf)

        print(f"Pages {start_page} to {end_page} successfully cropped and saved to {output_pdf}")

    except Exception as e:
        print(f"Error: {str(e)}")

    finally:
        # Close the PDF documents
        if pdf_document:
            pdf_document.close()
        if cropped_pdf:
            cropped_pdf.close()
# Specify the input and output file paths, and the range of pages to crop
input_pdf_path = r'C:\Users\Benek\Desktop\Studia_AGH\CV_tmp.pdf'
output_pdf_path = r'C:\Users\Benek\Desktop\Studia_AGH\CV_Beniamin_Jankowski.pdf'
start_page_number = 1
end_page_number = 1

# Call the function to crop the specified pages
crop_pdf(input_pdf_path, output_pdf_path, start_page_number, end_page_number)
