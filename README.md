# Collatz BU 논문 초안 및 재현 자료

**저자: Lee HaJin**  
**판본: 연구논문 초안 v0.1 · 2026-10-06**

이진 균일 치환 고정점의 블록 부호화에 대한 콜라츠 패리티 역상의 무리성  
*Irrationality of Collatz Parity Inverses for Block Codings of Binary Uniform Fixed Points*

이 저장소는 논문 초안과 보조 계산을 재현하는 자료를 함께 보관합니다. 원고는 저자의 최종 검토 전 초안이며, 전체 정리의 문헌상 최초성은 확정하지 않았습니다. 일반 콜라츠 추측의 해결을 주장하지 않습니다.

## 영문 투고용 원고

[english/collatz_bu_en.pdf](english/collatz_bu_en.pdf) · [english/collatz_bu_en.tex](english/collatz_bu_en.tex) · [변경 사항과 투고 전 확인 항목](english/README.md). 아래 한국어 초안 v0.1은 그대로 보존합니다.

## 문서

| 파일 | 내용 |
|---|---|
| [collatz_bu_draft_ko.pdf](collatz_bu_draft_ko.pdf) | 12쪽 논문 초안. 수식·번호·쪽 배치의 기준 문서 |
| [collatz_bu_draft_ko.docx](collatz_bu_draft_ko.docx) | 편집 가능한 Word 원고 |
| [collatz_bu_draft_ko.tex](collatz_bu_draft_ko.tex) | 전체 LaTeX 원고 |
| [collatz_bu_sources.zip](collatz_bu_sources.zip) | LaTeX 원고·글꼴·보충자료 원본 묶음 |
| [README_KO.txt](README_KO.txt) | 문서 사용 및 조판 안내 |
| [publication_notes_ko.txt](publication_notes_ko.txt) | 후보 선정·선행연구·보완 과제 |
| [supplement/README.txt](supplement/README.txt) | 재현 절차와 유한 검산의 범위 |
| [supplement/SOURCE_MANIFEST.json](supplement/SOURCE_MANIFEST.json) | 원본 연구 파일 7개의 출처와 SHA-256 |
| [SHA256SUMS](SHA256SUMS) | 이 저장소에 포함한 기존 자료의 SHA-256 |

Word의 절·정리·수식·문헌 번호는 고정되어 있으므로 구조를 바꾸면 번호도 갱신해야 합니다.

## PDF 조판

XeLaTeX와 필요한 LaTeX 패키지가 설치된 환경에서 저장소 루트에서 실행합니다.

```bash
xelatex -interaction=nonstopmode -halt-on-error collatz_bu_draft_ko.tex
xelatex -interaction=nonstopmode -halt-on-error collatz_bu_draft_ko.tex
```

한글 글꼴은 `fonts/`에 포함되어 있습니다. 글꼴 이용 조건은 [fonts/OFL.txt](fonts/OFL.txt)를 따릅니다.

## 계산 재현과 무결성

전체 계산 명령 및 결과 비교 방법은 [supplement/README.txt](supplement/README.txt)에 있습니다. 독립 검산 스크립트는 결과 파일을 기록하므로 안내대로 임시 복사본에서 실행하십시오. 유한 검산은 일반 정리의 서면 증명을 보완하는 자료이며 형식 검증이나 외부 동료심사를 뜻하지 않습니다.

Linux에서는 기존 자료의 해시를 다음과 같이 확인할 수 있습니다.

```bash
sha256sum -c SHA256SUMS
```

## 출처

- 기준 저장소: [hajin5305/collatz-research](https://github.com/hajin5305/collatz-research)
- 기준 커밋: `f751b9102355c516434ed9d0882bf4eb8608d95b`
- 정리 식별자: `RED-BINARY-UNIFORM-PADE-IRRATIONALITY`
- 원문 경로: `docs/research_records/2026-10-02/binary_uniform_pade/THEORY_KO.md`

원본 연구 저장소는 자료 준비 시 비공개였습니다. 이 저장소의 기존 원고·ZIP·재현 자료는 앞서 작성한 파일과 바이트 단위로 동일하게 보존했습니다.

## AI 활용

본 연구와 원고 준비에는 생성형 AI가 활용되었습니다. 이번 초안 준비에는 OpenAI의 ChatGPT를 사용하여 문헌 후보 탐색과 정리, 증명 구조 초안 및 비판적 검토, 계산 코드와 검산 보조, 원고 구성과 표현 정리를 수행했습니다. AI 활용 고지는 원고의 초록과 별도 절에도 포함되어 있습니다. 최종 원고의 정확성·인용·독창성 검토 책임은 저자에게 있습니다.
