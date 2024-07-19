# Mathematical Curves Visualizer with GLUT in C/C++

### 🎥 Showcase
Check out this [YouTube video](https://www.youtube.com/watch?v=Hz8D1atjipE&list=PL-j3UE1st04BZqRXq6eUBHpovhKjA1kiX&index=2&ab_channel=dragosel505) to see the project in action!


## Conchoid of Nicomedes

```
f(x) = |sin(x)| * e^(-sin(x)), for x in [0, 8*pi]
f(x) = 1, if x = 0
f(x) = d(x)/x, if 0 < x <= 100
d(x) = the distance from x to the nearest integer.
```

## Trisectrix of Longchamps

```
x = a / (4 * cos^2(t) - 3 )
y = a * tan(t) / (4 * cos^2(t) - 3 )
t in [-pi/2, pi/2] \ { +- pi/6 }
```

## Cycloid

```
x = a * t - b * sin(t)
y = a - b * cos(t)
for any t in R
```

## Lemniscate of Bernoulli

```
(r, t) - polar coordinates
where t in [a, b]
where r = f(t)

polar coordinates to cartesian:
x = r * cos(t)
y = r * sin(t)

f(t) = +-a * sqrt(2 * cos(2t))
where t in [-pi/4, pi/4]
```

## Logarithmic Spiral

```
(r, t) - polar coordinates
where t in [a, b]
where r = f(t)

polar coordinates to cartesian:
x = r * cos(t)
y = r * sin(t)

f(t) = a * e^(1+t)
where t in [0, infinty]
```

****
