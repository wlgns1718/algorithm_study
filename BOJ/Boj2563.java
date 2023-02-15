/**
title: 색종이
level : silver5
tag: implementation
date:20230215
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Boj2563 {

	static int[][] paper = new int[101][101];
	static int sum = 0;
	static int x, y;

	public static void main(String args[]) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			x = Integer.parseInt(st.nextToken());
			y = Integer.parseInt(st.nextToken());
			for (int p = 0; p < 10; p++) {
				for (int q = 0; q < 10; q++) {
					paper[x + p][y + q] = 1;
				}
			}

		}
		for (int p = 0; p < 101; p++) {
			for (int q = 0; q < 101; q++) {
				sum += paper[p][q];
			}
		}
		System.out.println(sum);

	}
}
