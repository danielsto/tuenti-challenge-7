import base64


image_decode = b'PNG'
image_encode = base64.b64encode(image_decode)
print(image_encode)
image_decode = base64.b64decode(image_encode)
print(image_decode)
image_result = open('../tuenti-challenge-2017/challenge-5/image_decode.png', 'wb')
image_result.write(image_decode)
