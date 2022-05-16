import os

class Config:
    pass

class DevConfig:
     DEBUG = True

class ProdConfig:
    pass
   
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}      