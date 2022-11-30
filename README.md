# ai_model_integrations


## How to run 

python version : 3.8.13

steps:
```
1. python3 -m venv models_env
2. source activate models_env/bin/activate
3. pip install -r requirements.txt
```

How to run
``` 
uvicorn api.main:_get_app --factory  --port 8000 --host 0.0.0.0 --reload --limit-concurrency 100

```

where to access

```
http://localhost:8000/docs

```


## how to run streamlit

```
>> cd ui
>> streamlit run main.py
```