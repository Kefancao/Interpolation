# Interpolation

This repo is meant to demonstrate the cubic spline interpolation method. Check out the example.py file, it has a function that is able to generate conditional cubic functions which interpolates data points which will resemble the original very closely!

For more information on cubic splines, I recommend checking out this [wikipedia](https://en.wikipedia.org/wiki/Spline_(mathematics)) article. 

# Parametric Interpolation
Since a x versus y version of interpolation is possible. We must also be able to interpolate an arbitrary line segment with parametric interpolation. This is exactly what the parametricInterpolation.py file does! There is an example in that file which basically does the following. 

For a given image of my nickname

<img width="588" alt="Screen Shot 2022-04-06 at 10 09 43 PM" src="https://user-images.githubusercontent.com/76069770/162106334-1d4c1b56-ddbc-45ce-ac20-6f7231460f21.png">

Taking small samples of those points and storing them in a list. Then feeding that into the parametric spline function, we can get somehting similar to

<img width="613" alt="Screen Shot 2022-04-06 at 10 12 28 PM" src="https://user-images.githubusercontent.com/76069770/162106627-771bbb02-ec94-4051-a4e0-4f4ce0c64f56.png">

Which as you can see, very closely resembles the original image!!!
