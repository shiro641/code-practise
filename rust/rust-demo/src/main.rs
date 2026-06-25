fn test_ok_or(flag:bool)->Result<&'static str, &'static str>{
    let test = match flag {
        true=>Some("success"),
        false=>None
    };

    test.ok_or("err")
}


fn main() -> Result<(), &'static str> {
    let res = test_ok_or(true)?;
    println!("{:?}", res);
    Ok(())
}
