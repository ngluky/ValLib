from .constant import Constant
from .structs import classproperty

class Version:
    @classproperty
    def valorant(cls):
        return Constant.valorantVersion

    @classproperty
    def riot(cls):
        return Constant.riotVersion

    @classproperty
    def sdk(cls):
        return Constant.sdkVersion
