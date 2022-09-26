# ABC classification library
Library is in process of development. It'll be published on pypi.org soon.

## Example
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
| B     | 22000      |
| C     | 9000       |
