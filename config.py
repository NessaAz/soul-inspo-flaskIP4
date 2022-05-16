class Config:
    pass

class DevConfig:
    pass

class ProdConfig:
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}      