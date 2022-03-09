# 행성 테라포밍하기
# language: Python
# Terraforming planets program
# This program should be played in computer

print("\n★ ★ ★ ★ ★\n")
print("\n행성 테라포밍하기\n")
planet = input("테라포밍할 행성을 입력하세요 : ")

if planet == "수성":
    print("\n수성을 테라포밍하세요\n")
    print("질량: 3.023 × 10**23㎏\n부피: 6.083x10**10km3\n밀도: 5.44g/㎤\n적도 반지름: 2439.7km\n표면중력: 3.7m/s2\n기압: 0.000000001013hpa\n평균온도: 167°C\n태양까지의 거리: 0.39AU\n물: 거의 없음\n지권 구성성분: 철64.1%, 니켈3.7%, 규산염30%\n대기 구성성분: 거의 없음\n")
    gravity = float(input("표면중력 바꾸기: 표면중력(m/s2)(지구는 9.8m/s2) = "))
    if gravity >= 7.0 and gravity <= 13.0:
        print("표면중력이 '3.7m/s2'에서 '{0}m/s2' 으로 바뀜".format(gravity))
        pressure = float(input("기압 바꾸기: 기압(hpa)(지구는 1013hpa) = "))
        if pressure >= 700 and pressure <= 1300:
            print("기압이 '0.000000001013hpa'에서 '{0}hpa' 으로 바뀜".format(pressure))
            temperature = float(input("평균온도 바꾸기: 온도(°C) = "))
            if temperature >= -40 and temperature <= 40:
                print("평균온도가 '167°C'에서 '{0}°C' 로 바뀜".format(temperature))
                Astronomical_Units = float(input("태양까지의 거리 바꾸기: 거리(AU)(지구는 1AU) = "))
                if Astronomical_Units >= 0.7 and Astronomical_Units <= 1.5:
                    print("태양까지의 거리가 '0.39AU'에서 '{0}AU' 로 바뀜".format(Astronomical_Units))
                    water = float(input("물(%) = "))
                    if water >= 10 and water <= 100:
                        print("물 '{0}%' 로 바뀜".format(water))
                        composition_Fe = float(input("지권 구성성분 바꾸기: 철(%) = "))
                        composition_Ni = float(input("니켈(%) = "))
                        composition_SiO2 = float(input("규산염(%) = "))
                        composition_O = float(input("산소(%) = "))
                        composition_C = float(input("탄소(%) = "))
                        if composition_Fe > 0 and composition_Fe < 100 and composition_Ni > 0 and composition_Ni < 100 and composition_SiO2 > 0 and composition_SiO2 < 100 and composition_O > 0 and composition_O < 100 and composition_C > 0 and composition_C < 100:
                            print("철 '64.1%'에서 '{0}%', 니켈 '3.7%'에서 '{1}%', 규산염 '30%'에서 '{2}%', 산소 '{3}%', 탄소 '{4}%' 로 바뀜".format(composition_Fe, composition_Ni, composition_SiO2, composition_O, composition_C))
                            air_composition_N = float(input("대기 구성성분 바꾸기: 질소(%) = "))
                            air_composition_O = float(input("산소(%) = "))
                            air_composition_H = float(input("수소(%) = "))
                            air_composition_Ar = float(input("아르곤(%) = "))
                            air_composition_Co2 = float(input("이산화 탄소(%) = "))
                            if air_composition_N and air_composition_O and air_composition_H and air_composition_Ar and air_composition_Co2 > 0 and air_composition_N and air_composition_O and air_composition_H and air_composition_Ar and air_composition_Co2 < 100:
                                print("질소 '{0}%', 산소 '{1}%', 수소 '{2}%', 아르곤 '{3}%', 이산화 탄소 '{4}%' 로 바뀜\n".format(air_composition_N, air_composition_O, air_composition_H, air_composition_Ar, air_composition_Co2))
                                print("테라포밍된 수성\n질량: 3.023 × 10**23㎏\n부피: 6.083x10**10km3\n밀도: 5.44g/㎤\n적도 반지름: 2439.7km\n표면중력: {0}m/s2\n기압: {1}hpa\n평균온도: {2}°C\n태양까지의 거리: {3}AU\n물: {4}%".format(gravity, pressure, temperature, Astronomical_Units, water))
                                print("지권 구성성분: 철 {0}%, 니켈 {1}%, 규산염 {2}%, 산소 {3}%, 탄소 {4}%".format(composition_Fe, composition_Ni, composition_SiO2, composition_O, composition_C))
                                print("대기 구성성분: 질소 {0}%, 산소 {1}%, 수소 {2}%, 아르곤 {3}%, 이산화 탄소 {4}%\n\n".format(air_composition_N, air_composition_O, air_composition_H, air_composition_Ar, air_composition_Co2, water))
                                print("{0}을 테라포밍에 성공하셨습니다!\n\n---- ☆ 축하드립니다 ☆ ----\n--- ☆ Congratulations ☆ ---\n\nThank you for playing Terraforming program\n\nMade by creator yunohsung\nCopyright(C) 2020.yunohsung.All rights reserved\n\n".format(planet))
                            else:
                                print("잘못 입력 되었습니다.")
                        else:
                            print("잘못 입력 되었습니다.")
                    elif water < 10:
                        print("물이 부족합니다.\n테라포밍 실패...")
                    else:
                        print("잘못 입력되었습니다.")
                elif Astronomical_Units < 0.7:
                    print("태양까지의 거리가 너무 가깝습니다.\n테라포밍 실패...")
                elif Astronomical_Units > 1.5:
                    print("태양까지의 거리가 너무 멉니다.\n테라포밍 실패...")
                else:
                    print("잘못 입력 되었습니다.")
            elif temperature < -40:
                print("너무 차갑습니다.\n테라포밍 실패...")
            elif temperature > 40:
                print("너무 뜨겁습니다.\n테라포밍 실패...")
            else:
                print("잘못 입력 되었습니다.")
        elif pressure < 800:
            print("기압이 너무 약합니다.\n테라포밍 실패...")
        elif pressure > 1200:
            print("기압이 너부 강합니다.\n테라포밍 실패...")
        else:
            print("잘못 입력 되었습니다.")
    elif gravity < 7.0:
        print("표면중력이 너무 약합니다.\n테라포밍 실패...")
    elif gravity > 12.0:
        print("표면중력이 너무 강합니다.\n테라포밍 실패...")
    else:
        print("잘못 입력 되었습니다.")
elif planet == "금성":
    print("\n금성을 테라포밍하세요\n")
    print("질량: 4.8685×10**24kg\n부피: 9.28×10**11km3\n밀도: 5.204g/㎤\n적도 반지름: 6051.85km\n표면중력: 8.87m/s2\n기압: 93000hPa\n평균온도: 457°C\n태양까지의 거리: 0.723332AU\n물: 거의 없음\n지권 구성성분: 정보부족\n대기 구성성분: 이산화탄소96.5%, 질소3.5%, 이산화황0.015%, 아르곤0.007%, 수증기0.002%, 일산화 탄소: 0.0017%\n")
    gravity = float(input("표면중력 바꾸기: 표면중력(m/s2)(지구는 9.8m/s2) = "))
    if gravity >= 7.0 and gravity <= 13.0:
        print("표면중력이 '8.87m/s2'에서 '{0}m/s2' 으로 바뀜".format(gravity))
        pressure = float(input("기압 바꾸기: 기압(hpa)(지구는 1013hpa) = "))
        if pressure >= 700 and pressure <= 1300:
            print("기압이 '93000hPa'에서 '{0}hpa' 으로 바뀜".format(pressure))
            temperature = float(input("평균온도 바꾸기: 온도(°C) = "))
            if temperature >= -40 and temperature <= 40:
                print("평균온도가 '457°C'에서 '{0}°C' 로 바뀜".format(temperature))
                Astronomical_Units = float(input("태양까지의 거리 바꾸기: 거리(AU)(지구는 1AU) = "))
                if Astronomical_Units >= 0.7 and Astronomical_Units <= 1.5:
                    print("태양까지의 거리가 '0.723332AU'에서 '{0}AU' 로 바뀜".format(Astronomical_Units))
                    water = float(input("물(%) = "))
                    if water >= 10 and water <= 100:
                        print("물 '{0}%' 로 바뀜".format(water))
                        composition_Fe = float(input("지권 구성성분 바꾸기: 철(%) = "))
                        composition_Ni = float(input("니켈(%) = "))
                        composition_SiO2 = float(input("규산염(%) = "))
                        composition_O = float(input("산소(%) = "))
                        composition_C = float(input("탄소(%) = "))
                        if composition_Fe > 0 and composition_Fe < 100 and composition_Ni > 0 and composition_Ni < 100 and composition_SiO2 > 0 and composition_SiO2 < 100 and composition_O > 0 and composition_O < 100 and composition_C > 0 and composition_C < 100:
                            print("철 '{0}%', 니켈 '{1}%', 규산염 '{2}%', 산소 '{3}%', 탄소 '{4}%' 로 바뀜".format(composition_Fe, composition_Ni, composition_SiO2, composition_O, composition_C))
                            air_composition_N = float(input("대기 구성성분 바꾸기: 질소(%) = "))
                            air_composition_O = float(input("산소(%) = "))
                            air_composition_H = float(input("수소(%) = "))
                            air_composition_Ar = float(input("아르곤(%) = "))
                            air_composition_Co2 = float(input("이산화 탄소(%) = "))
                            if air_composition_N and air_composition_O and air_composition_H and air_composition_Ar and air_composition_Co2 > 0 and air_composition_N and air_composition_O and air_composition_H and air_composition_Ar and air_composition_Co2 < 100:
                                print("질소 '3.5%'에서 '{0}%', 산소 '{1}%', 수소 '{2}%', 아르곤 '0.007%'에서 '{3}%', 이산화 탄소 '96.5%'에서 '{4}%' 로 바뀜\n".format(air_composition_N, air_composition_O, air_composition_H, air_composition_Ar, air_composition_Co2))
                                print("테라포밍된 금성\n질량: 3.023 × 10**23㎏\n부피: 6.083x10**10km3\n밀도: 5.44g/㎤\n적도 반지름: 2439.7km\n표면중력: {0}m/s2\n기압: {1}hpa\n평균온도: {2}°C\n태양까지의 거리: {3}AU\n물: {4}%".format(gravity, pressure, temperature, Astronomical_Units, water))
                                print("지권 구성성분: 철 {0}%, 니켈 {1}%, 규산염 {2}%, 산소 {3}%, 탄소 {4}%".format(composition_Fe, composition_Ni, composition_SiO2, composition_O, composition_C))
                                print("대기 구성성분: 질소 {0}%, 산소 {1}%, 수소 {2}%, 아르곤 {3}%, 이산화 탄소 {4}%\n\n".format(air_composition_N, air_composition_O, air_composition_H, air_composition_Ar, air_composition_Co2, water))
                                print("{0}을 테라포밍에 성공하셨습니다!\n\n---- ☆ 축하드립니다 ☆ ----\n--- ☆ Congratulations ☆ ---\n\nThank you for playing Terraforming program\n\nMade by creator yunohsung\nCopyright(C) 2020.yunohsung.All rights reserved\n\n".format(planet))
                            else:
                                print("잘못 입력 되었습니다.")
                        else:
                            print("잘못 입력 되었습니다.")
                    elif water < 10:
                        print("물이 부족합니다.\n테라포밍 실패...")
                    else:
                        print("잘못 입력되었습니다.")
                elif Astronomical_Units < 0.7:
                    print("태양까지의 거리가 너무 가깝습니다.\n테라포밍 실패...")
                elif Astronomical_Units > 1.5:
                    print("태양까지의 거리가 너무 멉니다.\n테라포밍 실패...")
                else:
                    print("잘못 입력 되었습니다.")
            elif temperature < -40:
                print("너무 차갑습니다.\n테라포밍 실패...")
            elif temperature > 40:
                print("너무 뜨겁습니다.\n테라포밍 실패...")
            else:
                print("잘못 입력 되었습니다.")
        elif pressure < 800:
            print("기압이 너무 약합니다.\n테라포밍 실패...")
        elif pressure > 1200:
            print("기압이 너무 강합니다.\n테라포밍 실패...")
        else:
            print("잘못 입력 되었습니다.")
    elif gravity < 7.0:
        print("표면중력이 너무 약합니다.\n테라포밍 실패...")
    elif gravity > 12.0:
        print("표면중력이 너무 강합니다.\n테라포밍 실패...")
    else:
        print("잘못 입력 되었습니다.")
elif planet == "화성":
    print("\n화성을 테라포밍하세요\n")
    print("질량: 6.4171×10**23kg\n부피: 1.6310×10**11km3\n밀도: 3.9335g/㎤\n적도 반지름: 3396.2km\n표면중력: 3.711m/s2\n기압: 6.36hPa\n평균온도: -63°C\n태양까지의 거리: 1.523679AU\n물: 정보부족\n지권 구성성분: 정보부족\n대기 구성성분: 이산화탄소95.97%, 질소2.7%, 아르곤1.93%, 산소0.146%, 일산화 탄소: 0.0557%\n")
    gravity = float(input("표면중력 바꾸기: 표면중력(m/s2)(지구는 9.8m/s2) = "))
    if gravity >= 7.0 and gravity <= 13.0:
        print("표면중력이 '3.711m/s2'에서 '{0}m/s2' 으로 바뀜".format(gravity))
        pressure = float(input("기압 바꾸기: 기압(hpa)(지구는 1013hpa) = "))
        if pressure >= 700 and pressure <= 1300:
            print("기압이 '6.36hpa'에서 '{0}hpa' 으로 바뀜".format(pressure))
            temperature = float(input("평균온도 바꾸기: 온도(°C) = "))
            if temperature >= -40 and temperature <= 40:
                print("평균온도가 '-63°C'에서 '{0}°C' 로 바뀜".format(temperature))
                Astronomical_Units = float(input("태양까지의 거리 바꾸기: 거리(AU)(지구는 1AU) = "))
                if Astronomical_Units >= 0.7 and Astronomical_Units <= 1.5:
                    print("태양까지의 거리가 '1.523679AU'에서 '{0}AU' 로 바뀜".format(Astronomical_Units))
                    water = float(input("물(%) = "))
                    if water >= 10 and water <= 100:
                        print("물 '{0}%' 로 바뀜".format(water))
                        composition_Fe = float(input("지권 구성성분 바꾸기: 철(%) = "))
                        composition_Ni = float(input("니켈(%) = "))
                        composition_SiO2 = float(input("규산염(%) = "))
                        composition_O = float(input("산소(%) = "))
                        composition_C = float(input("탄소(%) = "))
                        if composition_Fe > 0 and composition_Fe < 100 and composition_Ni > 0 and composition_Ni < 100 and composition_SiO2 > 0 and composition_SiO2 < 100 and composition_O > 0 and composition_O < 100 and composition_C > 0 and composition_C < 100:
                            print("철 '{0}%', 니켈 '{1}%', 규산염 '{2}%', 산소 '{3}%', 탄소 '{4}%' 로 바뀜".format(composition_Fe, composition_Ni, composition_SiO2, composition_O, composition_C))
                            air_composition_N = float(input("대기 구성성분 바꾸기: 질소(%) = "))
                            air_composition_O = float(input("산소(%) = "))
                            air_composition_H = float(input("수소(%) = "))
                            air_composition_Ar = float(input("아르곤(%) = "))
                            air_composition_Co2 = float(input("이산화 탄소(%) = "))
                            if air_composition_N and air_composition_O and air_composition_H and air_composition_Ar and air_composition_Co2 > 0 and air_composition_N and air_composition_O and air_composition_H and air_composition_Ar and air_composition_Co2 < 100:
                                print("질소 '2.7%'에서 '{0}%', 산소 '0.146%'에서 '{1}%', 수소 '{2}%', 아르곤 '1.93%'에서 '{3}%', 이산화 탄소 '95.97%'에서 '{4}%' 로 바뀜\n".format(air_composition_N, air_composition_O, air_composition_H, air_composition_Ar, air_composition_Co2))
                                print("테라포밍된 화성\n질량: 3.023 × 10**23㎏\n부피: 6.083x10**10km3\n밀도: 5.44g/㎤\n적도 반지름: 2439.7km\n표면중력: {0}m/s2\n기압: {1}hpa\n평균온도: {2}°C\n태양까지의 거리: {3}AU\n물: {4}%".format(gravity, pressure, temperature, Astronomical_Units, water))
                                print("지권 구성성분: 철 {0}%, 니켈 {1}%, 규산염 {2}%, 산소 {3}%, 탄소 {4}%".format(composition_Fe, composition_Ni, composition_SiO2, composition_O, composition_C))
                                print("대기 구성성분: 질소 {0}%, 산소 {1}%, 수소 {2}%, 아르곤 {3}%, 이산화 탄소 {4}%\n\n".format(air_composition_N, air_composition_O, air_composition_H, air_composition_Ar, air_composition_Co2, water))
                                print("{0}을 테라포밍에 성공하셨습니다!\n\n---- ☆ 축하드립니다 ☆ ----\n--- ☆ Congratulations ☆ ---\n\nThank you for playing Terraforming program\n\nMade by creator yunohsung\nCopyright(C) 2020.yunohsung.All rights reserved\n\n".format(planet))
                            else:
                                print("잘못 입력 되었습니다.")
                        else:
                            print("잘못 입력 되었습니다.")
                    elif water < 10:
                        print("물이 부족합니다.\n테라포밍 실패...")
                    else:
                        print("잘못 입력되었습니다.")
                elif Astronomical_Units < 0.7:
                    print("태양까지의 거리가 너무 가깝습니다.\n테라포밍 실패...")
                elif Astronomical_Units > 1.5:
                    print("태양까지의 거리가 너무 멉니다.\n테라포밍 실패...")
                else:
                    print("잘못 입력 되었습니다.")
            elif temperature < -40:
                print("너무 차갑습니다.\n테라포밍 실패...")
            elif temperature > 40:
                print("너무 뜨겁습니다.\n테라포밍 실패...")
            else:
                print("잘못 입력 되었습니다.")
        elif pressure < 800:
            print("기압이 너무 약합니다.\n테라포밍 실패...")
        elif pressure > 1200:
            print("기압이 너무 강합니다.\n테라포밍 실패...")
        else:
            print("잘못 입력 되었습니다.")
    elif gravity < 7.0:
        print("표면중력이 너무 약합니다.\n테라포밍 실패...")
    elif gravity > 12.0:
        print("표면중력이 너무 강합니다.\n테라포밍 실패...")
    else:
        print("잘못 입력 되었습니다.")
elif planet == "태양":
    print("항성은 테라포밍 할 수 없습니다.")
elif planet == "지구":
    print("지구는 테라포밍 할 수 없습니다.")
elif planet == "목성":
    print("목성은 가스행성이므로 테라포밍 할수 없습니다.")
elif planet == "토성":
    print("토성은 가스행성이므로 테라포밍 할수 없습니다.")
elif planet == "천왕성":
    print("천왕성은 가스행성이므로 테라포밍 할수 없습니다.")
elif planet == "해왕성":
    print("해왕성은 가스행성이므로 테라포밍 할수 없습니다.")
elif planet == "명왕성":
    print("명왕성은 행성이 아닙니다.")
else:
    print("잘못 입력 되었습니다.")

# Terraforming planets program
# Made at Visual Studio Code.Supply python
# Made by alone
# 1st program
# Finish program coding date: 2020 . 11 . 15
# Editing complete date: 2021 . 08 . 09
# Creator yunohsung.★ ★ ★ ★ ★
# Copyright(C) 2020.yunohsung.All rights reserved