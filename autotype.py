import time
import pyautogui
import keyboard

# 초성, 중성, 종성 2벌식 영문 자판 매핑
CHOSUNG_LIST = ['r', 'R', 's', 'e', 'E', 'f', 'a', 'q', 'Q', 't', 'T', 'd', 'w', 'W', 'c', 'z', 'x', 'v', 'g']
JUNGSUNG_LIST = ['k', 'o', 'i', 'O', 'j', 'p', 'u', 'P', 'h', 'hk', 'ho', 'hl', 'y', 'n', 'nj', 'np', 'nl', 'b', 'm', 'ml', 'l']
JONGSUNG_LIST = ['', 'r', 'R', 'rt', 's', 'sw', 'sg', 'e', 'f', 'fr', 'fa', 'fq', 'ft', 'fx', 'fv', 'fg', 'a', 'q', 'qt', 't', 'T', 'd', 'w', 'c', 'z', 'x', 'v', 'g']

def hangeul_to_keys(text):
    """한글 문장을 2벌식 키보드 입력 스트링으로 분해 변환"""
    res = []
    for ch in text:
        code = ord(ch)
        if 0xAC00 <= code <= 0xD7A3:
            s_index = code - 0xAC00
            cho = s_index // (21 * 28)
            jung = (s_index % (21 * 28)) // 28
            jong = s_index % 28
            res.append(CHOSUNG_LIST[cho])
            res.append(JUNGSUNG_LIST[jung])
            if jong != 0:
                res.append(JONGSUNG_LIST[jong])
        else:
            res.append(ch)
    return "".join(res)

AEGUKGA_1ST = [
    "애국가",
    "1. 동해물과 백두산이 마르고 닳도록",
    "하느님이 보우하사 우리나라 만세",
    "무궁화 삼천리 화려강산",
    "대한사람 대한으로 길이 보전하세."
]

def run_macro(target_cpm=700):
    print("=" * 50)
    print(" 🚀 한컴타자연습 실제 타이핑 매크로")
    print(f" 🎯 목표 타수: 약 {target_cpm} CPM")
    print(" ⚠️  [F8] 키를 누르면 시작됩니다.")
    print(" ⚠️  한컴타자연습 입력창이 [한글] 상태여야 합니다!")
    print("=" * 50)

    # F8 대기
    keyboard.wait('f8')
    print("\n▶ 3초 후 시작합니다! 한컴타자연습 입력창을 클릭해 두세요.")
    time.sleep(3)

    # 700타 기준 1타당 지연 시간 (60초 / target_cpm)
    stroke_interval = 60.0 / target_cpm

    for idx, line in enumerate(AEGUKGA_1ST, start=1):
        if keyboard.is_pressed('esc'):
            print("\n🛑 매크로가 중단되었습니다.")
            break

        # 한글 텍스트를 키보드 타수로 분해
        keys = hangeul_to_keys(line)
        
        # 실제 키 입력 진행
        for char in keys:
            if keyboard.is_pressed('esc'):
                break
            pyautogui.write(char)
            time.sleep(stroke_interval)

        # 줄 바꿈 (Enter)
        pyautogui.press('enter')
        time.sleep(0.1)

        print(f"[{idx}/{len(AEGUKGA_1ST)}] '{line}' 완료")

    print("\n✅ 모든 문장 입력 완료!")

if __name__ == "__main__":
    run_macro(target_cpm=700)
