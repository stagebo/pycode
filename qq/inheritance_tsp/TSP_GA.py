# -*- encoding: utf-8 -*-

import random
import math
from GA import GA

class TSP(object):
      def __init__(self, aLifeCount = 100,):
            self.initCitys()
            self.lifeCount = aLifeCount
            self.ga = GA(aCrossRate = 0.7, 
                  aMutationRage = 0.02, 
                  aLifeCount = self.lifeCount, 
                  aGeneLenght = len(self.citys), 
                  aMatchFun = self.matchFun())


      def initCitys(self):
            self.citys = []
            """
            for i in range(34):
                  x = random.randint(0, 1000)
                  y = random.randint(0, 1000)
                  self.citys.append((x, y))
            """

            #中国34城市经纬度
            self.citys.append((106.71, 26.57, '贵阳'))  # 贵阳
            self.citys.append((104.82, 26.58, '六盘水'))  # 六盘水
            self.citys.append((106.9, 27.7, ' 遵义'))  # 遵义
            self.citys.append((105.29, 27.32, '毕节'))  # 毕节
            self.citys.append((106.42, 26.14, '安顺'))  # 安顺
            self.citys.append((106.98, 26.46, '龙里'))  # 安顺
            self.citys.append((106.95, 27.06, '开阳'))  # 安顺
            self.citys.append((106.8, 28.16, '桐梓'))  # 安顺
            self.citys.append((106.74, 25.43, '罗甸'))  # 安顺
            self.citys.append((106.73, 27.1, '息烽'))  # 安顺
            self.citys.append((106.66, 26.14, '惠水'))  # 安顺
            self.citys.append((106.41, 27.81, '仁怀'))  # 安顺
            self.citys.append((106.22, 27.46, '金沙'))  # 安顺
            self.citys.append((106.2, 28.33, '习水'))  # 安顺
            self.citys.append((106.59, 26.84, '修文'))  # 安顺
            self.citys.append((106.46, 26.56, ' 清镇'))  # 安顺
            self.citys.append((108.11, 27.03, '施秉'))  # 安顺
            self.citys.append((108.07, 26.38, '雷山'))  # 安顺
            self.citys.append((107.97, 26.59, '凯里'))  # 安顺
            self.citys.append((107.89, 26.89, '黄平'))  # 安顺
            self.citys.append((107.88, 27.22, '余庆'))  # 安顺
            self.citys.append((107.86, 26.0, '务川'))  # 安顺
            self.citys.append((107.72, 27.97, '凤岗'))  # 安顺
            self.citys.append((107.6, 28.89, '道真'))  # 安顺
            self.citys.append((107.53, 26.72, '都匀'))  # 安顺
            self.citys.append((106.06, 25.75, '紫云'))  # 安顺
            self.citys.append((106.09, 25.17, '望谟'))  # 安顺
            self.citys.append((105.76, 26.66, '织金'))  # 织金
            self.citys.append((105.61, 27.16, '大方'))  # 大方
            self.citys.append((108.82, 27.68, '江口'))  # 安顺
            self.citys.append((108.41, 28.02, '印江'))  # 安顺
            self.citys.append((108.23, 27.94, '思南'))  # 安顺
            self.citys.append((107.5, 27.76, '湄潭'))  # 织金
            self.citys.append((105.47, 26.21, '六枝'))  # 大方
            # self.citys.append((116.46, 39.92))
            # self.citys.append((117.2,39.13))
            # self.citys.append((121.48, 31.22))
            # self.citys.append((106.54, 29.59))
            # self.citys.append((91.11, 29.97))
            # self.citys.append((87.68, 43.77))
            # self.citys.append((106.27, 38.47))
            # self.citys.append((111.65, 40.82))
            # self.citys.append((108.33, 22.84))
            # self.citys.append((126.63, 45.75))
            # self.citys.append((125.35, 43.88))
            # self.citys.append((123.38, 41.8))
            # self.citys.append((114.48, 38.03))
            # self.citys.append((112.53, 37.87))
            # self.citys.append((101.74, 36.56))
            # self.citys.append((117,36.65))
            # self.citys.append((113.6,34.76))
            # self.citys.append((118.78, 32.04))
            # self.citys.append((117.27, 31.86))
            # self.citys.append((120.19, 30.26))
            # self.citys.append((119.3, 26.08))
            # self.citys.append((115.89, 28.68))
            # self.citys.append((113, 28.21))
            # self.citys.append((114.31, 30.52))
            # self.citys.append((113.23, 23.16))
            # self.citys.append((121.5, 25.05))
            # self.citys.append((110.35, 20.02))
            # self.citys.append((103.73, 36.03))
            # self.citys.append((108.95, 34.27))
            # self.citys.append((104.06, 30.67))
            # self.citys.append((106.71, 26.57))
            # self.citys.append((102.73, 25.04))
            # self.citys.append((114.1, 22.2))
            # self.citys.append((113.33, 22.13))

            
      def distance(self, order):
            distance = 0.0
            for i in range(-1, len(self.citys) - 1):
                  index1, index2 = order[i], order[i + 1]
                  city1, city2 = self.citys[index1], self.citys[index2]
                  distance += math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

                  """
                  R = 6371.004
                  Pi = math.pi 
                  LatA = city1[1]
                  LatB = city2[1]
                  MLonA = city1[0]
                  MLonB = city2[0]

                  C = math.sin(LatA*Pi / 180) * math.sin(LatB * Pi / 180) + math.cos(LatA * Pi / 180) * math.cos(LatB * Pi / 180) * math.cos((MLonA - MLonB) * Pi / 180)
                  D = R * math.acos(C) * Pi / 100
                  distance += D
                  """
            return distance


      def matchFun(self):
            return lambda life: 1.0 / self.distance(life.gene)


      def run(self, n = 0):
            idx = 1
            while n > 0:
                  self.ga.next()
                  distance = self.distance(self.ga.best.gene)
                  print (("第%s代 : %s") % (str(self.ga.generation).zfill(3), "{:10f}".format(float(distance))),end='    ')

                  if idx%4==0:
                        print()
                  idx += 1
                  n -= 1


def main():
      tsp = TSP()
      tsp.run(120)


if __name__ == '__main__':
      main()


