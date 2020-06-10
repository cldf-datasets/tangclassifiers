Added by Marc based on Mattis' comments, these are the steps to generate the data:

```shell script
python -m virtualenv .venv2
source .venv2/bin/activate
pip install cldfbench
cldfbench makecldf cldfbench_tangclassifiers.py
cldfbench readme cldfbench_tangclassifiers.py
```

the dataset created is in cldf/ 
To check the data:

```shell script
cldf validate cldf/StructureDataset-metadata.json
```
