fn check_score(score: i32) -> Result<&'static str, &'static str> {
    if score >= 60 {
        return Ok("pass");
    } else {
        return Err("fail");
    }
}

fn divide(a: i32, b: i32) -> Result<i32, &'static str> {
    if b == 0 {
        return Err("divide zero");
    }
    Ok(a / b)
}

fn positive_double(a: i32, b: i32) -> Result<i32, &'static str> {
    if b <= 0 {
        return Err("not positive");
    }
    Ok(a * b)
}

fn positive_double_add(a: i32, b: i32, c: i32) -> Result<i32, &'static str> {
    if c <= 0 {
        return Err("not positive");
    }
    let res = match positive_double(a, b) {
        Ok(nub) => nub + c,
        Err(message) => return Err(message),
    };
    Ok(res)
}

fn to_even(a: i32) -> Result<i32, &'static str> {
    if a % 2 == 0 {
        return Err("不是奇数");
    }
    Ok(a)
}

fn add_two_after_even(a: i32) -> Result<i32, &'static str> {
    let res = match to_even(a) {
        Ok(even) => even,
        Err(message) => return Err(message),
    };
    Ok(res + 2)
}

fn main() {
    println!(
        "{:?} {:?}",
        positive_double(2, 2),
        positive_double_add(2, 2, 3)
    );
    println!(
        "{:?}",
        add_two_after_even(2)
    )

    // println!("{:?}", ans)
}
