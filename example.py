import os
from Clustering import FaceClusterBuilder, ObjectClusterBuilder, Utils

path = r"FULL PATH TO IMG FOLDER"
fc = FaceClusterBuilder()
utils = Utils()
face_paths = []
with os.scandir(path) as files:
    for file in files:
        if file.name.endswith(".jpg"):
            face_paths.append("/".join([path, file.name]))

labelIds, labels, data, clt = fc.cluster(face_paths)
utils.showClusters(labelIds, clt, data)



path = r"FULL PATH TO IMG FOLDER"
fc = ObjectClusterBuilder()
utils = Utils()
face_paths = []
with os.scandir(path) as files:
    for file in files:
        if file.name.endswith(".jpeg"):
            face_paths.append("/".join([path, file.name]))

labelIds, labels, data, clt = fc.cluster(face_paths)
utils.showClusters(labelIds, clt, data)
