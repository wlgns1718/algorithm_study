/*
title: 암호생성기
level : D3
tag: Queue
date:20230210

*/
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

class Solution {
	static int N;
	static int[] numbers;
	static int small;
	static int temp1;
	static boolean tri;
	public static void main(String args[]) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		ArrayDeque<Integer> q  = new ArrayDeque<Integer>();
		for(int tc=1; tc<=10; tc++) {
			bw.write("#"+tc+" ");
			tri = true;
			N = Integer.parseInt(br.readLine());
			StringTokenizer st = new StringTokenizer(br.readLine());
			numbers = new int[8];
			for(int i = 0; i<8; i++) {
				numbers[i] = Integer.parseInt(st.nextToken());
				if(i ==0) {
					small = numbers[i];
				}
				if(small > numbers[i]) {
					small = numbers[i];
				}
			}//numbers 배열 완성
			int temp = (int) small/15;
			for(int i = 0; i<8; i++) {
				numbers[i] = numbers[i] - ((temp-1) * 15);
				q.offer(numbers[i]);
			}
			System.out.println(q);
			while(true) {
				for(int idx = 1; idx<=5; idx++) {
					temp1 = q.poll() - idx;
					if (temp1<=0) {
						q.offer(0);
						tri =false;
						break;
					}
					q.offer(temp1);
				}
				if(!tri) {
					break;
				}
			}
			for(int i = 0; i<8; i++) {
				bw.write(q.poll()+" ");
			}
			bw.flush();
			System.out.println();
		}
	}
}
