이진 균일 치환 고정점의 블록 부호화에 대한 콜라츠 패리티 역상의 무리성
보조자료 및 재현 안내

저자: Lee HaJin
초안 및 보조자료 준비일: 2026-10-06
기준 저장소: hajin5305/collatz-research
고정 commit: f751b9102355c516434ed9d0882bf4eb8608d95b

1. 이 묶음의 목적

이 보조자료는 논문 초안의 유한 블록 항등식과 구체적인 Padé 인증서를
정확한 정수·유리수 연산으로 재현하기 위한 것이다. 주정리 BU의 일반적인
무리성 결론은 원고의 서면 증명에 근거한다. 유한 인증서 6개나 검사 성공을
무한한 모든 치환에 대한 증명 또는 일반 콜라츠 추측의 증명으로 해석하지 않는다.

주정리의 원본 위치는 다음과 같다.
  docs/research_records/2026-10-02/binary_uniform_pade/THEORY_KO.md
  정리 BU 및 §§0-9

정리는 q>=2인 이진 q-균일 치환의 일방향 고정점 t와 비어 있지 않은 이진
출력 블록 U,V에 대해 Phi(kappa(t))가 유리수일 필요충분조건을 분류한다.
그 조건은 t가 최종 주기적이거나 UV=VU인 것이다. 치환의 원시성이나 출력
블록의 같은 길이·같은 1의 개수를 요구하지 않는다. 모든 automatic 단어나
일반 비균일 치환을 포괄하는 정리는 아니다.

2. 파일과 원본의 대응

binary_uniform_pade/
  generate.py
    SymPy 선형대수로 6개의 유한 Padé 인증서를 생성한다.
    원본 패키지와 같은 파일이며 --output 인자가 필수이다.
  checker.py
    생성기를 import하지 않는 별도 검사기이다. 표준 라이브러리와 Fraction
    연산으로 인증서 및 유한 항등식을 검사한다. 제어 접두는 위치의 q진 전개로
    생성하므로 생성기의 반복 치환 방식과 구별된다.
  test_checker.py
    정상 사례와 변조 거부를 다루는 기존 회귀 검사 14개이다.
  certificates.json
    고정 기준점의 Padé 인증서 6개이다.
  RESULTS.json
    위 인증서 및 유한 항등식에 대한 원본 기대 결과이다.

위 다섯 파일의 원본 디렉터리:
  docs/research_records/2026-10-02/binary_uniform_pade/

independent_audit/
  verify_uniform_audit.py
    별도 구현으로 period-doubling, Cantor, Thue–Morse의 Padé 쌍을 재구성한다.
    아래 6절에서 설명하는 별도 실수 pseudo-trajectory 진단도 함께 실행한다.
    명령행 출력 파일 옵션은 없다. 스크립트 자신의 디렉터리에 있는
    EXACT_CHECK_RESULTS.json을 직접 기록하므로 반드시 임시 복사본에서 실행한다.
  EXACT_CHECK_RESULTS.json
    독립 구현의 원본 기대 결과이다.

위 두 파일의 원본 디렉터리:
  docs/research_records/2026-10-04/literature_value_audit/uniform_review/

requirements.txt
  생성기와 독립 Padé 검산에 필요한 SymPy 1.14.0의 설치 요구사항이다.
  checker.py와 test_checker.py 자체는 표준 라이브러리만 사용한다.
SOURCE_MANIFEST.json
  복사한 원본 파일 7개의 저장소 경로와 SHA-256 해시를 기록한다.
  최종 묶음을 만들 때 각 파일이 고정 commit의 원본과 바이트 단위로 일치함을 확인했다.
validation_summary.json
  2026-10-06에 실제로 완료한 재현, 실행 환경, 범위 및 결과 일치의 요약이다.
  기록된 실행 경로는 당시 작성 환경의 경로이며, 사용자의 재현에는 아래
  상대경로 명령을 사용한다.
literature_search_log.json
  초안 준비 과정의 문헌 검색 기록이다. 수학적 정리의 증명이나 전 문헌의
  완전한 조사 결과로 취급하지 않는다.
literature_review_ko.txt
  선행연구와 적용 조건, 전체 정리의 우선권에 관한 검토 범위를 설명한다.
README.txt
  이 안내문이다.

3. 실제 검증 환경과 확인된 결과

본 초안 준비 중 실제 사용한 환경:
  Python 3.12.14
  SymPy 1.14.0

원본 패키지의 임시 복사본에서 다음을 완료했다.
  - 기존 unit tests 14개 통과
  - generate.py로 Padé 인증서 6개 재생성
  - checker.py 정상 모드 통과
  - checker.py의 -O 최적화 모드 통과
  - verify_uniform_audit.py 정상 모드 통과
  - 원본 인증서, 정상·최적화 검사 결과, 독립 검산 결과의 4개 비교에서
    JSON 자료형과 값이 모두 일치

정확 유한 범위:
  - 유한 블록 분자·역아핀 자료: 254개 이진 단어
  - 첫 불일치 위치의 2-adic valuation: 10,795개 단어 쌍
  - 아핀 commutator 항등식 및 가환 예외: 900개 순서쌍
    이 수에는 commutator가 0인 가환 쌍도 포함된다.
  - 치환 계수 항등식: 1,200개 경우
  - 확대 블록의 유한 급수 항등식: 144개 경우
    유한 급수의 끝항을 유지하여 검사한다.
  - Padé 인증서: 6개
  - 정수 높이 간격: 2^13 - 3^8 = 1631 > 0

6개 제어 사례의 이름:
  thue_morse, period_doubling, cantor,
  delta_plus_one, delta_minus_two, delta_plus_two

모든 인증서는 z-차수가 6 이하이고 z^0부터 z^12까지의 13개 계수를
소거한다. 첫 비영항은 Cantor에서 14차, 나머지 5개에서 13차이다.
이는 구체적인 보조식의 유한 검산이다. 일반 치환마다 필요한 보조식의 존재와
실제 이동 평가값의 비영성은 원고에서 각각 별도로 증명한다.

4. 임시 복사본에서 전체 유한 재현 실행

아래 명령은 Linux/macOS의 bash를 기준으로 하며, 압축을 푼 supplement
디렉터리 안에서 시작한다. python3가 Python 3.12 계열을 가리키는 환경을
권장한다. 위의 실제 재현 버전은 3.12.14이다. 새 가상환경의 패키지 설치에는
패키지 저장소에 대한 접근이 필요하다.

다음 절차는 원본 보조자료를 수정하지 않고 임시 디렉터리에 복사한 뒤 실행한다.
BU_SOURCE_DIR와 BU_REPLAY_DIR는 이 재현 작업에만 쓰는 변수이다.

  BU_SOURCE_DIR="$(pwd -P)"
  BU_REPLAY_DIR="$(mktemp -d "${TMPDIR:-/tmp}/collatz-bu-replay.XXXXXX")"
  cp -R "$BU_SOURCE_DIR"/. "$BU_REPLAY_DIR"/
  cd "$BU_REPLAY_DIR"
  python3 -m venv .venv
  . .venv/bin/activate
  python -m pip install -r requirements.txt
  python -B -c 'import sys, sympy; print(sys.version); print(sympy.__version__)'

  cd binary_uniform_pade
  python -B -m unittest -v
  python -B generate.py --output regenerated.json
  python -B checker.py --certificate regenerated.json --report regenerated_results.json
  python -B -O checker.py --certificate regenerated.json --report optimized_results.json

  cd ../independent_audit
  cp EXACT_CHECK_RESULTS.json EXPECTED_EXACT_CHECK_RESULTS.json
  python -B verify_uniform_audit.py
  cd ..

각 명령의 종료코드와 출력을 확인한다. 실패한 명령이 있으면 해당 실패를
기록하고 그 실행 전체를 PASS로 보고하지 않는다. 다음의 비교까지 완료해야
재계산과 기대 결과의 일치를 확인한 것이다.

독립 스크립트는 EXACT_CHECK_RESULTS.json을 쓰므로 실행 직전에 기대값을
EXPECTED_EXACT_CHECK_RESULTS.json으로 보존했다. 이 복사와 재계산 모두
임시 디렉터리 안에서만 수행한다.

5. 원본 기대값과 재생성 JSON 비교

위 명령이 끝난 임시 supplement 디렉터리에서 다음을 실행한다. 단순한
문자열 서식 비교가 아니라 JSON 자료형과 값을 재귀적으로 비교한다.

python -B - <<'PY'
import json
from pathlib import Path

def typed_equal(a, b):
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(typed_equal(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(typed_equal(x, y) for x, y in zip(a, b))
    return a == b

pairs = [
    ('binary_uniform_pade/certificates.json',
     'binary_uniform_pade/regenerated.json'),
    ('binary_uniform_pade/RESULTS.json',
     'binary_uniform_pade/regenerated_results.json'),
    ('binary_uniform_pade/RESULTS.json',
     'binary_uniform_pade/optimized_results.json'),
    ('independent_audit/EXPECTED_EXACT_CHECK_RESULTS.json',
     'independent_audit/EXACT_CHECK_RESULTS.json'),
]
for expected, actual in pairs:
    a = json.loads(Path(expected).read_text(encoding='utf-8'))
    b = json.loads(Path(actual).read_text(encoding='utf-8'))
    if not typed_equal(a, b):
        raise SystemExit('FAIL: ' + expected + ' versus ' + actual)
    print('PASS: ' + expected + ' versus ' + actual)
print('PASS: all four typed JSON comparisons')
PY

검사기가 출력하는 PASS는 명시된 유한 검사를 통과했다는 뜻이다. 일반
무리성 정리, 외부 문헌의 전체 증명, 저장소 전체 검증 또는 원격 CI의 통과를
뜻하지 않는다. 재현 후 로그와 결과를 확인할 동안에는 임시 디렉터리를
보존하면 된다.

6. 최적화 모드와 독립 보조 진단의 범위

checker.py는 주요 검사에 명시적 예외를 사용하며, 정상 모드와 -O 모드에서
같은 결과를 확인했다. 이 사실을 다른 모든 스크립트의 -O 지원으로
일반화하지 않는다. verify_uniform_audit.py는 assert를 사용하므로 위와 같이
정상 모드로 실행한다. 독립 스크립트의 -O 실행을 검증 방법으로 사용하지 않는다.

verify_uniform_audit.py의 출력은 두 부분으로 구성된다.
  pade:
    period-doubling, Cantor, Thue–Morse 3개 사례의 독립 Padé 계산.
  pseudo_trajectory:
    유리수 -3에서 출발하고 실수 상태에 따라 분기를 선택하는 별도
    pseudo-trajectory의 정확한 2,000단계 진단.

두 번째 부분은 원래 문헌 검토의 보조 진단을 보존한 것이다. ordinary 정수의
실제 패리티 궤도라는 주장이 아니며, 이 BU 정리의 증명 입력이 아니다.
그 2,000단계 검산은 최종 2-adic 값의 유리성·무리성을 판정하지 않는다.
따라서 논문 본문의 BU 결과 표에는 이 진단을 포함하지 않았다.

7. 저자, AI 활용 및 검토 상태

논문과 이 보조자료의 저자는 Lee HaJin 단독이다. 연구 기록과 초안 작성에는
생성형 AI가 활용되었으며, 이번 재현 및 자연어 증명 재검토에도 ChatGPT를
사용했다. 별도 생성기·검사기 및 별도의 AI 검토라는 의미의 독립성을 외부
인간 전문가의 동료심사나 증명보조기를 이용한 형식 검증으로 해석하지 않는다.

원고는 저자의 최종 검토 전 초안이다. 제출 원고의 정확성, 인용, 독창성 및
공개 범위의 최종 확인과 책임은 저자에게 있다. 전체 BU 정리의 외부 우선권은
확정하지 않았으며, Thue–Morse 특수족과 Padé·Mahler 방법의 선행을 인정한다.
문헌 조사 범위와 남은 비교 의무는 함께 제공된 문헌 검토 파일을 따른다.
