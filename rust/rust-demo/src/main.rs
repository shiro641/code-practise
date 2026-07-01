
use clap::Parser;

fn test_anyhow(is_none: bool) -> anyhow::Result<&'static str> {
    let pre_match = match is_none {
        true => Some("success"),
        false => None,
    };

    let res = pre_match.ok_or_else(|| anyhow::anyhow!("err happen"))?;
    println!("reach");
    Ok(res)
}

enum Person {
    Basic{name:String, age:i32},
    Id(String)
}


// !! todo: 这里有问题，周末看一下
// fn print_info(info: Person) ->bool {
//     match info {
//         Basic{name, age}=>{
//             println!("basic is{} {}", name, age);
//             return true
//         }
//         Id(info)=>{
//             println!("id is{}", info);
//             return false
//         }
//     }

// }


#[derive(Debug, Clone, Parser)]
struct people {
    name: String,
    right: bool,
    
    #[arg(long)]
    port:String
}




fn main() -> Result<(), &'static str> {
    let args = people::parse();
    let tom = people {
        name: String::from("tom"),
        right:false,
        port:args.port
    };

    let marry = tom.clone();

    println!("{:?}, {:?}", tom, marry);

    // let basic = Person::Basic{ name: String::from("tom"), age: 12 };
    // let id = Person::Id(String::from("12345"));


    // println!("{}",print_info(basic));
    // println!("{}",print_info(id));

    Ok(())
}
