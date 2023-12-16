package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
	
	// 문자열 표기
	var string1 = "안녕하세요\n"
	var string2 = "\ud55c\uae00"			// 한글	: 유니코드 문자코드
	var string3 = "\U0000d55c\U0000ae00"	// 한글	: 유니코드 문자코드
	var string4 = "\xed\x95\x9c\xea\xb8\x80"// 한글 : UTF-8 인코딩 방식
	var string5 = `Hello, World
						안녕하세요`			 // 여러줄 표기 ==> 백쿼트``

	fmt.Println("[ basic println ]")
    fmt.Println(string1, string2, string3, string4, string5)
	/*
	[ fmt.Println ]
	안녕하세요
	 한글 한글 한글 Hello, World
							안녕하세요
	*/
	
	// 문자열 크기
	var string6 = "한글"
	var string7 = "Hello, World"

	fmt.Println("\n[ len(string) ] - 데이터 크기")
	fmt.Println(									string6, "\n :",len(string6))
	fmt.Println("\\xed\\x95\\x9c\\xea\\xb8\\x80(", 	string4, ")\n :",len(string4))
	fmt.Println(									string7, "\n :",len(string7))
	/*
	[ len(string) ] - 데이터 크기
	한글 
	: 6
	\xed\x95\x9c\xea\xb8\x80( 한글 )
	: 6
	Hello, World 
	: 12
	*/

	// 문자열 길이
	fmt.Println("\n[ utf8.RuneCountInString(string) ] - 길이")
	fmt.Println(									string6, "\n :",utf8.RuneCountInString(string6))
	fmt.Println("\\xed\\x95\\x9c\\xea\\xb8\\x80(", 	string4, ")\n :",utf8.RuneCountInString(string4))
	fmt.Println(									string7, "\n :",utf8.RuneCountInString(string7))
	/*
	[ utf8.RuneCountInString(string) ] - 길이
	한글 
	: 2
	\xed\x95\x9c\xea\xb8\x80( 한글 )
	: 2
	Hello, World 
	: 12
 	*/

	// 문자열 연산
	fmt.Println("\n[ 문자열 연산 ]")
	fmt.Println("( \\ud55c\\uae00 == 한글 )? :", ( string2 == string6 ))
	fmt.Println("( \\ud55c\\uae00 + string5 + 한글 )? :", string2 + string5 + string6)
    fmt.Println("<\\ud55c\\uae00>[0]? :", string2[0])
	
	// 기존 'printf'도 가능
	fmt.Printf("<\\ud55c\\uae00>[1]? : %c \n", string2[1])
	// string7[1] = H	==>	컴파일 오류
	/*
	[ 문자열 연산 ]
	( \ud55c\uae00 == 한글 )? : true
	( \ud55c\uae00 + string5 + 한글 )? : 한글Hello, World
							안녕하세요한글
	<\ud55c\uae00>[0]? : 237
	<\ud55c\uae00>[1]? :  
	*/
}
