# Intel_BCV
 Business Contract Validation Project

Overview
This project validates business contracts by classifying content within clauses and identifying deviations from standard templates. It ensures consistency and compliance by extracting, classifying, comparing, and highlighting differences in contract clauses.

 Features
Template and Contract Collection: Gather standard templates and existing contracts.
Clause Extraction and Segmentation: Extract and segment text into individual clauses.
Clause Classification: Categorize clauses (e.g., payment terms, confidentiality).
Template Comparison: Compare clauses with template clauses and highlight deviations.
Automation and Tools: Utilize contract management software and machine learning for automation.
Documentation and Reporting: Record findings and generate summary reports.

Code Overview
```python
import streamlit as st
import fitz  # PyMuPDF
from difflib import Differ
import spacy

nlp = spacy.load("en_core_web_sm")

template = """..."""

st.title('Business Contract Validator')
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = "".join([page.get_text() for page in doc])
    st.text_area("Extracted Text", text, height=300)

    differ = Differ()
    diff = list(differ.compare(template.splitlines(), text.splitlines()))
    highlighted_diff = "\n".join(diff)
    st.text_area("Highlighted Differences", highlighted_diff, height=300)

    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    st.subheader("Detected Entities")
    for entity in entities:
        st.write(f"{entity[0]} ({entity[1]})")

    template_doc = nlp(template)
    template_entities = [(ent.text, ent.label_) for ent in template_doc.ents]
    st.subheader("Template Entities")
    for entity in template_entities:
        st.write(f"{entity[0]} ({entity[1]})")
```



Conclusion
Participating in this project has been a valuable experience. We successfully completed the project, applying both logical and imaginative approaches to solve problems. We express our gratitude to our teachers and the Intel Unnati Training team for their support and guidance.
