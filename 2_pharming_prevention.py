"""
🔒 파밍(Pharming) 공격 예방 방법
DNS 검증, SSL/TLS, 보안 설정을 통한 방어

⚠️ 교육 목적으로만 사용 - 실제 해킹은 불법입니다
"""

from utils import *

class PharmingPrevention:
    """파밍 공격 예방 방법"""
    
    def __init__(self):
        self.trusted_dns_servers = {
            "Google": "8.8.8.8",
            "Cloudflare": "1.1.1.1",
            "KT": "168.126.63.1",
        }

    def show_prevention_methods(self):
        """파밍 예방 방법 설명"""
        print_header("🔒 파밍 공격 예방 방법")
        
        explanation = """
【 파밍 공격 방어의 5가지 핵심 】

1️⃣ DNS 보안 강화
   • 신뢰할 수 있는 DNS 서버 사용
   • DNSSEC 활성화
   
2️⃣ SSL/TLS 암호화 확인
   • HTTPS 사용 여부
   • SSL 인증서 검증
   
3️⃣ PC 보안
   • 최신 보안 업데이트 적용
   • 라우터 비밀번호 변경
   
4️⃣ 보안 소프트웨어
   • 신뢰할 수 있는 백신 설치
   • 실시간 위협 탐지
   
5️⃣ 사용자 교육
   • URL 주소 확인
   • 의심 링크 클릭 금지
   • 2단계 인증 사용
"""
        print_info(explanation)
        pause()

    def method1_trusted_dns(self):
        """방법1: 신뢰할 수 있는 DNS"""
        print_section("방법 1️⃣ : 신뢰할 수 있는 DNS 서버 사용")
        
        print_info("신뢰할 수 있는 DNS 서버:\n")
        for name, ip in self.trusted_dns_servers.items():
            print_safe(f"✓ {name}: {ip}")
        
        print_success("\n✅ 신뢰할 수 있는 DNS 사용 시 이점:")
        print("  • 공격자가 DNS 캐시 변조하기 어려움")
        print("  • 자동 피싱 사이트 필터링")
        
        create_divider()

    def method2_ssl_verification(self):
        """방법2: SSL 인증서 검증"""
        print_section("방법 2️⃣ : SSL/TLS 인증서 검증")
        
        print_info("SSL 인증서 확인 방법:\n")
        print_safe("1. 주소창 확인: https:// 필수")
        print_safe("2. 자물쇠 아이콘: 🔒 녹색 표시")
        print_safe("3. 인증서 정보: 유효한 발급자 확인")
        
        print_warning("\n⚠️  위험 신호:")
        print("  ❌ http:// (https 아님)")
        print("  ❌ 빨간색 경고 메시지")
        print("  ❌ 도메인 이름 불일치")
        
        create_divider()

    def method3_security_habits(self):
        """방법3: 안전한 사용 습관"""
        print_section("방법 3️⃣ : 안전한 사용자 습관")
        
        print_success("✅ 하면 좋은 습관:\n")
        habits = """
• URL 주소 직접 입력하기
• 의심 링크 클릭하지 않기
• 2단계 인증 활용하기
• 주기적 보안 점검하기
• 강력한 비밀번호 사용하기
"""
        print_info(habits)
        
        print_error("❌ 하면 안 되는 습관:\n")
        bad_habits = """
• 공용 Wi-Fi에서 금융거래
• 보안 업데이트 무시하기
• 의심 파일 다운로드하기
• PC 관리 소홀하기
• SNS에 금융정보 공개하기
"""
        print_warning(bad_habits)
        
        create_divider()

    def simulate_safe_access(self):
        """안전한 접속 시뮬레이션"""
        print_section("안전한 은행 사이트 접속")
        
        print_info("Step 1: URL 확인")
        print_safe("✅ 주소: https://www.bank.com")
        simulate_delay(1)
        
        print_info("Step 2: SSL 확인")
        print_safe("✅ 🔒 녹색 자물쇠 표시")
        simulate_delay(1)
        
        print_info("Step 3: 페이지 확인")
        print_safe("✅ 정상 페이지 로딩")
        simulate_delay(1)
        
        print_info("Step 4: 2단계 인증")
        print_safe("✅ SMS 인증코드 입력")
        simulate_delay(1)
        
        print_success("\n🔒 안전하게 거래 완료!")
        
        create_divider()

    def run_prevention_guide(self):
        """전체 예방 가이드 실행"""
        print_header("🔒 파밍 공격 예방 방법")
        
        self.show_prevention_methods()
        self.method1_trusted_dns()
        pause()
        
        self.method2_ssl_verification()
        pause()
        
        self.method3_security_habits()
        pause()
        
        self.simulate_safe_access()
        pause()
        
        print_section("🎯 최종 정리")
        conclusion = """
【 파밍 공격 예방 성공 】

파밍 공격은 기술적 방어와 사용자 주의가 결합되어야 
효과적으로 방어할 수 있습니다.

✓ 기술적 방어: DNS, SSL/TLS, 보안 소프트웨어
✓ 사용자 주의: URL 확인, 의심 신호 감지
✓ 정기적 관리: 시스템 업데이트, 보안 검사

다음: python 3_mitm_attack.py 를 실행하세요.
"""
        print_info(conclusion)


if __name__ == "__main__":
    prevention = PharmingPrevention()
    prevention.run_prevention_guide()
    
    print_success("\n✅ 파밍 공격 예방 학습 완료!")
    print_info("다음: python 3_mitm_attack.py 를 실행하세요.\n")