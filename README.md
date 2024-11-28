# clip_text_encode_split  

## what's the idea?  
this node handles raw text, lets you manipulate it (combine, replace parts, etc.), and encodes it using a clip model. useful for workflows needing text processing before generating conditioning vectors.  

---

## what does each class do?  

### **`RawText`**  
- takes raw text and wraps it for use in the workflow.  

### **`RawTextCLIPEncode`**  
- encodes the raw text using a clip model, returning a conditioning vector.  

### **`RawTextCombine`**  
- combines two raw text inputs with a comma separator.  

### **`StringEmptyCheck`**  
- checks if a string is empty or just whitespace.  

### **`RawTextReplace`**  
- replaces part of the text (`search`) with another text (`replace`) in the input.  
