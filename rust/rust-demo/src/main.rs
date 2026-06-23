fn flag_test(flag: bool) -> Result<&'static str, &'static str> {
    if flag {
        return Ok("yes");
    }
    Err("No")
}

fn get_flag(flag: bool) -> Result<&'static str, &'static str> {
    let ans = flag_test(flag)?;
    Ok(ans)
}

fn test_match(has_match: Option<bool>) -> Result<&'static str, &'static str> {
    match has_match {
        Some(msg) => {
            println!("{} success", msg);
            return Ok("success");
        }
        None => {
            println!("fail");
        }
    }
    Err("fail")
}

fn main() -> Result<(), &'static str> {
    let res = test_match(None)?;
    println!("{:?}", res);
    Ok(())
}
