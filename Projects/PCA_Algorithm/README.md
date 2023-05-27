# PCA Algorithm for Image Classification

## Yusuf Morsi
### Mar 17, 2023

## Introduction

Here, we are implementing PCA to reduce dimensionality, visualize principal components, determine optimal subspace dimension based on eigenvalues, calculate error rates, and identify the least 5-like image using orthogonal energy analysis, demonstrating improved classification performance.

## 1
In this project, we aim to implement the PCA algorithm for dimensionality reduction in our image dataset. We will visualize the top 10 principal components as 28 × 28 images, focusing on both the entire dataset and specifically on the 'digit5' class. To gain insights into the significance of features, we will plot the eigenvalues in descending order.

Below are plots of the top ten prinicpal components as 28x28 images.

![PCs](images/p11.png)

Below we repeat the same thing for the class for the digit 5. 

![PCs](images/p12.png)

Below is a plot of the eigenvalues of the entire dataset (in decreasing order).

![Eigenvalues](images/p13.png)

## 2

Moving on, we will explore classification using the PCA subspace. Analyzing the eigenvalue plot, we will determine the optimal subspace dimension for accurate classification. We will calculate error rates using different subspace dimensions (ranging from 5 to 350) and present the results in a plot, showcasing the impact of dimensionality reduction on classification accuracy. 

Below we see the total error rate using subspaces of following dimensions: [5, 10, 20, 30, 40, 60, 90, 130, 180, 250, 350].

![Error Rates](images/p2.png)

## 3

Lastly, we will focus on identifying the image in our imageTest dataset that is least similar to a digit 5. By utilizing the principal components specific to the 'digit5' class, we will identify the image with the highest energy orthogonal to the subspace spanned by the top 40 eigenvectors. This analysis will allow us to detect images that deviate significantly from the characteristics of a digit 5, demonstrating the effectiveness of our approach in improving classification performance.

Below is the image that looks least like the number 5:

![Image](images/p3.png)

<span> Irrelevant fun fact: this looks a lot like the number 5 in Arabic numerals </span>

## Conclusion

This project shows the effectiveness of using the PCA algorithm to reduce the dimensionality of our image dataset and improve classification performance. The visual representation of the top principal components as images gives us a very good outlook into the most important features relevant to classification. By analyzing the eigenvalues, we were able to find the optimal subspace dimension for achieving accurate classification results.

The evaluation of error rates across various subspace dimensions showed us the impact of dimensionality reduction on classification accuracy. The findings highlight the importance of choosing an appropriate subspace dimension for maximizing the performance. It is also important to not that leveraging the principal components specific to the 'digit5' class allowed us to identify the image in the imageTest dataset that exhibited the most significant deviation from the characteristics of a digit 5.

Overall, the successful implementation of PCA and orthogonal energy analysis in this project shows their effectiveness in improving image classification.

<hr>

**Note:** the MATLAB code is private for Academic Integrity purposes.
