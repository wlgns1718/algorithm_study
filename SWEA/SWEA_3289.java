/**
title: 서로소 집합
level : D4
tag: UnionSet
date:20230227
 */

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;
 
public class Solution {
    static int N,M,ord,x,y;
    static int[] p;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
         
        int TC = Integer.parseInt(br.readLine());
        StringTokenizer st = null;
        for(int tc = 1; tc<=TC; tc++) {
            bw.write("#"+tc+" ");
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken()); // 1부터 N까지 N개의 집합을 이루고 있다.
            M = Integer.parseInt(st.nextToken()); // 입력으로 주어지는 연산 수
            makeSet();
            for(int i = 0; i <M; i++) {
                st = new StringTokenizer(br.readLine());
                ord = Integer.parseInt(st.nextToken());
                x = Integer.parseInt(st.nextToken());
                y = Integer.parseInt(st.nextToken());
                if(ord==0) {
                    unionSet(x,y);
                }
                else if(ord ==1) {
                    if(findSet(x)==findSet(y)) {
                        bw.write(1+"");
                    }
                    else {
                        bw.write(0+"");
                    }
                }
            }
            bw.write("\n");
            bw.flush();
        }
    }
    private static void unionSet(int a, int b) {
        a = findSet(a);
        b = findSet(b);
         
        p[b] = a;
         
         
    }
    private static int findSet(int x) {
        if(p[x]==x) {
            return x;
        }
        return p[x]=findSet(p[x]);
    }
 
    static void makeSet() {
        p = new int[N+1];
        for(int i=0; i<=N; i++) {
            p[i] = i;
        }
    }
 
}