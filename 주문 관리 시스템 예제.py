import decimal

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = decimal.Decimal(price)

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class Order:
    def __init__(self):
        self.products = []
        self.total = decimal.Decimal("0.00")

    def add_item(self, prod: Product):
        self.products.append(prod)
        self.total += prod.get_price()

    def get_item(self, name):
        for prod in self.products:
            if prod.get_name() == name:
                return prod
        return None

    def remove_item(self, name):
        prod = self.get_item(name)
        if prod:
            self.products.remove(prod)
            self.total -= prod.get_price()
            return True
        return False

    def calculate_final_price(self, tax_rate: decimal.Decimal):
        tax = self.total * tax_rate
        final_price = self.total + tax
        return final_price.quantize(decimal.Decimal("0.01"), rounding=decimal.ROUND_HALF_UP)

order = Order()  # Order 객체를 while 바깥에 생성

while True:
    print('=' * 20)
    print("[1]. 제품 추가")
    print("[2]. 제품 제거")
    print("[3]. 제품 목록 보기")
    print("[4]. 제품 상세 보기")
    print("[5]. 최종 가격 계산(세금 포함)")
    print("[6]. 프로그램 종료")
    print('=' * 20)
    num = input("번호 입력 : ")

    if num == "1":
        a = input("제품 이름 입력 : ")
        b = input("제품 가격 입력 : ")
        new = Product(a, b)
        order.add_item(new)
        print(f"제품 '{a}' 추가 완료")
    elif num == "2":
        a = input("삭제할 제품 이름 입력 : ")
        if order.remove_item(a):
            print("제품 삭제 완료")
        else:
            print("일치하는 제품 없음")
    elif num == "3":
        if order.products:
            for prod in order.products:
                print(f"{prod.get_name()}")
        else:
            print("제품 목록이 비어 있습니다.")
    elif num == "4":
        if order.products:
            for prod in order.products:
                print(f"제품명: {prod.get_name()}, 가격: {prod.get_price()}")
        else:
            print("제품 목록이 비어 있습니다.")
    elif num == "5":
        while True:
            tax_rate_input = float(input("세금 비율을 소수점으로 입력 (예: 0.1 = 10%): "))
            if 0.0 <= tax_rate_input < 1.0:
                break
            else:
                print("잘못된 세율 입력")
        tax_rate_d = decimal.Decimal(tax_rate_input)
        tax_rate = tax_rate_d.quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_HALF_UP)
        t = order.calculate_final_price(tax_rate)
        for prod in order.products:
            print(f"{prod.get_name()}의 세금 {prod.get_price()*tax_rate} ", end="")
            print()
        print(f"세금 포함 최종 가격: {t}")
    elif num == "6":
        print("프로그램 종료")
        break
    else:
        print("잘못된 번호 입력.")
