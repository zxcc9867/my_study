/**
 * 
 * 제네릭 인터페이스
 */

import { Console } from "console"

interface KeyPair<T,K>{
    key : T
    value : K
}

let keyPair : KeyPair<string,number> = {
    key : "key",
    value : 0
}

let KeyPair2 : KeyPair<boolean, string []> = {
    key : true,
    value : ["1"]
}

/**
 * 
 * 인덱스 시그니처 
 */


interface Map<v> {
    [key : string] : v // 키의 타입은 스트링, 값의 타입은 number로 만드는 것 
}

let num : Map<string> = {
    key : "value",
    key2 : "haha"
}

let booleanMap : Map<boolean> = {
    key : true
}

/**
 * 
 * 제네릭 타입 별칭 
 */

type Map2<v> = {
    [key:string] : v 
}

let stringMap2 : Map2<string> = {
    key : "hello"
}

/** 
 * 
 * 제네릭 인터페이스의 활용 예시 
 * 유저 관리 프로그램 
 * 유저 구분 : 학생 유저 / 개발자 유저 
 * 
 * 
 */

interface Student {
    type : "student"
    school : string
}

interface Developer {
    // [key : string] : string | string[]
    // name : string 
    type : "developer"
    school : string
    skill : string[]
}



interface User<T> {
    name : string 
    profile : T
}

const developer : User<Developer> = {
    name : '박원진',
    profile : {
        type : "developer",
        skill : [ "TypeScript" , "Python"],
        school : "동의대학교"
    }
}

const user : User<Student> = {
    name : '익명',
    profile : {
        type : "student",
        school : "학교"
    }
}

console.log(developer)

function goToSchool (user : User<Student>){
    if (user.profile.type !== 'student'){
        console.log("잘못 왔습니다.")
        return; // 함수를 종료한다. 
    }

    const school = user.profile.school
    console.log((`${school}로 등교완료`));
    
}

const unknown_user : User<Student> = {
    name : "익명의 사용자",
    profile : {
        type : "student",
        school : "모름"
    },
    
}


function HiDeveloper(user : User<Developer>){
    if (user.profile.type !== 'developer'){
        console.log("잘못오셨습니다.")
        return
    }else if ( 'typescript' in user.profile.skill){
        console.log("typescript를 할 수 있군요 ! ")
    }else if ( 'python' in user.profile.skill){
        console.log('python을 할 수 있군요 ! ')
    }
}

