# Challenge Name: Wallpaper

![Category: Forensic](https://img.shields.io/badge/Category-Forensic-lightgrey.svg)
![Point: 10](https://img.shields.io/badge/Score-10-brightgreen.svg)

## Description

jadi gini nih, si budi lagi gabut trus dia mau ganti wallpaper laptop nya, saat dia mendownload gambar, ternyata ia malah mendownload file berformat zip. saat folder itu sudah di extract, folder itu berisi 3 file. Dapatkah kamu membantu Budi untuk melihat file zip tersebut?

## Attached Files

- [wallpaper.zip](files/wallpaper.zip)

## Solution

kita mendapatkan file zip, kita extract, flag ada di gambar maka lakukan command

```bash
strings isci-wallpaper.png | grep 'ISCI'
```

## Screen Shoot

## \-

[Back to home](/ISCI/)
