import requests

from .exceptions import InvalidRequest

from .agent import Agent
from .role import Role
from .weapon import Weapon

class Client:
    def __init__(self) -> None:
        self.session = requests.session()
        self.base_url = "https://valorant-api.com/v1/"

    def get_(self , url: str , json_: bool = False):
        if not url.lower().startswith(self.base_url):
            raise InvalidRequest("This client can only fetch https://valorant-api.com/")
        
        else:
            r = self.session.get(url, timeout=15)
            if not json_:
                return r
            else:
                return r.json()

    def agent(self, name: str = None, uuid: str = None, isPlayableCharacter: bool = True):
        if name is not None:
            to_fetch = ['displayName',name.capitalize()]
        elif uuid is not None:
            to_fetch = ['uuid', uuid]
        else:
            raise InvalidRequest("Neither name nor uuid was provided.")

        r = self.get_(self.base_url+'agents?isPlayableCharacter='+str(isPlayableCharacter).lower(), json_=True)
        data = r['data']

        for i in data:
            if i[to_fetch[0]] == to_fetch[1]:
                a = Agent(i)
                break
            else:
                continue
        
        return a

    def role(self, name: str = None, uuid: str = None):
        if name is not None:
            to_fetch = ['displayName' , name.capitalize()]
        elif uuid is not None:
            to_fetch = ['uuid' , uuid]

        else:
            raise InvalidRequest("Neither name nor uuid was not provided.")

        roles_ = [
            {'uuid': '1b47567f-8f7b-444b-aae3-b0c634622d10', 'displayName': 'Initiator', 'description': 'Initiators challenge angles by setting up their team to enter contested ground and push defenders away.', 'displayIcon': 'https://media.valorant-api.com/agents/roles/1b47567f-8f7b-444b-aae3-b0c634622d10/displayicon.png', 'assetPath': 'ShooterGame/Content/Characters/_Core/Roles/Breaker_PrimaryDataAsset'},
            {'uuid': 'dbe8757e-9e92-4ed4-b39f-9dfc589691d4', 'displayName': 'Duelist', 'description': 'Duelists are self-sufficient fraggers who their team expects, through abilities and skills, to get high frags and seek out engagements first.', 'displayIcon': 'https://media.valorant-api.com/agents/roles/dbe8757e-9e92-4ed4-b39f-9dfc589691d4/displayicon.png', 'assetPath': 'ShooterGame/Content/Characters/_Core/Roles/Assault_PrimaryDataAsset'},
            {'uuid': '5fc02f99-4091-4486-a531-98459a3e95e9', 'displayName': 'Sentinel', 'description': 'Sentinels are defensive experts who can lock down areas and watch flanks, both on attacker and defender rounds.', 'displayIcon': 'https://media.valorant-api.com/agents/roles/5fc02f99-4091-4486-a531-98459a3e95e9/displayicon.png', 'assetPath': 'ShooterGame/Content/Characters/_Core/Roles/Sentinel_PrimaryDataAsset'},
            {'uuid': '4ee40330-ecdd-4f2f-98a8-eb1243428373', 'displayName': 'Controller', 'description': 'Controllers are experts in slicing up dangerous territory to set their team up for success.', 'displayIcon': 'https://media.valorant-api.com/agents/roles/4ee40330-ecdd-4f2f-98a8-eb1243428373/displayicon.png', 'assetPath': 'ShooterGame/Content/Characters/_Core/Roles/Strategist_PrimaryDataAsset'}
        ]

        for i in roles_:
            if i[to_fetch[0]] == to_fetch[1]:
                r = Role(i)
                break
            else:
                continue

        return r

    def weapon(self, name: str = None, uuid: str = None):
        if name is not None:
            to_fetch = ['displayName', name.capitalize()]
        elif uuid is not None:
            to_fetch = ['uuid' , uuid]
        else:
            raise InvalidRequest("Neither name nor uuid was not provided.")

        r = self.get_(self.base_url+'weapons', json_=True)
        data = r['data']

        for i in data:
            if i[to_fetch[0]] == to_fetch[1]:
                w = Weapon(i)
                break
            else:
                continue

        return w