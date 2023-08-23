from flask import Flask, render_template, request
import pdfquery
from lxml import etree

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    customer_name = ""

    if request.method == 'POST':
        pdf = pdfquery.PDFQuery(request.files['pdf'])
        pdf.load()

        # Convert the PDF to XML
        xml_tree = pdf.tree
        xml_text = etree.tostring(xml_tree, pretty_print=True, encoding='unicode')

        # Access the data using coordinates
        coordinates = [68.0, 231.57, 101.990, 234.893]
        customer_name = pdf.tree.find('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % tuple(coordinates)).text

    return render_template('index.html', customer_name=customer_name)

if __name__ == '__main__':
    app.run(debug=True)
