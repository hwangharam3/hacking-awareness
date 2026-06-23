# 🔒 해킹 위험성 인식 교육 프로그램

이 프로젝트는 **파밍(Pharming)** 과 **중간자 공격(MITM)** 두 가지 주요 사이버 공격 기법을 직접 구현하고, 각각의 예방 방법을 실제로 보여주는 교육용 프로그램입니다.

## 📚 프로젝트 구조

```
hacking-awareness/
├── README.md                          # 프로젝트 설명
├── requirements.txt                   # 필요한 라이브러리
├── utils.py                           # 공유 유틸리티 함수
├── 1_pharming_attack.py               # 파밍 공격 시뮬레이션
├── 2_pharming_prevention.py           # 파밍 예방 방법
├── 3_mitm_attack.py                   # 중간자 공격 시뮬레이션
└── 4_mitm_prevention.py               # 중간자 공격 예방 방법
```

## 🎯 학습 목표

1. **파밍(Pharming)** 이해하기
   - DNS 변조를 통한 위조 사이트 접속
   - Hosts 파일 변조
   - 예방: DNS 검증, HTTPS 확인, 보안 프로그램

2. **중간자 공격(MITM)** 이해하기
   - 네트워크 트래픽 도청
   - 데이터 가로채기 및 변조
   - 예방: SSL/TLS 암호화, 인증서 검증, VPN

## 🚀 실행 방법

### 1단계: 라이브러리 설치
```bash
pip install -r requirements.txt
```

### 2단계: 파밍 공격 이해하기
```bash
python 1_pharming_attack.py
```

### 3단계: 파밍 예방 방법 학습
```bash
python 2_pharming_prevention.py
```

### 4단계: 중간자 공격 이해하기
```bash
python 3_mitm_attack.py
```

### 5단계: 중간자 공격 예방 방법 학습
```bash
python 4_mitm_prevention.py
```

## ⚠️ 주의사항

이 프로그램은 **교육 목적**으로만 사용되어야 합니다.
- 실제 해킹이나 불법 활동에 사용하면 안 됩니다.
- 오직 보안 인식 제고 및 학습 목적으로만 사용하세요.

## 📖 참고 자료

- [카스퍼스키: 파밍 정의](https://www.kaspersky.co.kr/resource-center/definitions/pharming)
- [IBM: 중간자 공격](https://www.ibm.com/kr-ko/think/topics/man-in-the-middle)

## 💡 각 프로그램이 보여주는 것

| 프로그램 | 내용 |
|---------|------|
| `1_pharming_attack.py` | 파밍 공격이 어떻게 작동하는지 시뮬레이션 |
| `2_pharming_prevention.py` | 파밍 공격 탐지 및 예방 방법 |
| `3_mitm_attack.py` | 중간자 공격이 어떻게 작동하는지 시뮬레이션 |
| `4_mitm_prevention.py` | 암호화와 SSL 검증을 통한 예방 방법 |

---

**⭐ 보안 교육은 나와 타인을 보호합니다!**