import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

# 웹 페이지 제목 설정
st.title("🍱 급식 평균 만족도 조사 프로그램")
st.markdown("---")

st.subheader("✍️ 만족도 점수 입력 (1~5점)")

# 3명의 점수를 입력받는 위젯 (st.number_input 또는 st.slider 활용)
# 여기서는 직관적인 슬라이더와 숫자 입력창을 조합해 사용했습니다.
score1 = st.slider("첫 번째 학생 점수", min_value=1, max_value=5, value=3)
score2 = st.slider("두 번째 학생 점수", min_value=1, max_value=5, value=3)
score3 = st.slider("세 번째 학생 점수", min_value=1, max_value=5, value=3)

# 리스트에 점수 저장 및 평균 계산
scores = [score1, score2, score3]
avg = sum(scores) / 3

st.markdown("---")
st.subheader("📊 조사 결과")

# 결과 출력 (소수점 둘째 자리까지 표시)
st.write(f"**입력된 점수:** {scores}")
st.metric(label="평균 만족도", value=f"{avg:.2f} / 5.0")

# 만족도 등급 판별 및 스트림릿 알림 컴포넌트 출력
if avg >= 4:
    st.success("🎉 결과: **만족**")
elif 2 <= avg < 4:
    st.info("😐 결과: **보통**")
else:
    st.error("🚨 결과: **불만족**")