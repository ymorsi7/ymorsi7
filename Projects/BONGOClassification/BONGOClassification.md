# CAPTCHA Classification: Solving BONGO Puzzles with Python

## Yusuf Morsi
### Feb 7, 2023

## 1
I wrote a function that would solve four different CAPTCHA (BONGO) generators. Tools that I used for this were OpenCV, NumPy, and Scikit-learn.



<hr>

## 2

After calculating the individual error rates, I calculated the overall error rate, which was 0.122. This shows that the classifier was able to correctly classify 87.8% of the test images, and that there is certainly room for improvement.

```
P(Error): 0.122000
```





<hr>

## 3
### For 5 test images that were misclassified by the NN classifier, I displayed both the test image, and training image closest to it. 

By looking at the test image and its corresponding nearest image, I can infer that the nearest neighbor classifier failed to perform because the number four in the former has plenty of similarities with the number nine in the latter. This is a very common mistake that not only NN classifiers, but also humans make.

![misclassified 1](images/nnmnist/1.png)

The classifier failed to perform here again because the number four in the former has plenty of similarities with the number nine in the latter. However, here it is apparent that the number nine in the latter image is a bit sloppy and even has a gap between its top two points.
![misclassified 2](images/nnmnist/2.png)

I reckon that in the former image here, the number six is so sloppy that the classifier had no clue what number it is. It just looked for an image with a similar location of pixels as the former, and found a '4' with such qualities.
![misclassified 3](images/nnmnist/3.png)

As seen before, our classifier has a hard time distinguishing between the number four and the number nine. Here, the number four in the latter image has a very small gap between its top two points, which caused our classifier to believe that it was a number nine.
![misclassified 4](images/nnmnist/4.png)

Unlike in our other cases, the numbers four and nine are written very clearly here. I would say that the classifier failed to perform here because the number nine in the latter image has a couple pixels on the right, similar to the number four in the former, leading it to believe that they were the same number. 
![misclassified 5](images/nnmnist/5.png)


<hr>

Note: the MATLAB code is private for Academic Integrity purposes.