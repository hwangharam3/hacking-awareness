"""
🔓 파밍(Pharming) 공격 시뮬레이션
DNS 변조와 Hosts 파일 변조를 통한 피싱 공격 시연

⚠️ 교육 목적으로만 사용 - 실제 해킹은 불법입니다
"""

from utils import *

class PharmingAttackSimulator:
    """파밍 공격 시뮬레이터"""
    
    def __init__(self):
        self.legitimate_sites = {
            "www.bank.com": "203.0.113.1",
            "www.shopping.com": "198.51.100.2",
            "www.payment.com": "192.0.2.3",
        }
        
        self.attacker_ips = {
            "www.bank.com": "10.0.0.50",
            "www.shopping.com": "10.0.0.51",
            "www.payment.com": "10.0.0.52",
        }
        
        self.dns_server = self.legitimate_sites.copy()
        self.is_compromised = False
        
    def explain_pharming(self):
        """파밍 공격 설명"""
        print_header("🔓 파밍(Pharming) 공격 이해하기")
        
        explanation = """
【 파밍(Pharming)이란? 】

파밍은 합법적인 웹사이트로 접속하려는 사용자를 공격자가 만든 
가짜(피싱) 사이트로 유도하여 개인정보를 탈취하는 공격입니다.

【 공격 원리 】
1️⃣ DNS 서버 변조
2️⃣ Hosts 파일 변조
3️⃣ 라우터 설정 변조

【 특징 】
✗ 사용자가 주소를 올바르게 입력해도 속기 쉬움
✗ 원본 사이트와 유사한 디자인으로 인해 잘 인식하지 못함
✗ 금융권, 인터넷 쇼핑몰 등 민감한 정보 입력 사이트를 집중 공격
"""
        print_info(explanation)
        pause()

    def show_normal_dns(self):
        """정상적인 DNS 동작"""
        print_section("시나리오 1️⃣ : 정상적인 DNS 동작")
        
        print_info("사용자가 'www.bank.com'에 접속하려고 합니다.\n")
        simulate_delay(1)
        
        print_info("DNS 조회 요청")
        print_info(f"사용자: 'www.bank.com의 IP 주소는?'")
        simulate_delay(1)
        
        domain = "www.bank.com"
        ip = self.dns_server[domain]
        
        print_success(f"DNS 응답: {domain} = {ip}")
        print_info(f"✓ {format_url(f'https://{domain}')} 으로 정상 접속")
        print_success("🔒 안전한 거래 진행 가능")
        
        create_divider()

    def show_dns_poisoning_attack(self):
        """DNS 포이즈닝 공격"""
        print_section("시나리오 2️⃣ : DNS 포이즈닝 공격")
        
        print_attack("공격자가 DNS 서버를 해킹합니다!")
        simulate_delay(2)
        
        print_warning("⚠️  DNS 서버 침해 감지!")
        print_info("공격자가 DNS 캐시를 변조하기 시작합니다...\n")
        
        for domain, fake_ip in self.attacker_ips.items():
            print_attack(f"DNS 변조: {domain} → {fake_ip}")
            self.dns_server[domain] = fake_ip
            simulate_delay(1)
        
        self.is_compromised = True
        
        print_error("\n❌ DNS 서버가 손상되었습니다!")
        create_divider()

    def user_access_attempt(self):
        """사용자의 접속 시도"""
        print_section("시나리오 3️⃣ : 사용자의 접속 시도")
        
        domain = "www.bank.com"
        print_info(f"사용자가 '{domain}'에 접속하려고 합니다.")
        print_info("⌨️  주소창에 정확히 입력:")
        print(f"   {format_url(domain)}")
        simulate_delay(2)
        
        print_info(f"\nDNS 조회 요청: '{domain}'의 IP 주소는?")
        simulate_delay(1)
        
        malicious_ip = self.dns_server[domain]
        print_error(f"DNS 응답: {domain} = {malicious_ip} (변조됨!)")
        
        print_warning(f"\n⚠️  사용자는 {format_url(f'http://{malicious_ip}')}로 연결됨")
        simulate_delay(1)
        
        print_attack("🔓 공격자의 피싱 사이트로 접속!")
        
        create_divider()

    def show_fake_banking_site(self):
        """가짜 은행 사이트"""
        print_section("시나리오 4️⃣ : 공격자의 가짜 은행 사이트")
        
        print_attack("피싱 사이트 렌더링...\n")
        
        fake_site = """
╔════════════════════════════════════════════╗
║   www.bank.com                      [≡]   ║
╠════════════════════════════════════════════╣
║                                            ║
║          🏦 국민은행 (위조 페이지)         ║
║                                            ║
║  로그인이 필요합니다.                      ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━        ║
║                                            ║
║  사용자 ID:  [________________________]    ║
║  비밀번호:   [________________________]    ║
║              [  로그인  ]                 ║
║                                            ║
║  ⚠️  페이지가 느립니다. 새로고침하세요.  ║
║  ❌ SSL 인증서 오류 무시                   ║
║                                            ║
╚════════════════════════════════════════════╝
"""
        print_attack(fake_site)
        
        print_warning("위험 신호들:")
        print("  ⚠️  주소 표시줄에 'http://' (https 아님)")
        print("  ⚠️  SSL 인증서 경고 메시지")
        print("  ⚠️  페이지 로딩이 느림")
        
        create_divider()

    def simulate_credential_theft(self):
        """자격증명 탈취"""
        print_section("시나리오 5️⃣ : 사용자의 실수")
        
        print_warning("사용자가 가짜 사이트인 줄 모르고 입력합니다:")
        print()
        print_error("입력된 정보:")
        print(f"  ID:      mybank123456")
        print(f"  Password: ●●●●●●●●●●●")
        
        simulate_delay(2)
        
        print_attack("💾 사용자의 로그인 정보가 공격자 서버로 전송됩니다!")
        print_attack("💾 신용카드 번호가 저장됩니다!")
        
        simulate_delay(2)
        
        print_error("\n❌ 피해 발생:")
        print("  • 은행 계좌 불법 접근")
        print("  • 돈 이체 및 출금")
        print("  • 신용 정보 도용")
        
        create_divider()

    def run_simulation(self):
        """전체 시뮬레이션 실행"""
        print_header("🔓 파밍(Pharming) 공격 시뮬레이션")
        
        self.explain_pharming()
        self.show_normal_dns()
        pause()
        
        self.show_dns_poisoning_attack()
        pause()
        
        self.user_access_attempt()
        pause()
        
        self.show_fake_banking_site()
        pause()
        
        self.simulate_credential_theft()
        pause()
        
        print_section("🎯 핵심 정리")
        conclusion = """
【 파밍 공격의 위험성 】

1️⃣ 사용자 인식 어려움
2️⃣ 대규모 피해 가능
3️⃣ 금융 사기 수단
4️⃣ 탐지 어려움

다음: python 2_pharming_prevention.py 로 예방 방법 학습
"""
        print_info(conclusion)


if __name__ == "__main__":
    simulator = PharmingAttackSimulator()
    simulator.run_simulation()
    
    print_success("\n✅ 파밍 공격 시뮬레이션 종료!")
    print_info("다음: python 2_pharming_prevention.py 를 실행하세요.\n")