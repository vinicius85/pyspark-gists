from pyspark import SparkConf, SparkContext, SQLContext
from graphframes import GraphFrame
from graphframes.examples import Graphs

conf = (SparkConf()
         .setMaster("local")
         .setAppName("My app")
         .set("spark.executor.memory", "1g"))

sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)

g = Graphs(sqlContext).friends()

g.vertices.show()
g.edges.show()

#g.bfs("name = 'Charlie'", "age > 30").show()

#result = g.stronglyConnectedComponents(maxIter=10)
#result.select("id", "component").orderBy("component").show()

#result = g.labelPropagation(maxIter=5)
#result.select("id", "label").show()

results = g.shortestPaths(landmarks=["a", "d"])
results.select("id", "distances").show()