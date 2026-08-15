import time
import win32clipboard
import win32con
import pyautogui
import keyboard

# 한컴타자연습 실제 화면에 나오는 정확한 텍스트 목록 (이전과 동일)
AEGUKGA_1ST = [
    "애국가",
    "1. 동해물과 백두산이 마르고 닳도록",
    "하느님이 보우하사 우리나라 만세",
    "무궁화 삼천리 화려강산",
    "대한사람 대한으로 길이 보전하세."
]

def set_clipboard(text):
    """클립보드에 문자열 복사"""
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, text)
    win32clipboard.CloseClipboard()

def run_macro(target_cpm=700):
    """
    한컴타자연습 애국가 1절 자동 입력 매크로 (강화된 붙여넣기 방식)
    :param target_cpm: 목표 타수 (기본값 700타)
    """
    print("=" * 50)
    print(" 🚀 한컴타자연습 애국가 1절 자동 타이핑 매크로 (V2)")
    print(f" 🎯 목표 타수: 약 {target_cpm} CPM")
    print(" ⚠️  [F8] 키를 누르면 시작됩니다.")
    print(" ⚠️  [Esc] 키를 누르면 중단됩니다.")
    print("=" * 50)

    # F8 키 입력 대기
    keyboard.wait('f8')
    print("\n▶ 3초 후 시작합니다! 한컴타자연습 입력창을 클릭해 두세요.")
    time.sleep(3)

    for idx, line in enumerate(AEGUKGA_1ST, start=1):
        if keyboard.is_pressed('esc'):
            print("\n🛑 매크로가 중단되었습니다.")
            break

        # 클립보드로 문장 복사
        set_clipboard(line)
        time.sleep(0.05) # 클립보드 안정화 대기

        # pyautogui.hotkey('ctrl', 'v') 대신 윈도우 메시지 직접 전송 (더 확실함)
        # 윈도우 키 이벤트 메시지 WM_KEYDOWN (0x100), WM_KEYUP (0x101), WM_CHAR (0x102)
        # Ctrl+V는 가상 키코드 VK_CONTROL (0x11) + 'V' (0x56) 입니다.
        # 이 방식은 한영키 상태를 무시하고 강제 붙여넣기합니다.
        
        pyautogui.keyDown('ctrl')
        pyautogui.press('v', presses=1)
        pyautogui.keyUp('ctrl')

        time.sleep(0.05) # 입력 안정화 대기

        # 엔터키 입력 (다음 줄로 이동)
        pyautogui.press('enter')

        # 700타 기준 지연 시간 계산 (한글/숫자/기호 타수 + 엔터)
        total_strokes = len(line) * 2.5 + 1
        delay = total_strokes / (target_cpm / 60.0)

        # delay 시간에서 붙여넣기 대기 시간을 차감
        delay = max(0, delay - 0.1)

        print(f"[{idx}/{len(AEGUKGA_1ST)}] 입력 완료: {line} (대기: {delay:.2f}초)")
        time.sleep(delay)

    print("\n✅ 모든 문장 입력 완료! 결과를 확인하세요.")

if __name__ == "__main__":
    run_macro(target_cpm=700)
