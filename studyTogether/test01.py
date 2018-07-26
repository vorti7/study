'''
트와이스 팬클럽 카페지기 "redvelvetForever"는 카페 신규가입자들에게 최소한의 테스트를 거치게 하려고 한다.
문제는 트와이스 전 멤버의 활동명을 맞추는 문제로, 순서에 상관없이 이름들을 공백문자(" ")로 연속적으로 입력받게 한다.
(입력된 이름들이 멤버수와 맞지 않으면 따로 표시한다.)
입력과 출력의 예로
input>>
나연 쯔위 정연 채영 다현 미나 사나 모모 지효
output>>
정답입니다! 트와이스 광팬이군요!
input>>
김정은 도날드트럼프 푸틴 아베
output>>
멤버수가 맞지 않아요
input>>
나연 쯔위 정연 수지 다혈 마나 사나 무모 지효
output>>
땡! 오답입니다.


다음은 멤버 체크를 위한 java의 array와 Python의 tuple이다.

String[] members = {"나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"};
members = {"나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"}
'''

import sys

members = {"나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"}
twiceInput = input("트와이스 모든 멤버를 입력하세요.").split(" ")
if len(members)!=len(twiceInput):
	print("멤버수가 맞지 않아요 ")
	sys.exit()
for i in members:
	if i in twiceInput:
		pass
	else:
		print("땡! 오답입니다.")
		sys.exit()

print("정답입니다! 트와이스 광팬이군요!")
