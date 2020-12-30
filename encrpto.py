import base64 as encoder_and_decoder

def decode(key, enc): 
    dec = [] 
      
    enc = encoder_and_decoder.urlsafe_b64decode(enc).decode() 
    for i in range(len(enc)): 
        key_c = key[i % len(key)] 
        dec_c = chr((256 + ord(enc[i]) -
                           ord(key_c)) % 256) 
                             
        dec.append(dec_c) 
    return "".join(dec) 

decode('Important', '')
