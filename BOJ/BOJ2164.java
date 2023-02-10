/**
title: 카드2
level : Silver4
tag: data_structure, Queue
date:20230210
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class Boj2164 {
	public static void main(String args[]) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		ArrayDeque<Integer> q = new ArrayDeque<>();
		
		int N = Integer.parseInt(br.readLine());
		
		for(int i=1; i<=N; i++) {
			q.offer(i);
		}
		System.out.println(q);
		int temp;
		while(q.size()>1) {
			q.poll();
			temp = q.poll();
			q.offer(temp);
		}
		System.out.println(q.poll());
	}
}
