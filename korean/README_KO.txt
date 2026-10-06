논문 초안 및 재현 자료 안내
==========================

제목: 이진 균일 치환 고정점의 블록 부호화에 대한 콜라츠 패리티 역상의 무리성
영문 제목: Irrationality of Collatz Parity Inverses for Block Codings of Binary Uniform Fixed Points
저자: Lee HaJin
판본: 연구논문 초안 v0.1, 2026-10-06

1. 문서

collatz_bu_draft_ko.pdf는 수식, 정리 번호, 인용 및 페이지 배치의 기준 문서입니다.
collatz_bu_draft_ko.docx는 편집 가능한 Word 문서입니다. 수식을 Word의 기본 수식 형식으로 변환했으며,
절·정리·수식·문헌 참조 번호는 PDF와 일치하도록 고정했습니다. Word에서 본문을 재구성할 때에는
이 고정 번호도 함께 갱신해야 합니다. PDF와 Word 파일은 소스 압축 묶음과 별도로 제공됩니다.

collatz_bu_draft_ko.tex는 전체 LaTeX 원고입니다. 소스 묶음에는 한글 조판용 글꼴과 보충자료가
함께 들어 있습니다. 글꼴의 이용 조건은 fonts/OFL.txt를 참조하십시오.

2. PDF 다시 만들기

이 소스 묶음을 한 폴더에 풀고, XeLaTeX와 일반 LaTeX 패키지가 있는 환경에서 아래를 실행합니다.
실행 위치에는 collatz_bu_draft_ko.tex와 fonts 폴더가 함께 있어야 합니다.

  xelatex -interaction=nonstopmode -halt-on-error collatz_bu_draft_ko.tex
  xelatex -interaction=nonstopmode -halt-on-error collatz_bu_draft_ko.tex

두 번째 실행은 교차 참조를 확정합니다. 생성된 PDF는 이번 검증 환경에서 12쪽입니다.
LaTeX 배포판 차이에 따라 줄바꿈과 쪽수는 달라질 수 있습니다.
필요한 패키지는 원고 앞부분에 명시되어 있으며, 한글 본문 글꼴은 포함되어 있습니다.

3. 계산 재현

supplement/README.txt에 원본 파일의 위치, 의존성, 생성·검사 명령과 결과 비교 방법을 기록했습니다.
supplement/validation_summary.json은 이번 초안 준비 중 실행한 검사의 범위와 결과 요약입니다.
원 생성기, 별도 검사기, 검사 대상 인증서 및 독립 Padé 검산 코드를 함께 제공합니다.
유한 계산은 본문에 있는 일반 정리의 서면 증명을 보완하며, 그 자체가 형식 증명은 아닙니다.

4. 출처와 판본

기준 저장소: https://github.com/hajin5305/collatz-research
고정 commit: f751b9102355c516434ed9d0882bf4eb8608d95b
주정리 식별자: RED-BINARY-UNIFORM-PADE-IRRATIONALITY
원문: docs/research_records/2026-10-02/binary_uniform_pade/THEORY_KO.md, §§0-9
독립 보조검토: docs/research_records/2026-10-04/literature_value_audit/uniform_review
최신 문헌 감사: docs/research_records/2026-10-06/novelty_frontier 및 novelty_access_followup

저장소에 처음 기록된 날짜와 전체 문헌에서의 최초 발견일은 별개의 사항입니다.
이 초안은 전체 정리의 외부 우선권이 확인되었다고 주장하지 않습니다.
기준 저장소는 작성 시점에 비공개이며, 이 파일 묶음을 만드는 작업은 외부 공개나 학술지 제출을
수행하지 않았습니다. 소스 묶음에 포함된 기존 연구 코드는 기준 commit의 원본 그대로입니다.

5. AI 활용과 초안 상태

사용자의 요청에 따라 단독 저자를 Lee HaJin으로 기재했습니다. 연구와 초안 작성에 생성형 AI를
활용했다는 사실을 초록과 본문의 독립된 고지 절에 명시했습니다. 이번 초안 준비에 사용한
서비스는 OpenAI의 ChatGPT입니다. 확인하지 못한 과거 모델명과 버전은 기재하지 않았습니다.

본 자료는 저자의 최종 검토 전 초안입니다. AI의 검토는 외부 동료심사가 아니며, 계산 성공도
증명보조기 검증을 뜻하지 않습니다. 저자 소속, 연락처, ORCID, 연구비 또는 이해상충에 관한
확인되지 않은 정보를 임의로 추가하지 않았습니다.

6. 논문화 선정 메모

publication_notes_ko.txt에는 이 결과를 우선 선정한 이유, 다른 후보와의 비교, 확인된 선행연구,
제출 전 보완해야 할 항목을 기록했습니다. 문헌 검색 기록은 supplement 폴더에 들어 있습니다.

