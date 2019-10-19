from .OneHot import OneHotEncoder
from .Recessive import RecessiveEncoder

def get_encoder(encoding_method):
    if (encoding_method == 'recessive'):
        return RecessiveEncoder

    if (encoding_method == 'one-hot'):
        return OneHotEncoder

    raise Exception('Invalid encoding method')