from enum import Enum

class MessageType(Enum):
    info = 'info'
    warning = 'warning'
    error = 'error'
    danger = 'danger'

#label
MessageType.info.label = "xinxi"
MessageType.warning.label = "jinggao"
MessageType.error.label = "cuowu"
MessageType.danger.label = "weixian"


#promote
MessageType.info.color = "green"
MessageType.warning.label = "orange"
MessageType.error.label = "grey"
MessageType.danger.label = "red"

#屏蔽敏感词  -->add into myfilter
SensitiveWord = ["坏人","黄色"]