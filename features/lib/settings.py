import os

app_env = os.environ.get('APP_ENV')

if app_env == None:
  app_env = "dev"
else:
  app_env = app_env.strip()

if app_env == "dev":
  products_url = "http://localhost:8000/"
elif app_env == "prod":
  products_url = "http://zhangyuan.github.io/databases/"
else:
  raise Exception("Invalid APP_ENV:", app_env)
