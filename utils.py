"""
공유 유틸리티 함수
해킹 교육 프로그램에서 사용되는 공통 함수들
"""

from colorama import Fore, Back, Style, init
import hashlib
import time

# colorama 초기화 (Windows에서 색상 표시를 위함)
init(autoreset=True)

class Colors:
    """콘솔 색상 정의"""
    SUCCESS = Fore.GREEN
    ERROR = Fore.RED
    WARNING = Fore.YELLOW
    INFO = Fore.CYAN
    ATTACK = Fore.RED + Back.BLACK
    SAFE = Fore.GREEN + Back.BLACK
    

def print_header(title):
    """프로그램 제목 출력"""
    print("\n" + "="*70)
    print(Colors.INFO + f"  {title}")
    print("="*70 + Style.RESET_ALL + "\n")


def print_section(title):
    """섹션 제목 출력"""
    print(Colors.INFO + f"\n📌 {title}")
    print("-" * 50 + Style.RESET_ALL)


def print_success(message):
    """성공 메시지 출력"""
    print(Colors.SUCCESS + f"✅ {message}" + Style.RESET_ALL)


def print_error(message):
    """에러 메시지 출력"""
    print(Colors.ERROR + f"❌ {message}" + Style.RESET_ALL)


def print_warning(message):
    """경고 메시지 출력"""
    print(Colors.WARNING + f"⚠️  {message}" + Style.RESET_ALL)


def print_info(message):
    """정보 메시지 출력"""
    print(Colors.INFO + f"ℹ️  {message}" + Style.RESET_ALL)


def print_attack(message):
    """공격 상황 표시"""
    print(Colors.ATTACK + f"🔓 [공격] {message}" + Style.RESET_ALL)


def print_safe(message):
    """안전 상황 표시"""
    print(Colors.SAFE + f"🔒 [안전] {message}" + Style.RESET_ALL)


def create_hash(data):
    """SHA-256 해시 생성"""
    return hashlib.sha256(data.encode()).hexdigest()


def simulate_delay(seconds=1):
    """네트워크 지연 시뮬레이션"""
    for i in range(seconds):
        print(".", end="", flush=True)
        time.sleep(1)
    print()


def create_divider():
    """구분선 출력"""
    print("\n" + "-" * 70 + "\n")


def format_url(url):
    """URL 포매팅"""
    return Colors.INFO + url + Style.RESET_ALL


def print_table_header(columns):
    """테이블 헤더 출력"""
    print(Colors.INFO + " | ".join(f"{col:^20}" for col in columns) + Style.RESET_ALL)
    print("-" * (22 * len(columns)))


def print_table_row(values):
    """테이블 행 출력"""
    print(" | ".join(f"{str(val):^20}" for val in values))


def pause():
    """사용자 입력 대기"""
    input(Colors.INFO + "\n👉 계속하려면 Enter를 누르세요..." + Style.RESET_ALL)


def yes_no_question(question):
    """Yes/No 질문"""
    while True:
        response = input(Colors.INFO + f"\n❓ {question} (y/n): " + Style.RESET_ALL).lower()
        if response in ['y', 'yes', 'n', 'no']:
            return response[0] == 'y'