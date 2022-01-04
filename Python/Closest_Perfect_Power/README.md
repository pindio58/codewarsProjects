[Perfect powers](https://en.wikipedia.org/wiki/Perfect_power) are numbers that can be written mkm^kmk, where mmm and kkk are both integers greater than 1.


Your task is to write a function that returns the perfect power nearest any number.


#### Notes


* When the input itself is a perfect power, return this number
* Since 4 is the smallest perfect power, for inputs < 4 (including 0, 1, and negatives) return 4
* The input can be either a floating-point number or an integer
* If there are two perfect powers equidistant from the input, return the smaller one


Examples
--------


For instance,



```Python
 0  -->   4
11  -->   9    # 9 = 3^2
34  -->  32    # 32 = 2^5 and 36 = 6^2 --> same distance, pick the smaller

```

