from cassandra.cluster import Cluster
from cassandra import ConsistencyLevel

cluster = Cluster(['localhost'])
session = cluster.connect('Audify')

print("Conectado a Cassandra")
session.default_consistency_level = ConsistencyLevel.QUORUM