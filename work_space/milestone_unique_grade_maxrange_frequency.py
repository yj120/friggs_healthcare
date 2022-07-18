# 마일스톤 고유넘버별로 5일씩 구간을 나눠 4번 응답 개수를 통해 평균 생후일수 구함
# 마일스톤 고유넘버 기준으로 오름차순 정렬,생후일수 기준으로 오름차순 정렬 -> 엑셀에서 처리 후 넣기
excelDF = pd.read_excel("mapping_uniquenum.xlsx")
# 최종 엑셀 파일에 저장할 데이터들
milestone_number = []   # 마일스톤 고유 넘버들
max_range = []  # 마일스톤 고유 넘버 내 최다 응답 개수가 나오는 구간들
frequency = []  # 마일스톤 고유 넘버 내 구간별 최다 응답 개수들
max_day_list = []   # 구간 속 최종적인 최다 응답 일수들 (최다 응답 일수 = 평균 일수)
max_frequency_list = [] # 구간 속 최종적인 최다 응답 개수들
def finalDay(max_days, max_answer):     # max_answer 리스트로 구간 내 최다 응답 일수를 구함
    x = 0
    for i in range(len(max_days)):
        if x < max_answer[i]:
            x = max_answer[i]
            index = i
    return max_days[index], max_answer[index]   # 최다 응답 일수와 개수 반환
def saveInfo(i, max_days, max_answer_4, max_day, max_frequency):     # 엑셀 파일에 내보낼 데이터들 append
    milestone_number.append(excelDF["milestone_unique"][i])  # 마일스톤 고유 넘버
    max_range.append(max_days)  # 최다 응답 구간
    frequency.append(max_answer_4)  # 그때 구간의 전체 응답 개수
    max_day_list.append(max_day)  # 구간 속 최다 응답 일수
    max_frequency_list.append(max_frequency)  # 그때 최다 응답 개수
def average_DoenDayAfterBirth():
    answer_4 = 0  # 구간 내 4번 응답 개수
    max_answer_4 = 0  # 구간 내 4번 최다 응답 개수
    ans = 0  # 동일 생후일자 내 4번 응답 개수
    answer = []  # 구간 내 생후일자별 4번 응답 개수들
    max_answer = []  # 구간 내 생후일자별 4번 최다 응답 개수들
    days = []  # 구간 내 생후일자들
    max_days = []  # 4번 최다 응답 개수가 나온 구간의 생후일수들
    for i in range(len(excelDF)):
        if i == len(excelDF)-1: # 마지막 행
            if excelDF["grade"][i] == 4:
                answer_4 += 1
                ans += 1
            answer.append(ans)
            if excelDF["done_day_after_birth"][i] != excelDF["done_day_after_birth"][i-1]:  # 생후일수가 달라졌다면
                days.append(excelDF["done_day_after_birth"][i])
            if max_answer_4 < answer_4:
                max_answer_4 = answer_4
                max_days = list(days)
                max_answer = list(answer)
            max_day, max_frequency = finalDay(max_days, max_answer)
            saveInfo(i, max_days, max_answer_4, max_day, max_frequency)
            break
        if excelDF["grade"][i] == 4:
            answer_4 += 1   # 구간 내 전체 4번 응답 개수 카운트
            ans += 1    # 구간 내 생후일자별 4번 응답 개수 카운트
        if excelDF["done_day_after_birth"][i] != excelDF["done_day_after_birth"][i+1]:  # 생후일수가 달라지면
            days.append(excelDF["done_day_after_birth"][i])
            answer.append(ans)   # 구간 내 생후일자별 4번 응답 개수 저장
            ans = 0    # 초기화
            if len(days) == 5:  # 5일 다 구하면 (구간을 5일마다 나눔)
                if max_answer_4 < answer_4:    # 이전에 구한 구간 내 전체 4번 응답 개수보다 현재 구한 4번 응답 개수가 많다면
                    max_answer_4 = answer_4
                    max_days = list(days)
                    max_answer = list(answer)
                answer_4 = 0    # 초기화
                days = []    # 초기화
                answer = []    # 초기화
        if excelDF["milestone_unique"][i] != excelDF["milestone_unique"][i+1]:  # 마일스톤 고유 넘버 달라지면
            if len(days) < 5:    # 마지막 구간이 5일 채우지 못 하고 끝날 경우
                if max_answer_4 < answer_4:
                    max_answer_4 = answer_4
                    max_days = list(days)
                    max_answer = list(answer)
            max_day, max_frequency = finalDay(max_days, max_answer)
            saveInfo(i, max_days, max_answer_4, max_day, max_frequency)
            answer_4 = 0  # 초기화
            max_answer_4 = 0  # 초기화
            days = []  # 초기화
            answer = []  # 초기화
            ans = 0    # 초기화
def output_toExcel():
    result_df = pd.DataFrame({"milestone_number": milestone_number, "range": range,
                              "frequency": frequency, "max_day": max_day_list, "max_frequency": max_frequency_list})
    print(result_df)  # 데이터 프레임 생성, 출력
    save_frame = '../데청캠 프로젝트/final_result.xlsx'  # 엑셀 파일 저장 위치
    result_df.to_excel(save_frame, index=False)
average_DoenDayAfterBirth()
output_toExcel()