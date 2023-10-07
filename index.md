---
layout: default
title: 月面植物園
---
# 月面植物園
みかぶるのホームページ

> テクノなまこ、科学の力

SNS
- [bluesky](https://bsky.app/profile/mikanixonable.bsky.social)
- [misskey](https://misskey.io/@Mikanixonable)
- [twitter](https://twitter.com/Mikanixonable)

### テイラー展開
$$
f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n
$$

~~~python
from matplotlib import pyplot as plt
import cv2 as cv2
import numpy as np

img = cv2.imread("1.png")
img = cv2.resize(img,(64,64))

print(img)
r = img[:,:,2]
g = img[:,:,1]
b = img[:,:,0]

rgb = np.dstack((r, g, b))
rgb_flat = rgb.reshape((rgb.shape[0]*rgb.shape[1], 3))
def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)
cCodes = np.apply_along_axis(rgb_to_hex, 1, rgb_flat)

# print(cCodes)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.scatter(b, g, r, c=cCodes,alpha=1)
plt.show()
~~~

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```
\$\sqrt{2}\$
services
- [github](https://github.com/Mikanixonable)
- [blog](https://mikanixonable.hatenablog.com/)


連絡 mikanixonable1@gmail.com

探検
- [site map](1)
- [旧トップ](300)

## links


- [140](140)
- [141](141)
- [142](142)
- [notes](notes)

## external links
- [チートシート](https://github.com/pages-themes/leap-day/blob/master/index.md)
- [チートシート日本語](https://gist.github.com/mignonstyle/083c9e1651d7734f84c99b8cf49d57fa)


