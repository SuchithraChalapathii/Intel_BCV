import streamlit as st
import fitz  # PyMuPDF
import spacy
from difflib import Differ

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Business contract template
template = """This Business Contract ("Agreement") is entered into on this [Date], by and between [Party A], located at [Party A's Address], and [Party B], located at [Party B's Address]. The parties agree to the following terms and conditions for the mutual benefit of both parties:

Scope of Work: [Party A] agrees to provide [specific services or products] to [Party B] as outlined in [detailed description of services/products]. This work shall be completed within [time frame], starting from the date of this Agreement. [Party B] agrees to provide necessary support and information to [Party A] to facilitate the timely and effective completion of the work.

Compensation and Payment Terms: In exchange for the services/products provided by [Party A], [Party B] agrees to pay a total amount of [specified amount] in accordance with the payment schedule outlined in [payment schedule details]. Payments shall be made via [preferred payment method] and are due [terms of payment, e.g., upon receipt of invoice, net 30 days]. Late payments will incur a [late fee/interest rate].

Confidentiality and Termination: Both parties agree to maintain the confidentiality of any proprietary information shared during the course of this Agreement. This Agreement may be terminated by either party with [number of days] written notice if the other party breaches any material term of this Agreement. Upon termination, [Party A] shall be compensated for all work completed up to the termination date, and all materials provided by [Party B] shall be returned promptly."""

# Streamlit UI
st.title('Business Contract Validator')

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Extract text from PDF
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    
    st.text_area("Extracted Text", text, height=300)

    # Compare extracted text with template
    differ = Differ()
    diff = list(differ.compare(template.splitlines(), text.splitlines()))
    highlighted_diff = "\n".join(diff)
    
    st.text_area("Highlighted Differences", highlighted_diff, height=300)

    # Detect entities in the extracted text
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    st.subheader("Detected Entities")
    for entity in entities:
        st.write(f"{entity[0]} ({entity[1]})")

    # Show entities in the template
    template_doc = nlp(template)
    template_entities = [(ent.text, ent.label_) for ent in template_doc.ents]

    st.subheader("Template Entities")
    for entity in template_entities:
        st.write(f"{entity[0]} ({entity[1]})")
 