# Challenge Name: Matrix

![Category: Forensic](https://img.shields.io/badge/Category-Forensic-lightgrey.svg)
![Point: 30](https://img.shields.io/badge/Score-30-brightgreen.svg)

## Description

Rijal sedang mencari wallpaper yang bagus untuk PC nya, dan dia memilih gambar matrix untuk menjadi wallpaper nya, namun size gambar nya sampai 220 KB, ia curiga mengapa size gambar nya begitu besar. Dapatkah kamu membantu Rijal untuk mencari tau apa yang menyebabkan size gambar tersebut sampai 220 KB?

## Attached Files

- [file.jpeg](files/file.jpeg)

## Solution

dengan besarnya file gambar, curiga dia memakai binwalk,
pada saat jalanin command, mendapatkan file text dan gambar, gambar adalah flagnya

```bash
 binwalk -e file.jpeg
```

## Screen Shoot

## \-

[Back to home](/ISCI/)
