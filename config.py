import os
import psycopg2



class Config:
    '''
    General configuration parent class
    '''
    SPOON_API_BASE_URL ='https://api.spoonacular.com/recipes/:id/information?includeNutrition=false'
    #ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SPOON_API_KEY = os.environ.get('SPOON_API_KEY')
    DB_USERNAME = os.environ.get('username')
    DB_PASSWORD = os.environ.get('password')



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'development' :DevConfig,
    'production' :ProdConfig
}

# Connecting to my postgres DB
conn = psycopg2.connect(dbname =Config.DB_USERNAME , user=Config.DB_PASSWORD)
  
# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
#cur.execute("SELECT * FROM my_data")

# Retrieve query results
#records = cur.fetchall()