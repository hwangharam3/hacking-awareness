"""
🔓 중간자 공격(MITM) 시뮬레이션
네트워크 트래픽 도청 및 데이터 변조

⚠️ 교육 목적으로만 사용 - 실제 해킹은 불법입니다
"""

from utils import *

class MITMAttackSimulator:
    """중간자 공격 시뮬레이터"""
    
    def __init__(self):
        self.user_data = {
            "username": "user123",
            "password": "mySecurePass!",
            "credit_card": "1234-5678-9012-3456",
        }
        
        self.communication_log = []
    
    def explain_mitm(self):
        """MITM 공격 설명"""
        print_header("🔓 중간자 공격(MITM) 이해하기")
        
        explanation = """
【 중간자 공격(Man-In-The-Middle Attack)이란? 】

MITM은 공격자가 두 통신 주체(사용자와 서버) 사이에 
몰래 들어가 데이터를 가로채거나 변조하는 공격입니다.

【 주요 특징 】
✗ 통신 당사자들이 공격 사실을 인식하지 못함
✗ 실시간으로 데이터 도청 및 변조 가능
✗ 금융 정보, 개인정보 탈취에 효과적

【 MITM 공격의 4가지 방식 】

1️⃣ ARP 스푸핑 (ARP Spoofing)
   ├─ MAC 주소를 속여 트래픽을 자신으로 리다이렉트
   ├─ 같은 네트워크(WiFi) 내에서 가능
   └─ 라우터로 가는 데이터를 모두 가로챔

2️⃣ DNS 스푸핑 (DNS Spoofing)
   ├─ DNS 응답을 속여 공격자 서버로 유도
   ├─ 정상 도메인 → 공격자 IP로 변조
   └─ 파밍과 유사하지만 실시간 조작

3️⃣ 불안전한 WiFi (Evil Twin)
   ├─ 공격자가 가짜 WiFi 핫스팟 개설
   ├─ "Starbucks_WiFi" 같은 정상처럼 보이는 이름
   └─ 모든 트래픽이 공격자를 통해 흐름

4️⃣ SSL 스트립핑 (SSL Stripping)
   ├─ HTTPS를 HTTP로 강제 변환
   ├─ 암호화를 해제하여 데이터 노출
   └─ 사용자는 보안 연결이라고 착각
"""
        print_info(explanation)
        pause()

    def show_normal_communication(self):
        """정상적인 통신"""
        print_section("시나리오 1️⃣ : 정상적인 안전한 통신")
        
        print_info("사용자와 서버 간의 정상적인 통신:\n")
        
        communication = """
사용자 (Client)          서버 (Server)
    │                         │
    │──────────────────────>  │
    │   https://bank.com      │
    │                         │
    │  SSL/TLS 핸드셰이크     │
    │<──────────────────────  │
    │                         │
    │  [암호화된 데이터]      │
    │  ID: ●●●●●●●●●●●●    │
    │──────────────────────>  │
    │                         │
    │  ✅ 인증 성공           │
    │<──────────────────────  │
"""
        print_safe(communication)
        
        print_success("✅ 특징:")
        print("  • 모든 데이터가 암호화됨")
        print("  • 제3자가 내용 읽을 수 없음")
        
        create_divider()

    def show_arpspoofing_setup(self):
        """ARP 스푸핑 설정"""
        print_section("시나리오 2️⃣ : ARP 스푸핑 공격 준비")
        
        print_attack("공격자가 ARP 스푸핑을 시작합니다!\n")
        
        print_info("네트워크 환경:")
        print("  라우터 IP: 192.168.1.1 (MAC: AA:AA:AA:AA:AA:AA)")
        print("  사용자 IP: 192.168.1.100 (MAC: BB:BB:BB:BB:BB:BB)")
        print("  공격자 IP: 192.168.1.101 (MAC: CC:CC:CC:CC:CC:CC)")
        
        simulate_delay(1)
        
        print_attack("\n공격자가 거짓 ARP 패킷을 브로드캐스트합니다:\n")
        
        arp_attack = """
【 사용자에게 보낸 ARP 패킷 】
"192.168.1.1의 MAC 주소는 CC:CC:CC:CC:CC:CC입니다"
(실제로는 공격자의 MAC 주소)

결과: 사용자의 ARP 캐시가 변조됨
      192.168.1.1 → CC:CC:CC:CC:CC:CC (거짓!)
"""
        print_attack(arp_attack)
        
        print_attack("\n공격자가 라우터에도 거짓 ARP를 보냅니다!")
        print_error("\n❌ 이제 모든 트래픽이 공격자를 통해 흐릅니다!")
        
        simulate_delay(1)
        
        create_divider()

    def show_mitm_attack_process(self):
        """MITM 공격 과정"""
        print_section("시나리오 3️⃣ : 중간자 공격 진행")
        
        print_info("사용자가 안전하다고 생각하고 은행 접속:\n")
        
        print_info("Step 1: HTTPS 연결 시도")
        print("사용자 → 은행서버: HTTPS 연결 요청")
        simulate_delay(1)
        
        print_attack("공격자가 중간에 가로챕니다!")
        simulate_delay(1)
        
        print_info("Step 2: 데이터 입력")
        print("사용자가 로그인 정보 입력:")
        print(f"  ID: {self.user_data['username']}")
        print(f"  Password: {self.user_data['password']}")
        simulate_delay(1)
        
        print_attack("공격자가 데이터를 가로챕니다!")
        print_error("❌ 입력된 정보가 공격자에게 노출됨!")
        
        self.communication_log.append({
            "type": "credential",
            "username": self.user_data['username'],
            "password": self.user_data['password'],
            "intercepted": True
        })
        
        simulate_delay(1)
        
        print_attack("\n공격자가 신용카드 정보도 수집합니다:")
        print_error(f"❌ 신용카드: {self.user_data['credit_card']}")
        
        self.communication_log.append({
            "type": "payment",
            "card": self.user_data['credit_card'],
            "intercepted": True
        })
        
        print_error("\n❌ 모든 민감한 정보가 공격자 손에!")
        
        create_divider()

    def show_evil_twin_attack(self):
        """Evil Twin 공격"""
        print_section("시나리오 4️⃣ : Evil Twin (가짜 WiFi) 공격")
        
        print_attack("공격자가 가짜 WiFi 핫스팟을 개설합니다!\n")
        
        wifi_list = """
【 사용자가 보는 WiFi 목록 】

네트워크 이름                신호    보안
────────────────────────────────────
Starbucks                   강함    열림  ← 공격자의 가짜
Starbucks_Guest             중간    열림
Starbucks                   약함    열림  ← 정상 WiFi
"""
        print_warning(wifi_list)
        
        print_warning("⚠️  사용자가 실수로 공격자의 WiFi에 연결!\n")
        
        print_attack("공격자의 WiFi에 접속하는 순간:")
        print_attack("✗ 모든 데이터가 공격자 서버를 통과")
        print_attack("✗ 공격자가 모든 트래픽 모니터링")
        
        simulate_delay(1)
        
        print_error("\n❌ 공격자가 수집한 데이터:")
        print("  • 금융 사이트 로그인 정보")
        print("  • 개인 메시지 및 이메일")
        print("  • 신용카드 정보")
        
        create_divider()

    def show_attack_impact(self):
        """공격의 영향"""
        print_section("시나리오 5️⃣ : 공격의 결과")
        
        print_error("❌ MITM 공격으로 수집된 데이터:\n")
        
        print_table_header(["정보 타입", "내용", "피해"])
        
        impacts = [
            ["로그인 정보", "ID/Password", "계정 탈취"],
            ["금융 정보", "계좌/카드번호", "금전 사기"],
            ["개인정보", "주소/전화번호", "신원 도용"],
            ["통신 내용", "메시지/이메일", "프라이버시 침해"],
        ]
        
        for impact in impacts:
            print_table_row(impact)
        
        print()
        print_error("💰 금전적 피해: 수백만원대 손실 가능")
        print_error("🔓 정보 피해: 신용도 하락, 추가 사기")
        
        create_divider()

    def run_simulation(self):
        """전체 시뮬레이션 실행"""
        print_header("🔓 중간자 공격(MITM) 시뮬레이션")
        
        self.explain_mitm()
        
        self.show_normal_communication()
        pause()
        
        self.show_arpspoofing_setup()
        pause()
        
        self.show_mitm_attack_process()
        pause()
        
        self.show_evil_twin_attack()
        pause()
        
        self.show_attack_impact()
        pause()
        
        print_section("🎯 핵심 정리")
        conclusion = """
【 MITM 공격의 위험성 】

1️⃣ 실시간 데이터 도청
2️⃣ 데이터 변조 가능
3️⃣ 광범위한 피해
4️⃣ 탐지 어려움

다음: python 4_mitm_prevention.py 로 예방 방법 학습
"""
        print_info(conclusion)


if __name__ == "__main__":
    simulator = MITMAttackSimulator()
    simulator.run_simulation()
    
    print_success("\n✅ MITM 공격 시뮬레이션 종료!")
    print_info("다음: python 4_mitm_prevention.py 를 실행하세요.\n")