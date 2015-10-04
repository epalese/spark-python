# spark-python
Package to ease the usage of Spark with Python:
- no need to run the pyspark script
- helper functions to easily manipualate, join and aggregate RDDs 

## Installation
Install the package contained in the dist/ directory:
pip install dist/spark_python-0.0.1.tar.gz

## Usage
```python
import spark_python.spark as sp
sp.bootstrap('/Users/fix/dev/spark-1.4.1-bin-hadoop2.6')

import pyspark
from pyspark.context import SparkContext
sc = SparkContext(appName="PySparkShell")
example_rdd = sc.textFile('../spark-1.4.1-bin-hadoop2.6/data/mllib/lr_data.txt')
```
