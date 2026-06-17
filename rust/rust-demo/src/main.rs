fn main() {
    let mut test = String::from("Hello World");
    let str1 = &test;
    let str2 = &test;
    println!("{} {}", str1, str2);

    let str3 = &mut test;
    str3.push_str("!!!");
    println!("{}", str3);
    println!("{}", test)

}
