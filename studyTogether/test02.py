'''
역삼동에 새로 이사온 희림이는 동네의 지역을 파악하기 위해 지도를 만들라고 한다.
지도 전체의 크기는 size로 입력 받으며 NxN 정사각형 모양과 크기를 가진다.
입력으로 맵의 크기와, 지도에 표시할 장소들의 숫자,이 후 그 숫자 만큼 역 좌표와 집의 좌표, 그리고 자주 가는 곳 좌표를 입력받고 좌표마다 역일 경우 0,집일 경우 1, 자주 가는 곳일 경우 2를 추가로 입력 받습니다.
맵에서 역, 집, 자주 가는 곳을 S, H, G로 표시되며 나머지는 빈공간으로 표시되고 지도의 가장자리를 X로 하는 지도를 출력하려 한다.
(x축과 y축에서 좌상이(0,0)이고 우로 갈수록 x좌표가 증가하고 내려갈수록 y자표가 증가한다.)
예> 맵의 크기를 먼저 입력받는다.
역, 집, 자주가는 곳의 좌표가 입력됩니다.
입력>>
8
5
3 8 0
4 5 1
5 1 2
2 3 2
6 7 2

출력>>
XXXXXXXXXX
X    G   X
X        X
X G      X
X        X
X   H    X
X        X
X     G  X
X  S     X
XXXXXXXXXX
단 범위 외의 좌표를 입력 받을 경우 프로그램은 종료됩니다.
'''
import sys

size = int(input())
#mapArray = [[[[" "]*(size+2)]*(size+2)]]
mapArray = [[" " for cols in range(size+2)]for rows in range(size+2)]
for i in range(len(mapArray)):
    for j in range(len(mapArray[i])):
        if i==0 or i==size+1 or j==0 or j==size+1:
            mapArray[i][j] = "X"

locSize = int(input())
symbols = ('S','H',"G")
for i in range(locSize):
    inputLoc = input().split(" ")
    mapArray[int(inputLoc[0])][int(inputLoc[1])] = symbols[int(inputLoc[2])]

for i in range(len(mapArray)):
    for j in range(len(mapArray[i])):
        print(mapArray[j][i],end="")
    print()
