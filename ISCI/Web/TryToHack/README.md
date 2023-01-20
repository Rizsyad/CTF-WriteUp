# Challenge Name: TryToHack

![Category: Website](https://img.shields.io/badge/Category-Website-lightgrey.svg)
![Point: 50](https://img.shields.io/badge/Score-50-brightgreen.svg)

## Description

baca teks di file!

## Attached Files

\-

## Solution

website ini ada banyak ringtangan, maka dari itu saya buat automasi dari python

```python
import requests
import base64
import re

def init():
    r = requests
    return Request(r), r

class Request:
    def __init__(self, r: requests):
        self.r = r

    def redirect(self, url, langkah):
        r = self.r

        response = r.get(url).text

        if langkah == 1:
            return self.getFlag(self.langkahPertama(response))
        elif langkah == 2:
            return self.langkahKedua(response)
        elif langkah == 3:
            return self.langkahKeTiga(response)
        else:
            return response

    def decodeDecimal(self, encode):
        listEncode = encode.split(' ')
        dec = ''

        for enc in listEncode:
            dec += chr(int(enc))

        return dec

    def decodeBase64(self, encode):
        return base64.b64decode(encode).decode('ascii')

    def decode_binary_string(self, s):
        binary_int = int(s, 2);

        # Getting the byte number
        byte_number = binary_int.bit_length() + 7 // 8

        # Getting an array of bytes
        binary_array = binary_int.to_bytes(byte_number, "big")

        # Converting the array into ASCII text
        ascii_text = binary_array.decode()

        return ascii_text

    def rot13(self, s):
        rot13 = str.maketrans('ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
        return s.translate(rot13)

    def langkahPertama(self, response):
        regex = r"<!-- (.*) --> "

        matchBase64 = re.findall(regex, response)
        return self.decodeDecimal(self.decodeBase64(matchBase64[0]))

    def langkahKedua(self, response):
        regexHitung = r"<!-- \((.*)\) -->"
        regexDecimal = r"<p>(.*)</p>"

        matchHitung = re.findall(regexHitung, response)
        perhitungan = matchHitung[0].replace(' = ...', '').split('-')
        perhitungan[0] = int(perhitungan[0])
        perhitungan[1] = int(perhitungan[1])
        hasil = f'0{eval("perhitungan[0] - perhitungan[1]")}'

        matchDecimal = re.findall(regexDecimal, response)[0].replace('...', hasil)

        return self.decodeDecimal(matchDecimal)

    def langkahKeTiga(self, response):
        regex = r"<p>(.*)\n(.*)\n(.*)\n(.*)\n(.*)</p>"
        gabungBinary = ''
        matchBinary = re.findall(regex, response)

        for match in matchBinary[0]:
            gabungBinary += match.strip().replace(' ', '')

        getBinary = self.decode_binary_string(gabungBinary).replace('\nrot13 dan base64 mungkin membantumu', '')
        # print(getBinary)
        return self.decodeBase64(self.rot13(getBinary))

    def getFlag(self, response):
        r = self.r

        regexFlag = r"<p>nih flag nyaa : (.*)</p>"

        langkahKedua = self.redirect(f"https://lighthearted-taffy-e5801e.netlify.app/{response}", 2)
        langkahKetiga = self.redirect(f"https://lighthearted-taffy-e5801e.netlify.app/{langkahKedua}", 3)
        langkahKeempat = self.redirect(f"https://lighthearted-taffy-e5801e.netlify.app/{langkahKetiga}", 4)
        matchFlag = re.findall(regexFlag, langkahKeempat)[0]

        print(matchFlag)

    def exploit(self):
        r = self.r
        self.redirect("https://lighthearted-taffy-e5801e.netlify.app/", 1)

if __name__ == "__main__":
    x, y = init()
    x.exploit()
```

## Screen Shoot

\-

---

[Back to home](/ISCI/)
