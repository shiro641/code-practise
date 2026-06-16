fn main() {
    let mut test = String::from("Hello World");
    let new = &mut test;
    // let new_read = &test;
    new.push_str("!!!");
    println!("{}", new);

}
