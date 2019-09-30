# spider 🕷

> web

Author: [lilc4t](https://github.com/masterT)

http://localhost:12000/

## Setup

Requirements:
- docker

Start:

```shell
docker-compose up
```

## Writeup

### Flag 1

Inspect the source code of the page.

At the very bottom can find the flag in an HTML comment element.

```html  
  <!-- Secret flag #1: FLAG-52cc82dc0c9c25dffae4f0031a116ed9 -->
```

### Flag 2

Visit the `/robots.txt` page, you'll see `Disallow: /secret-work-in-progress.php`.

Visit `/secret-work-in-progress.php` and you'll have the flag `FLAG-f2c795019c88df52bf941c0475cfe070`.

### Flag 3

Open the developper console of your browser.

Select the _network_ tab and visit the page `/index.php`.

Inspect the HTTP headers of the request, you should see this custom HTTP header `X-Secret-Flag-2: FLAG-e37a8a540f7f4c3348b2f940759622db`.
