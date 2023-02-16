/**
 title: 햄버거 다이어트
 level : D3
 tag: dp
 date:20230216
 */

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int testCase = 1; testCase <= T; testCase++) {
            int n = sc.nextInt();
            int limit = sc.nextInt();
            int[] dp = new int[limit + 1];
            int[][] arr = new int[n][2];

            for (int i = 0; i < n; i++) {
                int point = sc.nextInt();
                int cal = sc.nextInt();
                arr[i][0] = point;
                arr[i][1] = cal;
            }

            for (int i = 0; i < n; i++) {
                int p = arr[i][0];
                int c = arr[i][1];
                for (int j = limit; j >= 0; j--) {
                    if (j - c < 0) break;
                    dp[j] = Math.max(dp[j - c] + p, dp[j]);
                }
            }

            System.out.println("#" + testCase + " " + dp[limit]);
        }
        sc.close();
    }
}