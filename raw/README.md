Added by Marc based on Mattis' comments, these are the steps to generate the data:

- python -m virtualenv .venv2
- source .venv2/bin/activate
- pip install cldfbench
- python convert.py

the dataset created is in cldf/ 
To check the data:

- cldf validate cldf/StructureDataset-metadata.json
