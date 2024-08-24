// function swap(a : any, b : any){
//   return [b, a];
// }

// const [a, b] = swap(1, "2");

// console.log(a, b);


// function returnFirstValue<T>(data : [T,...unknown[]]){
//     return data[1]
// }

// let num = returnFirstValue(["1",0,1,2])


function getLength<T extends { length : number}>(data : T){
    return data.length
}

// 배열 , 문자열 모두 length라는 속성을 가지고 있다. 

// let var12 = getLength(1)

let var1 = getLength([1,2,3])

let var2 = getLength("12345")

let var3 = getLength( {length : 10}) // 객체 형태 -> 함수를 통해 data라는 매개변수의 length라는 속성이 있으면 그 값을 반환 

console.log(var1)