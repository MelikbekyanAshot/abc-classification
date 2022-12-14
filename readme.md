# ABC classification library
ABC classification is an inventory categorisation technique. A typical example of ABC classification is the segmentation of products (entity) based on sales (value). The best-selling products that contribute to up to 70% of the total sales belong to cluster A. The products making up the next 20% of sales are in cluster B, whereas the products representing the last 10% of sales, belong to class C. Hence, the pattern is named after the three clusters (ABC).

## Example
Installation
```
pip install abc-classification
```
Import 
```
from abc_classification.abc_classifier import ABCClassifier
```
Let's say we have dataframe 

| product      | total sold |
|--------------|------------|
| fade cream   | 	27000     |
| 	powders	    | 24000      |
| 	shadows	    | 18000      |
| 	mascara	    | 16000      |
| 	lipstick	   | 6000       |
| 	concealer	  | 5000       |
| 	sculptors 	 | 4000       |

You can create ABCClasifier object, pass your dataframe 
to it and call classify method.

```
abc_clf = ABCClassifier(df)
abc_df = abc_clf.classify('product', 'total sold')
```

This way you'll get new dataframe with classified products.

| product      | total sold | class |
|--------------|------------|-------|
| fade cream   | 	27000     | A     |
| 	powders	    | 24000      | A     |
| 	shadows	    | 18000      | A     |
| 	mascara	    | 16000      | B     |
| 	lipstick	   | 6000       | B     |
| 	concealer	  | 5000       | C     |
| 	sculptors 	 | 4000       | C     |

You also can use brief_abc method to get aggregated information
```
abc_clf.brief_abc(abc_df)
```
| class | total sold |
|-------|------------|
| A     | 69000      |
| B     | 16000      |
| C     | 15000      |

You can plot pareto chart.
```
from abc_classification.abc_visualiser import pareto_chart


pareto_chart(abc_df, 'total_sold', 'product')
```
![Pareto chart](images/pareto_chart.png)