import sys

from pyspark.sql.types import DoubleType
from pyspark.mllib.regression import LabeledPoint

from pyspark import SparkContext, SparkConf
from pyspark.mllib.tree import RandomForest
from pyspark.mllib.linalg import Vectors
from sklearn.preprocessing import LabelEncoder
	
sc = SparkContext("local", "pyspark MLrandomforest")
data = sc.textFile ("input/input.txt").map(lambda line: line.split(','))
header = data.first()
data = data.filter(lambda line: line != header)

user_ratings = data.map(lambda x: (str(x[0]), [str(x[1])])).reduceByKey(lambda x, y: x + y).collect()
positive_user_ratings = data.map(lambda x: (str(x[0]), [(str(x[1]), int(x[2]))])).filter(lambda x: x[1][0][1] > 2).reduceByKey(lambda x, y: x + y).map(lambda x: (x[0], [m_r[0] for m_r in x[1]])).collect()

print('user_ratings:')
for u in user_ratings:
    print(u)
print('\n')
print('positive_user_ratings:')
for p in positive_user_ratings:
    print(p)

recommendations = {}
for u in user_ratings:
    recommendations[u[0]] = []
    for p in positive_user_ratings:
        if p[0] == u[0]: continue
        for movie in p[1]:
            if movie not in u[1] and movie not in recommendations[u[0]]: recommendations[u[0]].append(movie)

print('________________________')
print('recommendations:')
for user in recommendations:
    print(f'{user}:')
    print(f'{recommendations[user]}')
    print('________________________')

sc.parallelize([(user, recommendations[user]) for user in recommendations]).saveAsTextFile("output")