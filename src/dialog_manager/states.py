# main states
actions_l = ['change language', 'activate', 'deactivate', 'increase', 'decrease', 'bring']
object_l = ['none', 'music', 'lights', 'volume', 'heat', 'lamp', 'newspaper', 'juice', 'socks',
            'Chinese', 'Korean', 'English', 'German', 'shoes']
location_l = ['none', 'kitchen', 'bedroom', 'washroom']

# Object States
music_states = ["on", "off"]
lights_states = ["on", "off"]
volume_states = list(map(lambda x: str(x), list(range(10))))
heat_states = ["hot", "warm", "cool", "cold"]
lamp_states = ["on", "off"]
newspaper_states = ["brought", "not brought"]
juice_states = ["brought", "not brought"]
socks_states = ["brought", "not brought"]
chinese_states = ["on", "off"]
korean_states = ["on", "off"]
english_states = ["on", "off"]
german_states = ["on", "off"]
shoes_states = ["brought", "not brought"]
allowed_states = {"music": music_states,
                  "lights": lights_states,
                  "volume": volume_states,
                  "heat": heat_states,
                  "lamp": lamp_states,
                  "newspaper": newspaper_states,
                  "juice": juice_states,
                  "socks": socks_states,
                  "chinese": chinese_states,
                  "korean": korean_states,
                  "english": english_states,
                  "german": german_states,
                  "shoes": shoes_states}

# allowed actions
allowed_actions = {"music": ["activate", "deactivate"],
                  "lights": ["activate", "deactivate"],
                  "volume": ["increase", "decrease"],
                  "heat": ["increase", "decrease"],
                  "lamp": ["activate", "deactivate"],
                  "newspaper": ["bring"],
                  "juice": ["bring"],
                  "socks": ["bring"],
                  "chinese": ["change language"],
                  "korean": ["change language"],
                  "english": ["change language"],
                  "german": ["change language"],
                  "shoes": ["bring"]}

# allowed rooms
allowed_rooms = {'music': ["none"],
                 'lights': ["none", "bedroom", "washroom", "kitchen"],
                 'volume': ["none"],
                 'heat': ["none", "bedroom", "washroom", "kitchen"],
                 'lamp': ["none"],
                 'newspaper': ["none"],
                 'juice': ["none"],
                 'socks': ["none"],
                 'chinese': ["none"],
                 'korean': ["none"],
                 'english': ["none"],
                 'german': ["none"],
                 'shoes': ["none"]}

# key table (foreign key + state)
# states = {"music": {"none": "off"},
#           "lights": {"none": "on", "bedroom": "on", "washroom":"on", "kitchen": "on"},
#           "volume": {"none":"3"},
#           "heat": {"none":"warm", "bedroom":"warm", "washroom":"warm", "kitchen": "warm"},
#           "lamp": {"none": "off"},
#           "newspaper": {"none": "not brought"},
#           "juice": {"none": "not brought"},
#           "socks": {"none": "not brought"},
#           "chinese": {"none": "off"},
#           "korean": {"none": "off"},
#           "english": {"none": "on"},
#           "german": {"none": "off"},
#           "shoes": {"none": "not brought"}}



