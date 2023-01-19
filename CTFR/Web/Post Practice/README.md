# Challenge Name: Post Practice

![Category: Website](https://img.shields.io/badge/Category-Website-lightgrey.svg)
![Point: 150](https://img.shields.io/badge/Score-150-brightgreen.svg)

## Description

Belum pernah ngirim Method POST ? Nah challenge ini baik untuk kalian belajar, Klik link dibawah untuk mencoba nyaa :D

## Attached Files

\-

## Solution

harus request method post dan parameternya flag=1.
disini saya menggunakan curl

```bash
curl -X POST --data "flag=1" -s https://web.ctf.rasyidmf.com/chal4/ | awk '/Flag :/{print $3}' | sed 's/<br>//g'
```

## Screen Shoot

\-
