class BaseConfig:
    """ Base configulation """
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """Development Configulation"""
    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing Configulation"""
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production Configulation"""
    DEBUG = True
