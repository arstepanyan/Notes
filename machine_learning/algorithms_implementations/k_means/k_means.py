'''
K-means basic algorithm based on the following steps
Randomly initialize  𝐾 cluster centroids  𝜇1,𝜇2,...,𝜇𝑘∈𝑅𝑛

Repeat {
    for  𝑖=1  to  𝑚
       𝑐𝑖 := index (from  1 to  K) of cluster centroid closest to  𝑥𝑖
    for  𝑘=1  to  𝐾
       𝜇𝑘 := average (mean) of points assigned to cluster  𝑘
    }

Note: Supports only one time random initialization of cluster centroids.
Note: Randomly generates 2000 data points with two features each.
'''

class KMeans:
    def __init__(self, data, k):
        self.data = data
        import random
        if k > len(self.data):
            print(
                "Number of clusters is greater than the number of observations, assigning 2 cluster centers by default")
            k = 2
        self.centroids = random.sample(self.data, k)

    def distance(self, point1, point2):
        import math
        dist = 0
        for i in range(len(point1)):
            dist += (point1[i] - point2[i])**2
        return math.sqrt(dist)

    def cluster_assignement(self):
        cluster_indices = []
        for i in range(len(self.data)):
            min_distance = self.distance(self.data[i], self.centroids[0])
            cluster_indices.append(0)
            for centroid_ind in range(1, len(self.centroids)):
                cur_distance = self.distance(self.data[i], self.centroids[centroid_ind])
                if cur_distance < min_distance:
                    min_distance = cur_distance
                    cluster_indices[-1] = centroid_ind
        return cluster_indices

    def update_centroids(self):
        import numpy as np
        cluster_indices = self.cluster_assignement()
        new_centroids = [0 for _ in range(len(self.centroids))]
        for cluster_ind in range(len(new_centroids)):
            new_centroids[cluster_ind] = np.mean([self.data[i] for i in range(len(self.data)) if cluster_indices[i]==cluster_ind], axis=0)
        #print(new_centroids)
        return new_centroids

    def train(self, n_iter=10):
        import numpy as np
        for iter in range(n_iter):
            new_centroids = self.update_centroids()
            if np.array_equal(new_centroids, self.centroids):
                break
            else:
                self.centroids = new_centroids

    def predict(self, new_data):
        predicted = []
        for data_point in new_data:
            min_distance = self.distance(self.centroids[0], data_point)
            cluster_center = self.centroids[0]
            for centroid in self.centroids[1:]:
                cur_distance = self.distance(centroid, data_point)
                if cur_distance < min_distance:
                    cluster_center = centroid
                    min_distance = cur_distance
            predicted.append(cluster_center)
        return predicted

def main():
    import random
    n_clusters = int(input('Choose the number of clusters: '))
    n_iter = int(input('Choose the number of iterations '))

    # Generate random data
    data = [[random.randint(1, 10), random.randint(2, 5)] for _ in range(1000)]
    for i in range(1000):
        data.append([random.randint(12, 15), random.randint(6, 10)])

    # kmeans
    kmeans = KMeans(data, n_clusters)
    print('Centroids', kmeans.centroids)
    kmeans.train(n_iter=n_iter)
    print('Centroids', kmeans.centroids)

    print("Choose a point/s to predict it's cluster center:  ")
    n_points = int(input("\t How many points do you want to predict the cluster centers for? "))
    new_points = []
    for i in range(n_points):
        x = int(input(f"\t Choose the x coordinate of the {i+1}th point: "))
        y = int(input(f"\t Choose the y coordinate of the {i+1}th point: "))
        new_points.append([x, y])

    predicted = kmeans.predict(new_points)
    print(f"The new data point/s {new_points} cluster center/s ........ {predicted}")

if __name__ == '__main__':
    main()
