# End-to-end Cell Segmentation Using Yolo v8

## Workflows

1. Constants
2. Entity
3. Components
4. Pipelines
5. App.py


# How to run?

## STEP 01 - Clone the repository

```bash
https://github.com/ishumann/Cell-Segmentation

```
## STEP 02 - Create a conda environment after opening the repository

```bash
conda create -n cellseg python=3.8 -y
```

```bash
conda activate cell
```


## STEP 03 - Install the requirements
```bash
pip install -r requirements.txt
```

## STEP 04 - Run the following command

```bash
python app.py
```

## STEP 05  - FinalLY Open up you local host and port
```
localhost:8080
```

# AZURE CI/CD Deployment with Github Actions

## Save pass:
```
S6tXzK7IxUHz9O/9jkhciLsseddeQ++E+OcD7nQYy8+ACRDtEgUW
```

## Run from terminal:
```
docker build -t cellseg.azurecr.io/cell:latest
```
```
docker login cellseg.azurecr.io
```
```
docker push cellseg.azurecr.io/cell:latest
```

## Deployment Steps:
#### 1. Build the Docker image of the Source Code
#### 2. Push the Docker image to Container Registry
#### 3. Launch the Web App Server in Azure 
#### 4. Pull the Docker image from the container registry to Web App server and run 

