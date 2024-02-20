import os
class Config:
    '''
    General configuration parent class
    '''
   # NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    #ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    #SECRET_KEY = os.environ.get('SECRET_KEY')
    #NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

 
 #   https://newsapi.org/v2/top-headlines?country=us&apiKey=93a3d4fc11694448b31c179828c974c4



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