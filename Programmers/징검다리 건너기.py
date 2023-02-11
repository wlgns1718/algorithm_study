"""
"""
"""
 title: 징검다리 건너기
 level : Level3
 tag: binary search
 date:20230211
"""


def solution(stones, k):
    max_num = 200000000
    min_num = 1
    while min_num <= max_num:
        mid = (max_num + min_num) // 2
        cnt = 0
        for i in stones:
            if i - mid > 0:  # 0보다 크면 돌을 밟을 수 있으므로 건너뛴 횟수 0으로 초기화
                cnt = 0
            else:  # 0이되거나 음수가 되면 건너뛰는 횟수 저장
                cnt += 1
            if cnt >= k:
                break
        if cnt >= k:  # 건너뛰는 횟수가 k보다 크므로 건너는 사람 줄여야 됨 max를 mid로
            max_num = mid - 1
        else:  # 건너뛴 횟수가 k보다 작을경우 더 건널수 있으므로 건너는 사람 늘여야 됨 min을 mid로
            min_num = mid + 1

    return min_num


