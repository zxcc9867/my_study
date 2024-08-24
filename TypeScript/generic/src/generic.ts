/**
제네릭 함수

T에 함수를 호출할 때 매개변수의 타입을 할당한다. 
 */

function func<T>(value: T): T {
  return value;
}

let number = 100;

let num = func(10);

func(true);

let str = func("string");

// 타입 스크립트에서 튜플을 지정하는 방법 -> 타입을 지정해주어야 한다.
let num_literal: [number, number, number] = [1, 2, 3];

let num_array: number[] = [1, 2, 3]; // 배열 형태로 지정

func(num_literal);

let num_literalV2 = func<[number, number, number]>([1, 2, 3]);

let test = func(["1"] as string[]);

func(num_array);
