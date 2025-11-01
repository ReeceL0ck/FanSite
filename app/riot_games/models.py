from enum import Enum
from pydantic import BaseModel

class puuids(str, Enum):
    MEOWCEL = "Cpc68Dk-zFO7ebvtvpBdIz0p8rGs7F7UoqCUN3PKSGEtHTrusF1cS0IYISoETNXnpzjIkTgRhWCB7Q"
    SAVAGE_JOHN = "-L4GcmsDvFiPkH_-oVws79CUIhnKmStXFQUXqv8ANPRoOJggqv1gy02RDfmG4UM8ZrCRCkbJa5y0yA"
    ATTENTION_U_PIGS = "wgtOb6NLS-ZyLslTQFAn4i4TCRBC5blPXUT2Ht3EBNybU16iCiqxUkVGQ2dykoXMXD5bn7fjLnbRtw"
    LARRY_LONGSTRIDE = "DRrRrL0KS6FWmOdk_y7nrtCw4YZPPDmUE-vbDko3iwSDtwzRK2o3Uyl47XUsAXexwk7kpQEMvrxLTw"
    KID_BALLS_PRO = "fhk26bSU8BOweq2aN_9JonYaNmSbKZCylpIc2wFg3eWhRj_pF6UuWTKIiS9WmZvBf6BBwrb1KcfVRA"


class playerModel(BaseModel):
    queueType : str
    rank : str
    win_rate : float
    leaguePoints : int
