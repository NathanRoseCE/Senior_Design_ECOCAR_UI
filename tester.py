import ROSData

obstacle = ROSData.Obstacle(25, 2, 4)
ROSData1 = ROSData.ROSData()
ROSData1.obstacles[25] = obstacle
print str(ROSData1.obstacles[25].x)
singletonTest = ROSData.ROSData()

print str(singletonTest.obstacles[25].x)
