/**
title: 수영장
level : 모의 SW 역량테스트
tag: dp
date:20230214
 */

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

class Solution {
	static int[] charge = new int[4];
	static int[] plan = new int[12];
	static ArrayList<Integer> dp = new ArrayList<>();

	public static void main(String args[]) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int TC = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= TC; tc++) {
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 0; i < 4; i++) {
				charge[i] = Integer.parseInt(st.nextToken());
			} // 비용받기
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < 12; i++) {
				plan[i] = Integer.parseInt(st.nextToken());
			} // 달 계획받기
			System.out.println(Arrays.toString(plan));
			dp.add(0);
			for (int i = 0; i < 12; i++) {
				if (i == 0 || i == 1) {
					dp.add(Math.min((plan[i] * charge[0]) + dp.get(i),charge[1] + dp.get(i)));
					continue;
				}
				int temp = Math.min(plan[i] * charge[0] + dp.get(i), charge[1] + dp.get(i)); //하루 요금 한달요금 빅교
				if(i==2) {
					dp.add(Math.min(temp,charge[2]));
					continue;
				}
				dp.add(Math.min(temp, dp.get(i - 2) + charge[2]));
			}
			System.out.println(dp.get(dp.size()-1));
			dp.clear();
		}

	}

}