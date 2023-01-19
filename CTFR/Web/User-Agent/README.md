# Challenge Name: User-Agent

![Category: Website](https://img.shields.io/badge/Category-Website-lightgrey.svg)
![Point: 300](https://img.shields.io/badge/Score-300-brightgreen.svg)

## Description

Belum pernah ng3dit User-Agent ? Nah coba edit dulu nih Us3r-4G3nt nya pada halaman dibawah ini untuk mendapatkan flag yaahh!

## Attached Files

\-

## Solution

disini kita harus mengedit user-agentnya, disini saya menggunakan curl

```bash
 curl --header -s "User-Agent: CTFR" https://web.ctf.rasyidmf.com/chal5/ | awk '/Flag : /{print $3}'
```

## Screen Shoot

\-
