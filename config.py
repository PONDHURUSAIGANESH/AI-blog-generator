
OPENAI_API_KEY = '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'

class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
