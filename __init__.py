# __init__.py

from .clip_text_encode_split import (
    RawText,
    RawTextCLIPEncode,
    StringEmptyCheck,
    RawTextCombine,
    RawTextReplace
)

NODE_CLASS_MAPPINGS = {
    "RawText": RawText,
    "RawTextEncode": RawTextCLIPEncode,
    "StringEmptyCheck": StringEmptyCheck,
    "RawTextCombine": RawTextCombine,
    "RawTextReplace": RawTextReplace
}
