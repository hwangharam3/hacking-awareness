"""
🔒 중간자 공격(MITM) 예방 방법
SSL/TLS 암호화, VPN, 인증서 검증

⚠️ 교육 목적으로만 사용 - 실제 해킹은 불법입니다
"""

from utils import *

class MITMPrevention:
    """MITM 공격 예방 방법"""
    
    def show_prevention_intro(self):
        """예방 방법 소개"""
        print_header("🔒 MITM 공격 예방 방법")
        
        intro = """
【 MITM 공격 방어의 핵심 】

MITM 공격을 효과적으로 방어하려면:
1️⃣ 암호화: 데이터를 읽을 수 없게 만듦
2️⃣ 인증: 진짜 서버인지 확인
3️⃣ 네트워크 보안: 안전한 환경에서 통신
4️⃣ 사용자 주의: 의심 신호 감지

각 방법을 자세히 살펴봅시다!
"""
        print_info(intro)
        pause()

    def method1_https_ssl_tls(self):
        """방법1: HTTPS/SSL-TLS"""
        print_section("방법 1️⃣ : HTTPS/SSL-TLS 암호화")
        
        print_info("SSL/TLS란?\n")
        print("""
데이터를 암호화하여 전송하는 보안 프로토콜
공격자가 패킷을 가로쳐도 내용을 읽을 수 없음
""")
        
        print_safe("✅ HTTPS의 작동 원리:\n")
        
        process = """
Step 1: SSL 핸드셰이크
────────────────────
클라이언트 ←→ 서버
• 서버 인증서 전송
• 암호화 알고리즘 협상

Step 2: 암호화 채널 수립
────────────────────
양쪽이 동일한 암호화 키 소유

Step 3: 데이터 통신
────────────────────
[평문] 'password' 
  ↓
[암호화] 'a8f3k9d7l2m0...'
"""
        print_info(process)
        
        print_success("\n✅ HTTPS 사용 시 이점:")
        print("  • 데이터가 암호화되어 전송")
        print("  • 공격자가 내용을 읽을 수 없음")
        print("  • 데이터 변조 감지 가능")
        
        create_divider()

    def method2_certificate_validation(self):
        """방법2: 인증서 검증"""
        print_section("방법 2️⃣ : SSL 인증서 검증")
        
        print_info("SSL 인증서 검증이 중요한 이유:\n")
        print("""
공격자도 자신의 인증서를 만들 수 있습니다.
사용자는 '정상 인증서'인지 '위조 인증서'인지 구분해야 합니다.
""")
        
        print_safe("\n✅ 신뢰할 수 있는 인증서 확인 사항:\n")
        
        checks = """
1️⃣ 발급 기관 (Issuer) 확인
   ✓ 신뢰할 수 있는 CA
   ✗ "자체 서명" (Self-signed)

2️⃣ 도메인 이름 일치
   ✓ 인증서의 도메인 = 접속 도메인
   ✗ 불일치하면 경고

3️⃣ 만료 날짜 확인
   ✓ 유효 기간 내
   ✗ 만료된 인증서
"""
        print_info(checks)
        
        print_warning("\n⚠️  의심할 만한 인증서 특징:")
        print("  ❌ 자체 서명 인증서")
        print("  ❌ 만료된 인증서")
        print("  ❌ 도메인 이름 불일치")
        
        create_divider()

    def method3_vpn_usage(self):
        """방법3: VPN 사용"""
        print_section("방법 3️⃣ : VPN(Virtual Private Network) 사용")
        
        print_info("VPN이란?\n")
        print("""
인터넷 연결을 암호화하여 가상 사설 네트워크로 만듦
ISP, 공유기, 로컬 네트워크 공격자가 트래픽 감시 불가능
""")
        
        print_safe("\n✅ VPN 사용 흐름:\n")
        
        vpn_flow = """
【 VPN 미사용 】
사용자 PC ──────> ISP ──────> 웹서버
        (평문 노출)     (누구나 봄)

【 VPN 사용 】
사용자 PC ──────> [VPN 터널] ──────> 웹서버
        (암호화)           (숨겨짐)

결과: ISP, 공격자, 라우터가 내용 볼 수 없음
"""
        print_info(vpn_flow)
        
        print_success("\n✅ VPN 사용 시 보호받는 것:")
        print("  • ARP 스푸핑: 효과 없음 (암호화됨)")
        print("  • WiFi 도청: 불가능 (VPN 터널)")
        print("  • ISP 추적: 차단됨")
        
        create_divider()

    def method4_secure_wifi(self):
        """방법4: 안전한 WiFi 선택"""
        print_section("방법 4️⃣ : 안전한 WiFi 사용")
        
        print_warning("\n❌ 피해야 할 WiFi:\n")
        
        bad_wifi = """
1️⃣ 암호 없는 개방형 WiFi
   • "Starbucks", "Public WiFi" 등
   • 누구나 연결 가능
   • 중간자 공격에 취약

2️⃣ 신뢰할 수 없는 WiFi
   • 정체 불명의 핫스팟
   • 너무 강한 신호

3️⃣ 가짜 WiFi (Evil Twin)
   • 정상 WiFi와 이름 유사
   • 실제로는 공격자 네트워크
"""
        print_error(bad_wifi)
        
        print_safe("\n✅ 안전한 WiFi 사용 방법:\n")
        
        safe_wifi = """
1️⃣ 개인용 WiFi만 사용
   • 집/회사 WiFi (암호 보호됨)

2️⃣ WiFi 보안 설정 확인
   • WPA3 또는 WPA2 암호화
   • 강력한 비밀번호

3️⃣ 공용 WiFi 사용 시
   • VPN 필수
   • 금융거래 금지
"""
        print_info(safe_wifi)
        
        create_divider()

    def show_safe_browsing_example(self):
        """안전한 브라우징 예시"""
        print_section("실제 사례: 안전한 인터넷 사용")
        
        print_info("시나리오: 카페에서 은행 업무\n")
        
        scenario = """
Step 1: VPN 활성화
────────────────────
□ 먼저 VPN 앱 실행
□ 신뢰할 수 있는 서버 선택
□ 연결 확인

Step 2: 안전한 WiFi 확인
────────────────────
□ 카페 직원에게 정확한 WiFi 이름 확인
□ 정확히 일치하는 WiFi 선택

Step 3: HTTPS 확인
────────────────────
□ 주소: https://www.bank.com
□ 🔒 자물쇠 아이콘 확인
□ 인증서 발급자 확인

Step 4: 거래 진행
────────────────────
□ 2단계 인증 활성화
□ SMS 인증코드 입력

결과: 🔒 안전하게 은행 업무 완료!
"""
        print_safe(scenario)
        
        create_divider()

    def show_detection_methods(self):
        """공격 탐지 방법"""
        print_section("MITM 공격 탐지 방법")
        
        print_warning("\n⚠️  MITM 공격이 발생하면 나타나는 신호:\n")
        
        signs = """
1️⃣ SSL 인증서 경고
   ⚠️  "이 사이트는 안전하지 않습니다"
   ⚠️  "인증서가 유효하지 않습니다"
   
2️⃣ 연결 끊김
   ⚠️  자주 로그아웃됨
   ⚠️  연결이 자주 끊김
   
3️⃣ 속도 저하
   ⚠️  평소보다 인터넷 느림
   
4️⃣ 비정상적인 활동
   ⚠️  모르는 거래 기록
"""
        print_warning(signs)
        
        print_error("\n❌ 이런 신호가 나타나면 즉시 중단하세요!\n")
        
        action = """
1. 브라우저 닫기
2. 해당 네트워크 연결 끊기
3. 기기 재부팅
4. 관련 기관에 신고
"""
        print(action)
        
        create_divider()

    def run_prevention_guide(self):
        """전체 예방 가이드"""
        print_header("🔒 MITM 공격 예방 방법")
        
        self.show_prevention_intro()
        
        self.method1_https_ssl_tls()
        pause()
        
        self.method2_certificate_validation()
        pause()
        
        self.method3_vpn_usage()
        pause()
        
        self.method4_secure_wifi()
        pause()
        
        self.show_safe_browsing_example()
        pause()
        
        self.show_detection_methods()
        pause()
        
        print_section("🎯 MITM 예방 종합 체크리스트")
        
        checklist = """
【 일상적인 보안 습관 】

□ HTTPS 사이트만 사용
□ 인증서 검증 확인
□ 공용 WiFi에서 VPN 사용
□ 신뢰할 수 있는 WiFi만 선택
□ 2단계 인증 활성화
□ 정기적인 보안 검사

【 기술적 방어 】

□ 방화벽 활성화
□ OS 보안 업데이트
□ 브라우저 최신 버전
□ VPN 설정 정기 점검

【 상황 대응 】

□ 인증서 경고 시 계속 진행 안함
□ 이상 증상 시 즉시 중단
□ 비정상 거래 시 즉시 신고
"""
        print_info(checklist)
        
        print_success("\n✅ MITM 공격은 다층 방어로 예방 가능합니다!")


if __name__ == "__main__":
    prevention = MITMPrevention()
    prevention.run_prevention_guide()
    
    print_success("\n✅ MITM 공격 예방 학습 완료!")
    print_info("🎉 모든 보안 교육 프로그램 완료!\n")
    print_info("배운 내용 정리:")
    print("  ✓ 파밍 공격 원리 및 예방")
    print("  ✓ MITM 공격 원리 및 예방")
    print("  ✓ 안전한 인터넷 사용 방법")
    print("  ✓ 보안 인식 및 대응\n")