fn main() {
    // let str = String::from("abc");
    // let str_new = str;
    // println!("{}",str_new);
    // let a = 1;
    // let b = a;
    // println!("{}",a);

    let str = String::from("codex");
    let str1 = &str;
    let mut str2 = &str;
    println!("{} {} {}",str1,str2,str);

    str2 = &String::from("new");

    let str3 = str;
    println!("{}, {}",str3, str2);
    // println!("{}",str);
}
