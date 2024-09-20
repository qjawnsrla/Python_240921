# 다형성이란 부모가 물려준 특성을 재정의하여 사용하는 것을 의미
# 오버로딩 (정적 바인딩) : 파이썬에서는 지원하지 않는다 (메소드 이름은 동일하고 매개변수의 개수나 타입으로 구분한다)
# 오버라이딩 (동적 바인딩) : 부모가 물려준 특성을 재정의하는 것

"""
def over_sum(x, y, z):
    return x + y + z

# 파이썬에서는 아래와 같이 오버로딩 지원 X
print(over_sum(1, 2, 3))        # 정수에 대한 덧셈
print(over_sum(1.1, 2.2, 3.3))  # 실수에 대한 덧셈
print(over_sum("혜인", "하나", "가을"))   # 문자열 덧셈
"""

class PrototypeTv:
    def __init__(self, is_on, channel, volume):
        self.is_on = is_on
        self.channel = channel
        self.volume = volume
    def set_on(self, is_on):
        self.is_on = is_on
    def set_channel(self, cnl):
        if 0 < cnl <= 1000:
            self.channel = cnl
            print(f"채널을 {self.channel}로 변경하였습니다.")
        else:
            print(f"채널 설정 범위가 아닙니다.")

class ProductTv(PrototypeTv):
    def set_channel(self, cnl):     # 오버라이딩
        if 1 < cnl <= 2000:
            self.channel = cnl
            print(f"채널을 {self.channel}로 변경하였습니다.")
        else:
            print(f"채널 설정 범위가 아닙니다.")

lg_tv = ProductTv(False, 20, 20)
lg_tv.set_channel(1500)

