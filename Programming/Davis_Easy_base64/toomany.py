import base64
normal_string = "YCEP{bu773RF1N93RZ}"
encoded = base64.b64encode(bytes(normal_string, 'utf-8')).decode("utf-8") 
for i in range(0,31):
        encoded = base64.b64encode(bytes(encoded,'utf-8')).decode("utf-8") 
        print(i)
with open('encoded.txt', 'w') as f:
    f.write(encoded)
    
decoded = base64.b64decode(bytes(encoded, 'utf-8')).decode("utf-8")     
for i in range(0,31):
    decoded = base64.b64decode(bytes(decoded,'utf-8')).decode("utf-8") 
    print(i)
print(decoded)