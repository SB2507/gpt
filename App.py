import streamlit as st
import pdfquery
from lxml import etree

def main():
    st.title("PDF Data Extractor")

    # File upload widget
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        pdf = pdfquery.PDFQuery(uploaded_file)
        pdf.load()

        # Convert the PDF to XML
        xml_tree = pdf.tree
        xml_text = etree.tostring(xml_tree, pretty_print=True, encoding='unicode')

        st.subheader("XML Representation of PDF:")
        st.code(xml_text, language='xml')

        st.subheader("Extracted Data from PDF:")

        # Extract all LTTextLineHorizontal elements
        text_elements = pdf.tree.findall('.//LTTextLineHorizontal')

        extracted_data = []

        for element in text_elements:
            text = element.text.strip() if element.text else ""
            extracted_data.append(text)

        # Display extracted data
        for idx, data in enumerate(extracted_data):
            st.write(f"Line {idx + 1}: {data}")

if __name__ == "__main__":
    main()
