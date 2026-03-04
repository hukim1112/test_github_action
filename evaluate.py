import sys
import time

# =====================================================================
# [LLMOps 실습용 평가 스크립트]
# 1. 아래 FAKE_SCORE 값을 0.85 미만(예: 0.70)으로 설정하고 Push 해보세요. (Fail)
# 2. 이번에는 FAKE_SCORE 값을 0.85 이상(예: 0.95)으로 설정하고 Push 해보세요. (Pass)
# =====================================================================

FAKE_SCORE = 0.80  # <-- 이 값을 수정해가며 테스트하세요!
QUALITY_GATE = 0.85

print("🧪 [Step 1] LLM 파이프라인 모델 성능 측정 시작...")
for i in range(3):
    time.sleep(1)
    print("   ... 답변의 충실도(Faithfulness) 분석 중 ...")

print("\n📊 [Step 2] 평가 평가지표 검증 완료")
print(f"👉 측정된 모델 점수: {FAKE_SCORE}")
print(f"👉 달성해야 할 품질 방어선(Quality Gate) 점수: {QUALITY_GATE}\n")

print("🚧 [Step 3] Quality Gate 최종 판정 작동")

if FAKE_SCORE < QUALITY_GATE:
    print(f"❌ [Fail / Block] 치명적 오류: 모델 성능이 기준에 미달합니다!")
    print(f"❌ 안전을 위해 프로덕션 배포 파이프라인을 즉시 중단합니다.")
    # sys.exit(1)은 GitHub Actions에게 "이 워크플로는 실패했어! 멈춰!"라고 알려주는 중요한 신호입니다.
    sys.exit(1)
else:
    print(f"✅ [Pass] 훌륭합니다! 모델의 품질 기준을 통과했습니다.")
    print(f"✅ 승인 완료. 다음 단계인 가상의 프로덕션 서버 배포 프로세스로 넘어갑니다.")
    # sys.exit(0)은 GitHub Actions에게 "워크플로가 성공적으로 끝났어! 다음 단계로 가!"라고 알려주는 신호입니다.
    sys.exit(0)
