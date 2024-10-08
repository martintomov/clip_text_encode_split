class RawText:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"raw_text": ("STRING", {"multiline": True})}}
    
    RETURN_TYPES = ("RAW_TEXT",)
    FUNCTION = "forward"
    CATEGORY = "utils"

    def forward(self, raw_text):
        return (raw_text, )
    
class RawTextCLIPEncode:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"raw_text": ("RAW_TEXT", ), 
                             "clip": ("CLIP", )
                    }}
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "encode"
    CATEGORY = "conditioning"

    def encode(self, clip, raw_text):
        return ([[clip.encode(raw_text), {}]], )
    
class RawTextCombine:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "raw_text_1": ("RAW_TEXT", ), 
                "raw_text_2": ("RAW_TEXT", )
            }
        }
    RETURN_TYPES = ("RAW_TEXT",)
    FUNCTION = "combine"
    CATEGORY = "utils"

    def combine(self, raw_text_1, raw_text_2):
        return (raw_text_1 + "," + raw_text_2, )
    
class StringEmptyCheck:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"string": ("STRING", {"multiline": True})}}
    
    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "check_empty"
    CATEGORY = "string_operations"

    def check_empty(self, string):
        return (len(string.strip()) == 0,)
    
class RawTextReplace:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "search": ("STRING", {}),
                "subject": ("RAW_TEXT", ), 
                "replace": ("RAW_TEXT", )
            }
        }
    RETURN_TYPES = ("RAW_TEXT",)
    FUNCTION = "replace"
    CATEGORY = "utils"

    def replace(self, search, subject, replace):
        return (subject.replace(search, replace), )
