Added by Marc based on Mattis' comments, these are the steps to generate the data:

```shell script
python -m virtualenv .venv2
source .venv2/bin/activate
pip install cldfbench
cd Desktop/GitHub/tangclassifiers/
pip install pyglottolog
cldfbench makecldf cldfbench_tangclassifiers.py --glottolog ~/Desktop/GitHub/glottolog/
cldfbench readme cldfbench_tangclassifiers.py
```

the dataset created is in cldf/ 
To check the data:

```shell script
cldf validate cldf/StructureDataset-metadata.json
```

https://github.com/cldf/cookbook

to read cldf datasets in R
https://github.com/SimonGreenhill/rcldf 

to test with CLLD locally
http://127.0.0.1:6543/
