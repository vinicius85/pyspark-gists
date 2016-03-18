from pyspark import SparkConf, SparkContext, SQLContext
from graphframes import GraphFrame

conf = (SparkConf()
         .setMaster("local")
         .setAppName("My app")
         .set("spark.executor.memory", "1g"))

sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)

#Usar python cassandra para gerar lista de resultados e alimentar dataframe

#Utilizar algoritmos de grafos para recomendacao (LPA, SCC)

#Usar matplotlib para gerar grafos