# sre.cachedemo



### Setup in Local 
#### Install virtual env

``` 
python -m venv venv
```
#### Source the Env. 
``` 
source venv/bin/activate 
```

### Install pip modules

```
pip install python-dotenv requests flask Flask-Caching redis --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org
```
### Docker Compose Up 

```
docker compose up -d --build --remoove-orphans
```

### Docker Compose Down 

```
docker compose down --volumes
```
